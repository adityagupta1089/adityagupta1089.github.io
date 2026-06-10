#!/usr/bin/env python3
"""
Quick layout width test — run while the Jekyll server is up on :4000.
Fails if any key element's width deviates from the 800px target.
"""
from playwright.sync_api import sync_playwright
import sys

TARGET = 800
TOLERANCE = 2  # px

CHECKS = [
    (".wrapper.topround",          "Title card"),
    (".site-navigation",           "Nav bar"),
    (".topic-nav",                 "Topic pills"),
    (".page-content > .wrapper",   "Content wrapper"),
    (".page-content",              "Page content"),
]

def run():
    with sync_playwright() as pw:
        b = pw.firefox.launch()
        p = b.new_page()
        p.set_viewport_size({"width": 1040, "height": 800})
        p.goto("http://127.0.0.1:4000/")
        p.wait_for_timeout(800)

        failures = []
        for selector, label in CHECKS:
            el = p.query_selector(selector)
            if not el:
                failures.append(f"  MISSING  {label} ({selector})")
                continue
            w = el.bounding_box()["width"]
            status = "OK   " if abs(w - TARGET) <= TOLERANCE else "FAIL "
            msg = f"  {status}  {label:<30} {w:.1f}px"
            print(msg)
            if status.strip() == "FAIL":
                failures.append(msg)

        b.close()

        if failures:
            print("\nFAILURES:")
            for f in failures:
                print(f)
            sys.exit(1)
        else:
            print("\nAll widths match 800px ✓")

if __name__ == "__main__":
    run()
