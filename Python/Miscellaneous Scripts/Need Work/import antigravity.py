from antigravity import geohash
import yfinance as yf
import datetime
import pandas as pd

current_date = datetime.datetime.now()
current_date = current_date.strftime('%Y-%m-%d')

n_coordinate = input("What is your current North coordinate? ")
w_coordinate = input("What is your current West coordinate? ")

dow_today = yf.download("djia", start=current_date, end=current_date)
dow_opening = dow_today['Open'].iloc[-1]
dow_opening = str(dow_opening)
dow_opening = bytes(dow_opening, 'utf-8')

# Found this on Stack Overflow. Might help.
# def get_current_price(symbol):
# ticker = yf.Ticker(symbol)
#todays_data = ticker.history(period='1d')
# return todays_data['Close'][0]

# print(get_current_price('TSLA'))


geohash(n_coordinate, w_coordinate, current_date + dow_opening)
