from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

report_path = BASE_DIR / "reports" / "market_report.json"
scoring_path = BASE_DIR / "reports" / "market_scoring.json"
recommendation_path = BASE_DIR / "reports" / "recommendation.txt"

output_pdf = BASE_DIR / "reports" / "executive_report.pdf"

# LOAD DATA
with open(report_path) as f:
    report = json.load(f)

with open(scoring_path) as f:
    scoring = json.load(f)

with open(recommendation_path, encoding="utf-8") as f:
    recommendation = f.read()

# CREATE PDF
c = canvas.Canvas(str(output_pdf), pagesize=letter)
width, height = letter

y = height - 50

def draw_line(text, size=10, space=15):
    global y
    c.setFont("Helvetica", size)
    c.drawString(50, y, text)
    y -= space

# TITLE
draw_line("EXECUTIVE MARKET INSIGHT REPORT", 14, 25)

# SECTION 1
draw_line("1. Executive Summary", 12, 20)
draw_line(f"Market Score: {scoring.get('market_score', 0)}")
draw_line("This market shows moderate opportunity based on current data.")

y -= 10

# SECTION 2
draw_line("2. Market Overview", 12, 20)
draw_line(f"Total Products: {report.get('total_products', 0)}")
draw_line(f"Dominant Price Range: {report.get('dominant_price_range', '-')}")
draw_line(f"Price Distribution: {report.get('price_distribution', {})}")

y -= 10

# SECTION 3
draw_line("3. Competitive Landscape", 12, 20)
draw_line(f"Competition Score: {scoring.get('competition_score', 0)}")
draw_line("Indicates level of market saturation and seller density.")

y -= 10

# SECTION 4
draw_line("4. Opportunity Analysis", 12, 20)
draw_line(f"Opportunity Score: {scoring.get('opportunity_score', 0)}")
draw_line(f"Gap Zones: {report.get('gap_opportunities', [])}")

y -= 10

# SECTION 5
draw_line("5. Final Recommendation", 12, 20)

for line in recommendation.split("\n"):
    draw_line(line)

# SAVE
c.save()

print("Executive report generated")