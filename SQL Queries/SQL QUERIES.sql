#Q1.How is the shopping distribution according to gender
select gender,sum(price) as revenue
from customer 
group by gender;
#Q2.Which gender did we sell more products to
select Gender,
SUM(quantity) AS Products_Sold
FROM customer
GROUP BY Gender
ORDER BY Products_Sold DESC;
#Q3.Which gender generated more revenue
select Gender,
SUM(Quantity * Price) AS Revenue
FROM customer
GROUP BY Gender
ORDER BY Revenue DESC;
#Q4.Distibution of purchase category relative to other columns need to clear
SELECT category,
COUNT(*) AS Purchases
FROM customer
GROUP BY category
ORDER BY Purchases DESC;
#Q5.How is the shopping distribution according to age
	SELECT Age,	
	COUNT(*) AS Purchases
	FROM customer
	GROUP BY Age
	ORDER BY Age;
#Q6.Which age category did we sell more products to. how age group is defined
SELECT
CASE
WHEN Age BETWEEN 18 AND 25 THEN '18-25'
WHEN Age BETWEEN 26 AND 35 THEN '26-35'
WHEN Age BETWEEN 36 AND 45 THEN '36-45'
WHEN Age BETWEEN 46 AND 55 THEN '46-55'
ELSE '55+'
END AS Age_Group,
SUM(Quantity) AS Products_Sold
FROM customer
GROUP BY Age_Group
ORDER BY Products_Sold DESC;
#Q7.Which age category generated more revenue
SELECT
CASE
WHEN Age BETWEEN 18 AND 25 THEN '18-25'
WHEN Age BETWEEN 26 AND 35 THEN '26-35'
WHEN Age BETWEEN 36 AND 45 THEN '36-45'
WHEN Age BETWEEN 46 AND 55 THEN '46-55'
ELSE '55+'
END AS Age_Group,
SUM(Quantity * Price) AS Revenue
FROM customer
GROUP BY Age_Group
ORDER BY Revenue DESC;
#Q8.does the payment method have relation is other columns
SELECT Payment_Method,
Gender,
COUNT(*) AS Transactions
FROM customer
GROUP BY Payment_Method, Gender;
#Q9.How is the distribution of payment method
SELECT Payment_Method,
COUNT(*) AS Total_Transactions
FROM customer
GROUP BY Payment_Method
ORDER BY Total_Transactions DESC;

------------------------------------------------------------------------------------------------------------------------------------
