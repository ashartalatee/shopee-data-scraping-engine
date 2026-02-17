import pandas as pd
from pathlib import Path
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4


# PATH SETUP


BASE_DIR = Path(__file__).resolve().parent.parent
input_path = BASE_DIR / "03_output" / "clean_shopee_products.csv"
output_path = BASE_DIR / "03_output" / "market_report.pdf"

df = pd.read_csv(input_path)


# BASIC METRICS


total_products = len(df)
avg_price = df["price"].mean()

bins = [0, 20000, 50000, 100000, 200000, 1000000]
labels = ["<20K", "20-50K", "50-100K", "100-200K", "200K+"]

df["price_range"] = pd.cut(df["price"], bins=bins, labels=labels)
price_dist = df["price_range"].value_counts().sort_index()
dominant_price = price_dist.idxmax()

capacity_dist = df["capacity_ml"].value_counts().sort_index()
dominant_capacity = capacity_dist.idxmax()

low_comp = price_dist[price_dist < price_dist.mean()]
gap_zones = list(low_comp.index)


# BUILD PDF


doc = SimpleDocTemplate(str(output_path), pagesize=A4)
elements = []

styles = getSampleStyleSheet()

title_style = styles["Heading1"]
normal_style = styles["Normal"]

elements.append(Paragraph("SHOPEE MARKET INTELLIGENCE REPORT", title_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", normal_style))
elements.append(Spacer(1, 0.2 * inch))

elements.append(Paragraph("KEY METRICS", styles["Heading2"]))
elements.append(Spacer(1, 0.2 * inch))

metrics = [
    f"Total Products Analyzed: {total_products}",
    f"Average Price: Rp {avg_price:,.0f}",
    f"Dominant Price Range: {dominant_price}",
    f"Dominant Capacity: {dominant_capacity} ml",
]

elements.append(
    ListFlowable(
        [ListItem(Paragraph(m, normal_style)) for m in metrics],
        bulletType='bullet'
    )
)

elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("MARKET OPPORTUNITY ANALYSIS", styles["Heading2"]))
elements.append(Spacer(1, 0.2 * inch))

gap_text = f"Low competition price zones detected: {', '.join(gap_zones)}."

elements.append(Paragraph(gap_text, normal_style))
elements.append(Spacer(1, 0.3 * inch))

elements.append(Paragraph("STRATEGIC INSIGHT", styles["Heading2"]))
elements.append(Spacer(1, 0.2 * inch))

insight_text = f"""
The current market is concentrated in the {dominant_price} range,
with the majority of products offering around {dominant_capacity} ml capacity.

The average market price is Rp {avg_price:,.0f},
indicating a mid-tier competitive landscape.

Entry into lower competition price zones such as
{', '.join(gap_zones)} may present strategic opportunities,
subject to demand validation and differentiation strategy.
"""

elements.append(Paragraph(insight_text, normal_style))

# Build PDF
doc.build(elements)