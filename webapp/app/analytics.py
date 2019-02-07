import pandas as pd
import sqlite3

query_true =  """
    select {0}, 
    count(*)
    from churn
    where churn = True
    group by {0};"""

query_false =  """
    select {0}, 
    count(*)
    from churn
    where churn = False
    group by {0};"""

def get_columns():
    conn = sqlite3.connect("webapp.db")
    cur = conn.cursor()
    result_columns = list(cur.execute("""PRAGMA table_info(churn);"""))
    columns = list(map(lambda x: x[1], result_columns[1:]))
    cur.close()
    conn.close()
    return columns

def get_statistics(value,query=True):
    #get grouped by churn
    conn = sqlite3.connect("webapp.db")
    cur = conn.cursor()
    if query == True:
        result = list(cur.execute(query_true.format(str(value))))
    else:
        result = list(cur.execute(query_false.format(str(value))))
    cur.close()
    conn.close()
    return result