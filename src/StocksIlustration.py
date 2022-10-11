import pandas as pd
import MySQLdb
import plotly.express as px

# Step 1 -- Connection to my Data Base OlenaDB
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="OlenaDB")
# Step 2 --  Must create a Cursor object. It will let you execute all the queries you need from my data base
cur = db.cursor()

#
cur.execute("select aa.date_stocks, ts.tmin,ts.tmax,lu.lmin,lu.lmax,aa.amin,aa.amax from (select date_stocks, name_stock, max_day as lmax, min_day as lmin from Stocks WHERE name_stock ='LCID') lu join (select date_stocks, name_stock, max_day as tmax, min_day as tmin from Stocks WHERE name_stock ='TSLA') ts on (lu.date_stocks = ts.date_stocks) join (select date_stocks, name_stock, max_day as amax, min_day as amin from Stocks WHERE name_stock ='AAPL') aa on (ts.date_stocks = aa.date_stocks)")

# print all data from my Stocks Table
df = pd.DataFrame(cur.fetchall())
# rename columns
df = df.rename(columns={0: 'date_stocks', 1: 'ts.tesla_min', 2:'ts.tesla_max', 3:'lu.lucid_min',4: 'lu.lucid_max', 5:'aa.apple_min', 6:'aa.apple_max'})

print(list(df.columns))




fig = px.line(df, x='date_stocks', y=['lu.lucid_min','lu.lucid_max','aa.apple_min','aa.apple_max']) #'ts.tesla_min','ts.tesla_max'
fig.update_yaxes(tickprefix="$")
#annotation that indicate the last value automatically .iloc[-1]
#fig.add_annotation(
 #   dict(
  #      x = df['date_stocks'].iloc[-1],
   #     y = df['ts.tesla_max'].iloc[-1],
    #    text = 'TESLA MAX',
    #)
#)
fig.add_annotation(
    dict(
        x = df['date_stocks'].iloc[-1],
        y = df['lu.lucid_max'].iloc[-1],
        text = 'LUCID MAX',
    )
)
fig.add_annotation(
    dict(
        x = df['date_stocks'].iloc[-1],
        y = df['aa.apple_max'].iloc[-1],
        text = 'APPLE MAX',
    )
)

fig.show()


