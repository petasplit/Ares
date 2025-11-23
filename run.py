# run.py - ARES v8.0 — FINAL FLOW
from scanner import GodTierScanner
from fusion_core import fusion_run_all
from exploiter import full_compromise_all

target = input("Target URL: ")

# 1. Fast discovery
GodTierScanner(target).scan()

# 2. True merged sqlmap + ghauri exploitation
fusion_run_all()

# 3. Final RCE/XSS on confirmed targets
full_compromise_all()

print(Panel("[bold red]ARES v8.0 — TARGET ANNIHILATED[/]"))
