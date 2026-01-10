CREATE OR REPLACE TABLE `mrdiy-483917.sql_test_raw.final_pivot_table` AS
WITH metrics AS (
  SELECT
    month,
    product,
    category,
    sales_qty,
    sales_amt,
    sales_cost,
    -- Profit
    (sales_amt - sales_cost) AS profit,
    -- Calculate monthly totals per category
    SUM(sales_qty) OVER(PARTITION BY month, category) AS total_qty_cat,
    SUM(sales_amt) OVER(PARTITION BY month, category) AS total_amt_cat,
    SUM(sales_cost) OVER(PARTITION BY month, category) AS total_cost_cat,
    SUM(sales_amt - sales_cost) OVER(PARTITION BY month, category) AS total_profit_cat
  FROM `mrdiy-483917.sql_test_raw.raw_data`
),
formatted AS (
  SELECT
    month,
    product,
    category,
    -- Format contributions as percentages
    FORMAT("%.0f%%", ROUND(SAFE_DIVIDE(sales_qty, total_qty_cat) * 100, 0)) AS sales_qty_contribution,
    FORMAT("%.0f%%", ROUND(SAFE_DIVIDE(sales_amt, total_amt_cat) * 100, 0)) AS sales_amt_contribution,
    FORMAT("%.0f%%", ROUND(SAFE_DIVIDE(sales_cost, total_cost_cat) * 100, 0)) AS sales_cost_contribution,
    FORMAT("%.0f%%", ROUND(SAFE_DIVIDE(profit, total_profit_cat) * 100, 0)) AS profit_contribution
  FROM metrics
)
SELECT * 
FROM formatted
PIVOT(
  ANY_VALUE(sales_qty_contribution) AS sales_qty_contribution_by_category,
  ANY_VALUE(sales_amt_contribution) AS sales_amt_contribution_by_category,
  ANY_VALUE(sales_cost_contribution) AS sales_cost_contribution_by_category,
  ANY_VALUE(profit_contribution) AS profit_contribution_by_category
  FOR month IN ('Jan-25', 'Feb-25', 'Mar-25', 'Apr-25', 'May-25', 'Jun-25', 'Jul-25', 'Aug-25')
)
ORDER BY product;

