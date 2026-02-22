import subprocess
import sys
import logging
from pathlib import Path


# ==============================
# PATH SETUP
# ==============================

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / "02_scripts"
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

log_file = LOG_DIR / "engine.log"


# ==============================
# LOGGING CONFIG
# ==============================

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger()


# ==============================
# SCRIPT PIPELINE FLOW
# ==============================

scripts = [
    "clean_normalize.py",
    "generate_market_report.py",
    "generate_market_pdf.py",
    "market_scoring_model.py",
]


# ==============================
# EXECUTION FUNCTION
# ==============================

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


# ==============================
# RECOMMENDATION ENGINE (DAY 23)
# ==============================

def run_recommendation():
    try:
        import json

        scoring_file = BASE_DIR / "reports" / "market_scoring.json"

        if not scoring_file.exists():
            logger.error("market_scoring.json not found!")
            return

        with open(scoring_file, "r") as f:
            data = json.load(f)

        score = data.get("market_score", 0)
        competition = data.get("competition_score", 0)
        saturation = data.get("price_saturation_score", 0)

        recommendation = []

        # DECISION LOGIC
        if score < 30:
            recommendation.append("❌ AVOID MARKET — terlalu lemah")
        elif 30 <= score < 60:
            recommendation.append("⚠️ ENTER WITH CAUTION — validasi dulu")
        elif 60 <= score < 80:
            recommendation.append("✅ GOOD OPPORTUNITY — layak masuk")
        else:
            recommendation.append("🔥 HIGH POTENTIAL — gas agresif")

        if saturation > 80:
            recommendation.append("⚠️ Harga sangat padat (red ocean)")

        if competition < 20:
            recommendation.append("💡 Kompetitor sedikit → peluang validasi demand")

        output_path = BASE_DIR / "reports" / "recommendation.txt"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("MARKET RECOMMENDATION\n")
            f.write("====================\n\n")
            for r in recommendation:
                f.write(f"- {r}\n")

        logger.info("Recommendation generated successfully")

    except Exception as e:
        logger.error("Recommendation engine failed")
        logger.error(str(e))


# ==============================
# PIPELINE EXECUTION
# ==============================

logger.info("===== SHOPEE MARKET INTELLIGENCE ENGINE STARTED =====")

for script in scripts:
    run_script(script)

# NEW STEP (DAY 23)
logger.info("Running Recommendation Engine")
run_recommendation()

logger.info("===== FULL PIPELINE COMPLETED SUCCESSFULLY =====")