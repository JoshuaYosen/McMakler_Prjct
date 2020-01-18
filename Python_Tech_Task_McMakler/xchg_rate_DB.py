import pandas as pd
import sqlite3 as lite

#load pickle into pandas DataFrame
data = pd.read_pickle("Tech_Task_Jr_Data_Engineer_Joshua_Yosen_Answers/Python_Tech_Task_McMakler/xchg_rate.pkl")

#initiate a connection to sqlite DB
conn = lite.connect('xchg_rate.db')

#load DataFrame into DataBase
data.to_sql("Exchange_Rates", conn, if_exists='replace')

#Run SQL query over DataBase to find max exchange rates for each currency in DataFrame
max_rates = pd.read_sql_query("SELECT MAX(GBP), MAX(USD), MAX(JPY) FROM Exchange_Rates", conn)

#stdout results from query
print(max_rates)
