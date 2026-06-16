Customer Segmentation Analysis: Identifying High-Value Shopper Groups Using K-Means Clustering
📌 Project Overview
Business Problem: Retail businesses often treat all customers the same, missing opportunities to tailor marketing, promotions, and inventory decisions to distinct shopper behaviors.
Objective: This project analyzes a U.S. retail shopping dataset (3,900 records) to answer one core question:
> \*"Can customers be grouped into distinct segments based on purchasing behavior, and what marketing strategies would work best for each group?"\*
Why it matters: Understanding customer segments allows a business to personalize promotions, optimize inventory by segment, and improve customer retention — directly impacting revenue and marketing ROI.
---
🗂️ Dataset
Detail	Description
Source	[Add dataset source / Kaggle link]
Size	3,900 records, [X] columns
Key fields	Age, Gender, Purchase Amount, Category, Frequency of Purchases, Discount Applied, Subscription Status, Location, Season
Time period	[Add if relevant]
---
🛠️ Tools & Technologies
Python: Pandas, NumPy (data cleaning & preparation)
Scikit-learn: K-Means Clustering, PCA (dimensionality reduction)
Matplotlib / Seaborn: Data visualization
SQL: Data extraction and aggregation queries
Jupyter Notebook: Analysis environment
---
🔍 Methodology
Step 1 — Defining the Question
Started with a clear, business-relevant question (see Project Overview) to keep the analysis focused and avoid scope creep.
Step 2 — Data Exploration & Cleaning
Reviewed dataset structure (`.info()`, `.describe()`, `.head()`) to understand data types, null values, and distributions
Checked for duplicates, missing values, and inconsistent categories
Converted categorical fields (e.g., subscription status, discount applied) into numeric formats suitable for clustering
Verified numeric fields (e.g., purchase amount) for outliers and incorrect entries
Step 3 — Feature Engineering & Preprocessing
Selected features relevant to customer behavior (purchase amount, frequency, category preferences, discount usage)
Standardized/scaled features using `StandardScaler` since K-Means is distance-based
Applied PCA to reduce dimensionality while retaining maximum variance, and to visualize clusters in 2D
Step 4 — Clustering Analysis
Used the Elbow Method and Silhouette Score to determine the optimal number of clusters (k=4)
Applied K-Means Clustering to segment customers into 4 distinct groups
Profiled each cluster by average spend, purchase frequency, age, and category preference
Step 5 — Visualization
2D PCA scatter plot showing cluster separation
Bar charts comparing average spend and frequency across clusters
Demographic breakdown (age/gender distribution) per cluster
---
📊 Key Insights & Recommendations
Segment	Profile	Recommendation
Segment 1 – High-Value Loyalists	High spend, frequent purchases, low discount sensitivity	Offer exclusive early access / loyalty rewards rather than discounts
Segment 2 – Discount-Driven Shoppers	Moderate spend, high discount usage	Target with seasonal promotions and flash sales
Segment 3 – Occasional Browsers	Low frequency, low spend	Re-engagement campaigns (email/SMS reminders, first-purchase incentives)
Segment 4 – Young Trend Followers	Younger demographic, category-specific (e.g., apparel/accessories)	Social-media-led campaigns and trend-based product bundles
---
📁 Repository Structure
```
customer-segmentation-analysis/
│
├── data/
│   └── shopping\_trends.csv
│
├── notebooks/
│   └── customer\_segmentation\_analysis.ipynb
│
├── images/
│   ├── elbow\_method.png
│   ├── pca\_clusters.png
│   └── cluster\_profiles.png
│
├── README.md
└── requirements.txt
```
---
▶️ How to Run This Project
Clone the repository
```
   git clone https://github.com/dharanidharanrx-alt/customer-segmentation-analysis.git
   ```
Install dependencies
```
   pip install -r requirements.txt
   ```
Open `notebooks/customer\_segmentation\_analysis.ipynb` in Jupyter Notebook or Google Colab
Run all cells to reproduce the analysis
---
🔐 Note on Data Privacy
This project uses anonymized/public data. In real-world deployments (e.g., for markets like Singapore), customer segmentation work would need to comply with relevant data protection regulations such as PDPA, including data minimization and anonymization practices.
---
👤 Author
Dharanidharan
Data Analyst | SQL, Python, Power BI, Machine Learning
🔗 www.linkedin.com/in/dharaniddj | 📧 dharanidharanrx@gmail.com
