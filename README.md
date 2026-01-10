# SQL Data Transformation: Pivot Table of Monthly Sales Contributions

## Description
This project transforms raw sales data into a pivot table showing monthly contributions for sales quantity, sales amount, sales cost, and profit by product and category. The resulting table helps analyze each product's contribution to the monthly totals by category.

---

## Repository Structure

sql-data-transformation/
│
├── data/
│ └── raw_data.csv # CSV of the raw dataset
│
├── queries/
│ └── final_pivot_table.sql # SQL script to create the pivot table
│
└── README.md # This documentation


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

1. Open your SQL client or BigQuery console.
2. Open the SQL script: `queries/final_pivot_table.sql`.
3. Execute the query.
   - This will create a table named `final_pivot_table`.
   - The table will include:
     - Sales quantity contribution by category and month
     - Sales amount contribution by category and month
     - Sales cost contribution by category and month
     - Profit contribution by category and month

---

## Query Notes

- **Profit calculation:** `profit = sales_amt - sales_cost`.
- **Contribution percentages:** Calculated as `(metric / total per month-category) * 100`, rounded to the nearest whole number and formatted as a percentage (e.g., `25%`).
- **Pivoting:** The SQL pivots months from `Jan-25` to `Aug-25`. To add more months, update the `FOR month IN (...)` clause in the SQL.
- The query uses **window functions** to compute totals per month-category, ensuring efficient and accurate contribution calculations.

---

## Optional: Export Final Table

- After running the query, you can export `final_pivot_table` back to CSV for further analysis:
  - **BigQuery:** Use the "Export" feature.
  - **Other SQL engines:** Use standard CSV export commands.
