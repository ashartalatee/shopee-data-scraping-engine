import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / "02_scripts"

scripts = [
    "clean_normalize.py",
    "generate_market_report.py",
    "generate_market_pdf.py",
]

def run_script(script_name):
    script_path = SCRIPTS_DIR / script_name
    print(f"\n▶ Running {script_name} ...")
    
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f" Error in {script_name}")
        print(result.stderr)
        sys.exit(1)
    else:
        print(f" {script_name} completed.")

# =============================
# PIPELINE EXECUTION
# =============================

print("\n==============================")
print(" SHOPEE MARKET INTELLIGENCE ENGINE ")
print("==============================")

for script in scripts:
    run_script(script)

print("\n FULL PIPELINE COMPLETED SUCCESSFULLY")
