import sqlite3
import pandas as pd
from sqlalchemy.types import Integer, String, Boolean, Float

conn = sqlite3.connect("webapp.db")
cur = conn.cursor()

dataset = pd.read_csv('dataset_prepared.csv')
dataset.to_sql('churn', conn, index = False)

cur.close()
conn.close()