#!/usr/bin/env python3
"""Check that the hazard ledger table in web/index.html matches data/hazard-tract-ledger/ledger_summary.csv.

Run from the repository root:  python3 tests/check_ledger_matches_page.py
Exit status 0 means every number in the page table equals the CSV; non-zero lists the differences.
This checks the page against the committed CSV only. It does not re-query the sources.
"""
import csv
import html
import re
import sys

page = open("web/index.html", encoding="utf-8").read()
m = re.search(r'<table id="hazard-ledger-table">.*?<tbody>(.*?)</tbody>', page, re.S)
if not m:
    sys.exit("FAIL: hazard-ledger-table not found in web/index.html")
page_rows = []
for tr in re.findall(r"<tr>(.*?)</tr>", m.group(1), re.S):
    cells = [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<td>(.*?)</td>", tr, re.S)]
    page_rows.append(cells)
csv_rows = list(csv.DictReader(open("data/hazard-tract-ledger/ledger_summary.csv", encoding="utf-8")))
problems = []
if len(page_rows) != len(csv_rows):
    problems.append("row count page=%d csv=%d" % (len(page_rows), len(csv_rows)))
cols = ["hazard", "nri_field", "matched_in_source", "positive", "zero", "missing", "invalid", "not_in_source"]
for p, c in zip(page_rows, csv_rows):
    for name, val in zip(cols, p):
        if str(c[name]) != val:
            problems.append("%s / %s: page=%r csv=%r" % (c["hazard"], name, val, c[name]))
    if int(c["positive"]) + int(c["zero"]) + int(c["missing"]) + int(c["invalid"]) != int(c["matched_in_source"]):
        problems.append("%s: classes do not sum to matched" % c["hazard"])
    if int(c["matched_in_source"]) + int(c["not_in_source"]) != int(c["universe_461"]):
        problems.append("%s: matched + not in source != universe" % c["hazard"])
if problems:
    print("FAIL")
    print("\n".join(problems))
    sys.exit(1)
print("PASS: %d hazard rows on the page equal ledger_summary.csv; classes sum to matched and matched + not in source = 461" % len(page_rows))
