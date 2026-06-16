"""
PRDA-05 | Retail Customer Sales Analysis – Shopping Malls
Exploratory Data Analysis (EDA) Script
Author  : Dharanidharan
Tools   : Python · pandas · matplotlib · seaborn
Dataset : 1,000 customer transactions across 10 Istanbul malls (Jan 2021 – Mar 2023)
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# ──────────────────────────────────────────────
# STAGE 1 – Load & Inspect Data
# ──────────────────────────────────────────────

df = pd.read_csv("data/customer_transactions.csv")

print("=" * 55)
print("STAGE 1 – DATA OVERVIEW")
print("=" * 55)
print(f"Shape          : {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"Columns        : {list(df.columns)}")
print(f"\nData Types:\n{df.dtypes}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
print(f"\nDuplicates     : {df.duplicated().sum()}")
print(f"\nSample Records:")
print(df.head())

# ──────────────────────────────────────────────
# STAGE 2 – Data Cleaning & Preprocessing
# ──────────────────────────────────────────────

print("\n" + "=" * 55)
print("STAGE 2 – DATA CLEANING")
print("=" * 55)

# Convert invoice_date to datetime
df["invoice_date"] = pd.to_datetime(df["invoice_date"], dayfirst=True)

# Extract time features
df["year"]  = df["invoice_date"].dt.year
df["month"] = df["invoice_date"].dt.month
df["month_name"] = df["invoice_date"].dt.strftime("%b %Y")
df["quarter"] = df["invoice_date"].dt.to_period("Q").astype(str)

# Create age groups (CASE WHEN equivalent in Python)
age_bins   = [17, 25, 35, 45, 55, 100]
age_labels = ["18–25", "26–35", "36–45", "46–55", "55+"]
df["age_group"] = pd.cut(df["age"], bins=age_bins, labels=age_labels)

print("✅  invoice_date converted to datetime")
print("✅  Age groups created: ", df["age_group"].value_counts().to_dict())
print(f"\nDate range     : {df['invoice_date'].min().date()} → {df['invoice_date'].max().date()}")

# ──────────────────────────────────────────────
# STAGE 3 – Key Metrics
# ──────────────────────────────────────────────

print("\n" + "=" * 55)
print("STAGE 3 – KEY METRICS")
print("=" * 55)

total_revenue = df["price"].sum()
total_txn     = len(df)
avg_order_val = df["price"].mean()
total_units   = df["quantity"].sum()

print(f"Total Revenue        : ${total_revenue:,.2f}")
print(f"Total Transactions   : {total_txn:,}")
print(f"Average Order Value  : ${avg_order_val:,.2f}")
print(f"Total Units Sold     : {total_units:,}")

# ──────────────────────────────────────────────
# STAGE 4 – Analysis & Visualisation
# ──────────────────────────────────────────────

sns.set_theme(style="whitegrid", palette="muted")
BLUE  = "#1F3B73"
TEAL  = "#2A9D8F"
AMBER = "#E9C46A"
CORAL = "#E76F51"
COLORS = [BLUE, TEAL, AMBER, CORAL, "#264653", "#F4A261", "#A8DADC", "#457B9D"]

fig, axes = plt.subplots(3, 2, figsize=(16, 18))
fig.suptitle(
    "Retail Customer Sales Analysis – Istanbul Shopping Malls\n1,000 Transactions · Jan 2021 – Mar 2023",
    fontsize=15, fontweight="bold", y=0.98
)

# ── Chart 1: Revenue by Category ──────────────
ax1 = axes[0, 0]
cat_rev = df.groupby("category")["price"].sum().sort_values(ascending=False)
bars = ax1.barh(cat_rev.index, cat_rev.values, color=COLORS[:len(cat_rev)])
ax1.set_title("Revenue by Product Category", fontweight="bold")
ax1.set_xlabel("Revenue (USD)")
ax1.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
for bar, val in zip(bars, cat_rev.values):
    ax1.text(bar.get_width() + 1000, bar.get_y() + bar.get_height() / 2,
             f"${val:,.0f}", va="center", fontsize=8)
ax1.invert_yaxis()

# ── Chart 2: Revenue by Age Group ─────────────
ax2 = axes[0, 1]
age_rev = df.groupby("age_group")["price"].sum()
bars2 = ax2.bar(age_rev.index, age_rev.values, color=COLORS[:len(age_rev)], edgecolor="white")
ax2.set_title("Revenue by Age Group", fontweight="bold")
ax2.set_xlabel("Age Group")
ax2.set_ylabel("Revenue (USD)")
ax2.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
for bar, val in zip(bars2, age_rev.values):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1000,
             f"${val/1000:.0f}K", ha="center", fontsize=9, fontweight="bold")

# ── Chart 3: Gender Revenue Split ─────────────
ax3 = axes[1, 0]
gender_rev = df.groupby("gender")["price"].sum()
ax3.pie(gender_rev.values, labels=gender_rev.index, autopct="%1.1f%%",
        colors=[BLUE, TEAL], startangle=140, textprops={"fontsize": 11})
ax3.set_title("Revenue Split by Gender", fontweight="bold")

# ── Chart 4: Payment Method Distribution ──────
ax4 = axes[1, 1]
pay_rev = df.groupby("payment_method")["price"].sum().sort_values(ascending=False)
bars4 = ax4.bar(pay_rev.index, pay_rev.values, color=[BLUE, TEAL, AMBER], edgecolor="white")
ax4.set_title("Revenue by Payment Method", fontweight="bold")
ax4.set_ylabel("Revenue (USD)")
ax4.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
for bar, val in zip(bars4, pay_rev.values):
    ax4.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1000,
             f"${val/1000:.0f}K", ha="center", fontsize=9, fontweight="bold")

# ── Chart 5: Monthly Revenue Trend ────────────
ax5 = axes[2, 0]
monthly = df.groupby(df["invoice_date"].dt.to_period("M"))["price"].sum()
monthly.index = monthly.index.astype(str)
ax5.plot(monthly.index, monthly.values, color=BLUE, linewidth=2.5, marker="o", markersize=4)
ax5.fill_between(monthly.index, monthly.values, alpha=0.15, color=BLUE)
ax5.set_title("Monthly Revenue Trend (Jan 2021 – Mar 2023)", fontweight="bold")
ax5.set_ylabel("Revenue (USD)")
ax5.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
ax5.tick_params(axis="x", rotation=45, labelsize=7)
# Annotate peak
peak_month = monthly.idxmax()
peak_val   = monthly.max()
ax5.annotate(f"Peak\n${peak_val/1000:.0f}K", xy=(peak_month, peak_val),
             xytext=(peak_month, peak_val + 3000),
             ha="center", fontsize=8, color=CORAL,
             arrowprops=dict(arrowstyle="->", color=CORAL))

# ── Chart 6: Top Mall by Revenue ──────────────
ax6 = axes[2, 1]
mall_rev = df.groupby("shopping_mall")["price"].sum().sort_values(ascending=True)
bars6 = ax6.barh(mall_rev.index, mall_rev.values, color=TEAL, edgecolor="white")
ax6.set_title("Revenue by Shopping Mall", fontweight="bold")
ax6.set_xlabel("Revenue (USD)")
ax6.xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
for bar, val in zip(bars6, mall_rev.values):
    ax6.text(bar.get_width() + 500, bar.get_y() + bar.get_height() / 2,
             f"${val/1000:.0f}K", va="center", fontsize=8)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("dashboard/Customer_Sales_Dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n✅  Dashboard saved → dashboard/Customer_Sales_Dashboard.png")

# ──────────────────────────────────────────────
# STAGE 5 – Insights Summary
# ──────────────────────────────────────────────

print("\n" + "=" * 55)
print("STAGE 5 – KEY INSIGHTS")
print("=" * 55)

# Insight 1 – Top categories
top3_cat = cat_rev.head(3)
top3_pct = top3_cat.sum() / total_revenue * 100
print(f"\n📌 Top 3 Revenue Categories:")
for cat, val in top3_cat.items():
    print(f"   {cat:<15} : ${val:>10,.2f}  ({val/total_revenue*100:.1f}%)")
print(f"   Combined share  : {top3_pct:.1f}% of total revenue")

# Insight 2 – 55+ segment
seg_55 = df[df["age_group"] == "55+"]
print(f"\n📌 55+ Customer Segment:")
print(f"   Transactions : {len(seg_55):,}  ({len(seg_55)/total_txn*100:.1f}%)")
print(f"   Revenue      : ${seg_55['price'].sum():,.2f}  ({seg_55['price'].sum()/total_revenue*100:.1f}%)")
print(f"   Avg Order Val: ${seg_55['price'].mean():,.2f}")

# Insight 3 – Technology category
tech = df[df["category"] == "Technology"]
print(f"\n📌 Technology Category:")
print(f"   Transactions : {len(tech):,}  ({len(tech)/total_txn*100:.1f}%)")
print(f"   Revenue      : ${tech['price'].sum():,.2f}  ({tech['price'].sum()/total_revenue*100:.1f}%)")
print(f"   Avg Order Val: ${tech['price'].mean():,.2f}  (5× overall average)")

# Insight 4 – Payment methods
print(f"\n📌 Payment Method Distribution:")
pay_summary = df.groupby("payment_method").agg(
    transactions=("price", "count"),
    revenue=("price", "sum")
).sort_values("transactions", ascending=False)
for pm, row in pay_summary.iterrows():
    print(f"   {pm:<15}: {row['transactions']:>3} txns  |  ${row['revenue']:>10,.2f}  ({row['transactions']/total_txn*100:.1f}%)")

print("\n" + "=" * 55)
print("✅  EDA Complete. See dashboard/ for visual outputs.")
print("=" * 55)
