import subprocess
import sys
import logging
from pathlib import Path


# PATH SETUP


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / "02_scripts"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

log_file = LOG_DIR / "engine.log"


# LOGGING CONFIG


logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger()


# SCRIPT LIST


scripts = [
    "clean_normalize.py",
    "generate_market_report.py",
    "generate_market_pdf.py",
    "market_scoring_model.py",
]

def run_script(script_name):
    script_path = SCRIPTS_DIR / script_name
    logger.info(f"Running {script_name}")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        logger.error(f"Error in {script_name}")
        logger.error(result.stderr)
        sys.exit(1)
    else:
        logger.info(f"{script_name} completed successfully")


# PIPELINE EXECUTION


logger.info("===== SHOPEE MARKET INTELLIGENCE ENGINE STARTED =====")

for script in scripts:
    run_script(script)

logger.info("===== FULL PIPELINE COMPLETED SUCCESSFULLY =====")
