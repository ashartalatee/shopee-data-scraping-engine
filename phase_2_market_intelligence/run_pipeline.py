import subprocess
import sys
import logging
from pathlib import Path
import json



# PATH SETUP


BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / "02_scripts"
REPORTS_DIR = BASE_DIR / "reports"
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)

log_file = LOG_DIR / "engine.log"



# LOGGING CONFIG


logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger()



# SCRIPT PIPELINE FLOW (UPDATED)


scripts = [
    "clean_normalize.py",
    "generate_market_report.py",
    "generate_market_pdf.py",
    "market_scoring_model.py",
    "generate_executive_report.py",  # DAY 24
]



# EXECUTION FUNCTION


def run_script(script_name):
    script_path = SCRIPTS_DIR / script_name
    logger.info(f"Running {script_name}")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True
    )

    # tampilkan ke console juga (biar kamu lihat realtime)
    print(result.stdout)

    if result.returncode != 0:
        logger.error(f"Error in {script_name}")
        logger.error(result.stderr)

        print(f"❌ ERROR in {script_name}")
        print(result.stderr)

        sys.exit(1)
    else:
        logger.info(f"{script_name} completed successfully")
        print(f"✅ {script_name} done")



# RECOMMENDATION ENGINE


def run_recommendation():
    logger.info("Running Recommendation Engine")

    try:
        scoring_file = REPORTS_DIR / "market_scoring.json"

        if not scoring_file.exists():
            logger.error("market_scoring.json not found!")
            print("❌ market_scoring.json not found!")
            return

        with open(scoring_file, "r") as f:
            data = json.load(f)

        score = data.get("market_score", 0)
        competition = data.get("competition_score", 0)
        saturation = data.get("price_saturation_score", 0)

        recommendation = []

        
        # DECISION LOGIC
        

        if score < 30:
            recommendation.append("AVOID MARKET — terlalu lemah")
        elif 30 <= score < 60:
            recommendation.append("ENTER WITH CAUTION — validasi dulu")
        elif 60 <= score < 80:
            recommendation.append("GOOD OPPORTUNITY — layak masuk")
        else:
            recommendation.append("HIGH POTENTIAL — gas agresif")

        if saturation > 80:
            recommendation.append("Harga sangat padat (red ocean)")

        if competition < 20:
            recommendation.append("Kompetitor sedikit → peluang validasi demand")

        output_path = REPORTS_DIR / "recommendation.txt"

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("MARKET RECOMMENDATION\n")
            f.write("====================\n\n")
            for r in recommendation:
                f.write(f"- {r}\n")

        logger.info("Recommendation generated successfully")
        print("✅ Recommendation generated")

    except Exception as e:
        logger.error("Recommendation engine failed")
        logger.error(str(e))
        print("❌ Recommendation failed:", str(e))



# PIPELINE EXECUTION


def main():
    print("\n==============================")
    print(" SHOPEE MARKET INTELLIGENCE ENGINE")
    print("==============================\n")

    logger.info("===== ENGINE STARTED =====")

    # STEP 1: RUN ALL CORE SCRIPTS
    for script in scripts:
        run_script(script)

    # STEP 2: RECOMMENDATION
    run_recommendation()

    logger.info("===== FULL PIPELINE COMPLETED SUCCESSFULLY =====")

    print("\n🚀 PIPELINE SELESAI — SIAP DIJUAL KE CLIENT\n")



# ENTRY POINT


if __name__ == "__main__":
    main()