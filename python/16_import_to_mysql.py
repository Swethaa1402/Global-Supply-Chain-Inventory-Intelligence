
import pandas as pd
import mysql.connector
from pathlib import Path

csv_path = Path("data/processed/supply_chain_cleaned.csv")

print("Reading cleaned CSV...")
df = pd.read_csv(csv_path, encoding="utf-8")
print(f"CSV rows: {len(df)}")

password = input("Enter your MySQL root password: ")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="supply_chain_intelligence"
)

cursor = connection.cursor()

# Create a separate table so the existing table remains untouched.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS supply_chain_cleaned_full
    LIKE supply_chain_cleaned
""")

# Clear only this dedicated import table if the script is rerun.
cursor.execute("TRUNCATE TABLE supply_chain_cleaned_full")
connection.commit()

columns = list(df.columns)
column_sql = ", ".join(f"`{col}`" for col in columns)
placeholders = ", ".join(["%s"] * len(columns))

insert_sql = (
    f"INSERT INTO supply_chain_cleaned_full "
    f"({column_sql}) VALUES ({placeholders})"
)

batch_size = 1000
inserted = 0

try:
    for start in range(0, len(df), batch_size):
        batch = df.iloc[start:start + batch_size]

        rows = []
        for row in batch.itertuples(index=False, name=None):
            values = []
            for value in row:
                if pd.isna(value):
                    values.append(None)
                elif hasattr(value, "item"):
                    values.append(value.item())
                else:
                    values.append(value)
            rows.append(tuple(values))

        cursor.executemany(insert_sql, rows)
        connection.commit()

        inserted += len(rows)
        print(f"Imported {inserted:,} / {len(df):,} rows")

    cursor.execute("SELECT COUNT(*) FROM supply_chain_cleaned_full")
    mysql_count = cursor.fetchone()[0]

    print(f"\nCSV rows: {len(df):,}")
    print(f"MySQL rows: {mysql_count:,}")

    if mysql_count == len(df):
        print("SUCCESS: All rows imported correctly!")
    else:
        print("WARNING: The row counts do not match.")

except Exception:
    connection.rollback()
    raise

finally:
    cursor.close()
    connection.close()
