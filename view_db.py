import sqlite3
import pandas as pd

with sqlite3.connect("monitoring.db") as conn:

    # read the SQL table into a DataFrame
    df = pd.read_sql_query("SELECT * FROM checks", conn)

    # print the DataFrame
    print(df.head(30))
