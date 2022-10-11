import yfinance as yf
import MySQLdb
import pandas as pd


# Step 1 -- Connection to my Data Base OlenaDB
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="OlenaDB")
# Step 2 --  Must create a Cursor object. It will let you execute all the queries you need from my data base
cur = db.cursor()



#
stockList = ["LCID", "AAPL", "TSLA"]
for stockTiker in stockList:
    stock = yf.Ticker(stockTiker)
    #insert min amd max value
    low = str( round(stock.info["dayLow"],2))
    high = str(round (stock.info["dayHigh"],2))
    # add f for string formatting/ f комбинирует старические строки с переменными
    sql =f'INSERT INTO Stocks (date_stocks, name_stock, max_day, min_day) VALUES (now() ,"{stockTiker}", {high},{low});'
    print (sql)
    cur.execute(sql)




# print all data from my Stocks Table
#cur.execute("SELECT * FROM Stocks")

# print all the first cell of all the rows
#for row in cur.fetchall():
    #print (row)

db.commit()
db.close()



