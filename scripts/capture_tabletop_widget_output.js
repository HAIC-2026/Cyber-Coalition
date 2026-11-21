#!/usr/bin/env node
/*
 * Capture what the tabletop widget in web/index.html actually renders for each inject combination.
 *
 * This records TOOL OUTPUT only: the planning-picture sentence and the human-review questions the page
 * displays. It records no human review, no reviewer decision and no elapsed time. Every value is a
 * synthetic tabletop output. It is deterministic, so re-running it on the same page gives the same rows.
 *
 * Requires Playwright (npm i playwright, or an existing global install) and a Chromium build.
 * Usage:  node scripts/capture_tabletop_widget_output.js [pageUrl] [outFile]
 * Default pageUrl is file:// plus web/index.html; default outFile is data/tabletop-runs/widget_output_by_inject_set.csv
 */
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const pageUrl = process.argv[2] || 'file://' + path.join(root, 'web', 'index.html');
const outFile = process.argv[3] || path.join(root, 'data', 'tabletop-runs', 'widget_output_by_inject_set.csv');

const ALL = ['inject-power', 'inject-comms', 'inject-road', 'inject-language', 'inject-connectivity', 'inject-highrise'];
const DEFAULT_THREE = ALL.slice(0, 3);
const runs = [
  { id: 'T00', label: 'baseline: no injects', on: [] },
  { id: 'T01', label: 'page default: power, communications, road', on: DEFAULT_THREE },
  ...ALL.map((id, i) => ({ id: 'S' + String(i + 1).padStart(2, '0'), label: 'single inject: ' + id, on: [id] })),
  ...ALL.map((id, i) => ({ id: 'L' + String(i + 1).padStart(2, '0'), label: 'all six except ' + id, on: ALL.filter(x => x !== id) })),
  { id: 'A06', label: 'all six injects', on: ALL },
];

const csvCell = v => '"' + String(v).replace(/"/g, '""') + '"';

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(pageUrl, { waitUntil: 'load' });
  const rows = [];
  for (const run of runs) {
    const out = await page.evaluate(({ ALL, on }) => {
      for (const id of ALL) {
        const box = document.getElementById(id);
        box.checked = on.includes(id);
        box.dispatchEvent(new Event('change', { bubbles: true }));
      }
      return {
        summary: document.getElementById('tabletop-summary').textContent.trim(),
        questions: [...document.querySelectorAll('#tabletop-review li')].map(li => li.textContent.trim()),
        state: document.getElementById('tabletop-state').textContent.trim(),
      };
    }, { ALL, on: run.on });
    // With no injects the widget shows one placeholder list item, which is a prompt and not a review question.
    const placeholder = run.on.length === 0;
    const questionCount = placeholder ? 0 : out.questions.length;
    rows.push([run.id, run.label, run.on.join(';'), run.on.length, questionCount, placeholder ? 'yes' : 'no', out.summary, out.questions.join(' | '), out.state]);
  }
  await browser.close();

  const header = ['run_id', 'condition', 'injects_active', 'injects_active_count', 'review_questions_displayed', 'placeholder_shown_instead', 'planning_picture_text', 'review_questions_text', 'state_line'];
  fs.mkdirSync(path.dirname(outFile), { recursive: true });
  fs.writeFileSync(outFile, [header.map(csvCell).join(',')].concat(rows.map(r => r.map(csvCell).join(','))).join('\n') + '\n', 'utf8');
  console.log('Wrote ' + rows.length + ' rows to ' + path.relative(root, outFile) + ' from ' + pageUrl);
  for (const r of rows) console.log(r[0].padEnd(4) + String(r[3]).padStart(2) + ' active -> ' + r[4] + ' question(s)' + (r[5] === 'yes' ? ' (placeholder shown)' : '') + '  [' + r[1] + ']');
})().catch(e => { console.error(e); process.exit(1); });
