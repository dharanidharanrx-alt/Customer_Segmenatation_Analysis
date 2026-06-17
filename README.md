# 🛍️ Retail Customer Sales Analysis – Shopping Malls

> **End-to-end Business Intelligence project** analysing 1,000 customer transactions across 10 Istanbul shopping malls (Jan 2021 – Mar 2023).  
> Tools: **SQL · Power BI · MS Excel**

---

## 📌 Project Overview

| Attribute | Details |
|---|---|
| **Dataset** | Shopping Mall Customer Transactions |
| **Record Count** | 1,000 transactions |
| **Date Range** | January 2021 – March 2023 |
| **Data Source** | SQL Database |
| **Malls Covered** | 10 Shopping Malls (Istanbul) |
| **Product Categories** | 8 (Clothing, Shoes, Technology, Books, Souvenirs, F&B, Cosmetics, Toys) |
| **Tools Used** | SQL, Power BI, MS Excel |

---

## 🎯 Business Objective

Extract actionable business insights from raw transactional data to support retail management decisions across four key areas:

- **Revenue optimisation** by category, mall, and customer segment
- **Customer demographic profiling** for targeted marketing
- **Seasonal trend identification** for inventory planning
- **Payment method analysis** to improve transaction efficiency

---

## 📊 Key Findings at a Glance

| KPI | Value | Business Significance |
|---|---|---|
| Total Revenue | $653,015.77 | Baseline for all revenue benchmarks |
| Total Transactions | 1,000 | Sample size for statistical validity |
| Average Order Value | $653.02 | Benchmark for upsell / cross-sell targets |
| Total Units Sold | 2,981 | Inventory demand baseline |
| Top Category | Clothing ($293K) | 44.9% of total revenue |
| Top Mall | Mall of Istanbul ($143K) | 21.9% of total revenue |
| Top Customer Segment | 55+ Age Group ($212K) | 32.4% of total revenue |
| Peak Revenue Month | July 2022 ($43.2K) | 66% above monthly average |

---
## 📋 Dataset Schema

| Column | Data Type | Description | Sample Value |
|---|---|---|---|
| `invoice_no` | TEXT | Unique transaction identifier | I100008 |
| `customer_id` | TEXT | Customer reference ID | C199951 |
| `gender` | TEXT | Customer gender (Male / Female) | Female |
| `age` | INTEGER | Customer age in years | 35 |
| `category` | TEXT | Product category purchased | Clothing |
| `quantity` | INTEGER | Number of units purchased | 3 |
| `price` | REAL | Total transaction price (USD) | 1500.40 |
| `payment_method` | TEXT | Cash / Credit Card / Debit Card | Credit Card |
| `invoice_date` | TEXT | Transaction date (DD-MM-YYYY) | 10-07-2022 |
| `shopping_mall` | TEXT | Name of the shopping mall | Mall of Istanbul |

---

## ✅ Data Quality Assessment

| Quality Dimension | Status | Notes |
|---|---|---|
| Completeness | ✅ PASS – No nulls detected | All 1,000 rows × 10 columns populated |
| Consistency | ✅ PASS – Uniform formats | Gender, category, and payment values standardised |
| Accuracy | ✅ PASS – Values in valid range | Age: 18–69 · Price: $6.99–$5,250 · Qty: 1–5 |
| Uniqueness | ✅ PASS – No duplicates | `invoice_no` verified as unique primary key |
| Timeliness | ⚠️ NOTE – Partial Mar 2023 | March 2023 has only 12 records (cut-off month) |

---

## 🔍 SQL Analysis – Business Questions 


•How is the shopping distribution according to gender?
•Which gender did we sell more products to?
•Which gender generated more revenue?
•How is the purchase category distributed relative to other columns?
•How is the shopping distribution according to age?
•Which age category did we sell more products to?
•Which age category generated more revenue?
•Does the payment method relate to other columns?
•How is the distribution of the payment method?

---

## 💡 Key Business Insights

### 1. Revenue Concentration (Pareto Analysis)
- Clothing, Shoes, and Technology = **94.2% of total revenue**
- These top 3 categories represent only 48.3% of transaction volume
- Bottom 5 categories contribute only 5.8% of revenue across 417 transactions

> **Implication:** Focus merchandising and promotional budget on top 3 categories. Consider reducing floor space for underperformers.

---

### 2. High-Value Segment – 55+ Customers
- 293 transactions (29.3%) but **$211,878 revenue (32.4%)**
- Highest average order value: **$723** vs $653 overall average
- Top categories: Clothing ($109K) and Shoes ($70K)

> **Implication:** Design loyalty and VIP programs specifically for the 55+ segment. Consider concierge shopping experiences and premium brand partnerships.

---

