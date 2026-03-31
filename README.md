# Sales Performance Analysis

## Project Overview
This project analyzes sales data to identify top-performing products, revenue-driving categories, and high-value customers. The goal is to generate business insights that could help support commercial decision-making.

## Business Question
Which products and categories generate the most revenue, and which ones appear to have lower commercial performance?

## Tools Used
- Python
- Pandas
- SQLite
- SQL

## Dataset
The dataset contains sales transaction data, including:
- Order ID
- Order Date
- Customer ID
- Product Name
- Category
- Quantity
- Price

## Analysis Performed
The project includes SQL-based analysis to answer key business questions such as:
- Which products generate the most revenue?
- Which categories contribute the most to total sales?
- Which products sell the most units?
- Which customers generate the highest revenue?

## Key Insights
- Some products contribute significantly more to total revenue than others.
- The Electronics category generated the highest revenue.
- The most sold products are not always the highest revenue drivers.
- A small group of customers contributes a large share of sales value.

## Files Included
- `main.py` → main analysis script
- `data/sales_data.csv` → dataset used for the analysis
- `sales_database.db` → SQLite database
- `README.md` → project documentation

## Visualizations

### Revenue by Product
![Revenue by Product](images/revenue_by_product.png)

### Revenue by Category
![Revenue by Category](images/revenue_by_category.png)

### Revenue by Customer
![Revenue by Customer](images/revenue_by_customer.png)

## Next Steps
Future improvements for this project may include:
- Profit margin analysis
- Monthly sales trends
- Interactive dashboard development
- excetuvie business summary
