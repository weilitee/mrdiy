# SQL Data Transformation: Pivot Table of Monthly Sales Contributions

## Description
This project transforms raw sales data into a pivot table showing monthly contributions for sales quantity, sales amount, sales cost, and profit by product and category. The resulting table helps analyze each product's contribution to the monthly totals by category.

---

## Setup Instructions

1. **Download the raw dataset**
   - Get the CSV file `raw_data.csv` from the `data/` folder.
   
2. **Import the CSV into your SQL environment**
   - **BigQuery**
     - Create a table named `raw_data` in your preferred dataset.
     - Upload `raw_data.csv` into the table.
   - **SQLite / PostgreSQL / MySQL**
     - Create a table named `raw_data` with the following columns:
       - `month`, `product`, `store_code`, `category`, `sales_qty`, `sales_amt`, `sales_cost`
     - Import the CSV into the table.

---

## Running the SQL Query

1. Open your  BigQuery console.
2. Open the SQL script: `queries/final_pivot_table.sql`.
3. Execute the query.
   - This will create a table named `final_pivot_table`.
   - The table will include:
     - Sales quantity contribution by category and month
     - Sales amount contribution by category and month
     - Sales cost contribution by category and month
     - Profit contribution by category and month


## Optional: Export Final Table

- After running the query, you can export `final_pivot_table` back to CSV for further analysis:
  - **BigQuery:** Use the "Export" feature.