### 3. Technology Category Opportunity
- Only 42 transactions but **$134,400 revenue – AOV of $3,200 (5× overall)**
- 4.2% of transactions but 20.6% of revenue
- Low transaction count suggests demand exceeds current availability

> **Implication:** Expand Technology SKUs, introduce EMI/financing options, and create dedicated tech zones in top malls to capture latent demand.

---

### 4. Mall Performance Disparity
- Top 3 malls (Mall of Istanbul, Kanyon, Metrocity) = **53% of total revenue**
- Bottom 3 malls = only 15% of revenue
- Viaport Outlet: only 53 transactions but **$810 AOV – highest per transaction**

> **Implication:** Investigate underperforming malls for footfall data, lease cost efficiency, and category mix alignment. Viaport's premium AOV suggests repositioning opportunity.

---

### 5. Seasonal Revenue Patterns
- July 2022 peak: **$43,229** – highest single month
- May 2021 trough: **$16,585** – lowest full-month revenue
- Q3 (Jul–Sep) consistently outperforms Q2 (Apr–Jun) by **~25–40%**

> **Implication:** Front-load inventory procurement for Q3. Run clearance promotions in Q2 to improve cash flow. Target November with pre-holiday campaigns.

---

### 6. Payment Method Analysis

| Payment Method | Transactions | Revenue | Share |
|---|---|---|---|
| Cash | 420 (42%) | $285,770 | 43.8% |
| Credit Card | 366 (36.6%) | $218,659 | 33.5% |
| Debit Card | 214 (21.4%) | $148,587 | 22.8% |

> **Implication:** High cash dependency limits customer data capture. Transitioning 20% of cash transactions to digital via incentives would unlock personalised marketing for ~84 additional customers.

---

## 🚀 Strategic Recommendations

| Priority | Recommendation | Expected Impact | Timeline |
|---|---|---|---|
| 🔴 P1 – HIGH | Launch 55+ VIP Loyalty Program (Clothing & Shoes focus) | +15% frequency → ~$30K incremental annual revenue | Q1 2024 |
| 🔴 P1 – HIGH | Expand Technology SKUs + 12-month EMI options | Double transactions (42→84) → ~$130K additional revenue | Q2 2024 |
| 🟡 P2 – MED | Invest in Q3 peak readiness: inventory surge, staffing, mall campaigns | +10% Q3 performance → ~$25K incremental | Pre-Q3 2024 |
| 🟡 P2 – MED | Digital payment incentive (3–5% cashback for card payments) | Better analytics + reduced shrinkage + targeting | Q2 2024 |
| 🟢 P3 – STD | Reassess floor space for Books, Souvenir, F&B categories | Reallocate 15% space to Shoes/Tech for AOV uplift | Q3 2024 |
| 🟢 P3 – STD | Investigate underperforming malls (Forum Istanbul, Cevahir AVM) | Raise bottom-mall average from $32K to $45K annually | Q4 2024 |

---

## 🛠️ Methodology

| Phase | Activity | Output |
|---|---|---|
| 1. Data Quality | Check nulls, duplicates, format consistency, value ranges | All checks PASS |
| 2. Exploratory SQL | 9 core queries covering KPIs, categories, trends, demographics | Structured query results |
| 3. Insight Generation | Apply business framing to SQL outputs; identify patterns | 6 key business insights |
| 4. Visualisation | Power BI dashboard (4 report pages) | `Customer_Sales_Dashboard.png` |
| 5. Documentation | BA project documentation with strategic framing | This README + DOCX report |
| 6. Recommendations | Translate insights into prioritised action plan | 6 P1/P2/P3 recommendations |

---

## 🧰 Tools & Technologies

| Tool | Purpose | Skills Demonstrated |
|---|---|---|
| **SQL** | Data extraction, aggregation, segmentation | GROUP BY, CASE WHEN, aggregate functions, subqueries |
| **Power BI** | Interactive dashboard design and visualisation | DAX measures, data model, visual design |
| **MS Excel** | Data validation and supplementary analysis | PivotTables, conditional formatting |
| **Python (EDA)** | Exploratory data analysis and charts | pandas, matplotlib, seaborn |

---

## 📈 Power BI Dashboard

The dashboard is structured across 4 report pages following the standard BI pyramid — from summary KPIs down to granular product and demographic drill-downs:

1. **Executive KPI Summary** – Revenue, AOV, transactions, units sold
2. **Category & Mall Analysis** – Revenue by category and mall performance
3. **Customer Demographics** – Age group and gender breakdown
4. **Temporal & Payment Trends** – Monthly trends, seasonal patterns, payment mix

---

## 👤 Author

**Dharanidharan**  
Customer Data Analysis Project  
[LinkedIn](https://www.linkedin.com/in/dharaniddj) · [GitHub](https://github.com/dharanidharanrx-alt)

---

## 📄 License

This project is for portfolio and educational purposes. Dataset sourced from public domain.
