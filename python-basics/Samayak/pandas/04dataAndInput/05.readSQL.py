# Write a Python program to connect to a SQLite database named "company.db" and read the data from a table named "employees" into a DataFrame. Print the first 5 rows of the DataFrame.

import sqlite3
import pandas as pd

# connect to an SQLite db
conn = sqlite3.connect('company.db')

#SQL query to fetch data
query = "SELECT * FROM employees"

# Reading from SQL into a DataFrame

df = pd.read_sql(query, conn)

# display the data
print(df)