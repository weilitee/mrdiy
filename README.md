# SQL and Python Assessment

---

## SQL 

### Setup Instructions

1. **Download the CSV file**
   - Download `raw_data.csv` 

2. **Upload CSV into BigQuery**
   - Open your BigQuery console.
   - Create a table to hold the CSV data:
   - You can name it `raw_data` or choose any name.
   - Note the **full table path**, e.g., `your-project.dataset.raw_data`.

### Running the SQL Query

1. Open the SQL script `SQL.sql`
2. Copy the query and paste it into the BigQuery console.
3. Update the output table path in the `CREATE OR REPLACE TABLE` statement to create `final_pivot_table`. (Line 1)
4. Update the file path in the query to reference the table where you uploaded the CSV. (Line 17)
5. Execute the query to create the `final_pivot_table` to retrieve expected output.

---

## Python

### Setup Instructions

1. **Download the CSV file**  
   - Download `raw_data.csv`

2. **Install required Python packages**  
   - Ensure you have `pandas` installed:
   ```bash
   pip install pandas

### Running the Python Script

1.  Open VSCode or any Python IDE
3.  Copy and paste python code from `Python.py` into the console of your preferred IDE
4.  Update the CSV file path so it points to your local file (Line 4). For example:
```bash
df = pd.read_csv(r"C:\Users\YourName\Downloads\raw_data.csv")
```
4.  Run the code, a CSV file with the table will be created.
5.  Open CSV file in excel to see final expected table.


