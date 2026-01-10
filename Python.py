import pandas as pd

# Load your raw data (update the path to your local CSV)
df = pd.read_csv(r"C:\Users\weili\Downloads\raw_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Calculate profit
df['profit'] = df['sales_amt'] - df['sales_cost']

# Calculate monthly totals per category
totals = df.groupby(['month', 'category']).agg(
    total_qty_cat=('sales_qty', 'sum'),
    total_amt_cat=('sales_amt', 'sum'),
    total_cost_cat=('sales_cost', 'sum'),
    total_profit_cat=('profit', 'sum')
).reset_index()

# Merge totals back to original dataframe
df = df.merge(totals, on=['month', 'category'], how='left')

# Calculate contributions as percentages
df['sales_qty_contribution'] = (df['sales_qty'] / df['total_qty_cat'] * 100).round(0).astype(int).astype(str) + '%'
df['sales_amt_contribution'] = (df['sales_amt'] / df['total_amt_cat'] * 100).round(0).astype(int).astype(str) + '%'
df['sales_cost_contribution'] = (df['sales_cost'] / df['total_cost_cat'] * 100).round(0).astype(int).astype(str) + '%'
df['profit_contribution'] = (df['profit'] / df['total_profit_cat'] * 100).round(0).astype(int).astype(str) + '%'

# Pivot table including category
pivot_df = df.pivot_table(
    index=['product', 'category'],
    columns='month',
    values=['sales_qty_contribution', 'sales_amt_contribution', 'sales_cost_contribution', 'profit_contribution'],
    aggfunc='first'
)

# Flatten column names
pivot_df.columns = [f"{month}_{metric}_by_category" for metric, month in pivot_df.columns]
pivot_df = pivot_df.reset_index()

# Extract unique month names from pivoted columns
month_names = [col.split('_')[0] for col in pivot_df.columns if col not in ['product','category']]
month_names = list(set(month_names))

# Sort months chronologically
month_ordered = sorted(month_names, key=lambda x: pd.to_datetime(x, format='%b-%y'))

# Define metric order
metrics = ['sales_qty_contribution_by_category',
           'sales_amt_contribution_by_category',
           'sales_cost_contribution_by_category',
           'profit_contribution_by_category']

# Fix Column order
fixed_columns = ['product', 'category']
for month in month_ordered:
    for metric in metrics:
        col_name = f"{month}_{metric}"
        if col_name in pivot_df.columns:
            fixed_columns.append(col_name)

pivot_df = pivot_df[fixed_columns]

# Sort by product
pivot_df = pivot_df.sort_values('product')

# Display and export
print(pivot_df)
pivot_df.to_csv("final_pivot_table.csv", index=False)
