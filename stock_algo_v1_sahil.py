# Important info
# Polygon API Key: '59QUbittfbkmR4n3z9h4vBcTV8euOkRh'

# Imports

# Polygon API & Requests
import requests
# from polygon import RESTClient
import polygon

# Date Time Functions
import datetime

# Statistics Functions
import numpy

# Psuedocode
# Phase 0: Loading stock CSV
# 1) Load CSV of all stock tickers and industries
# 2) Determine delimiters

# Phase 1: Load all data up until current day
# 1) start date = start of the load cycle
# 2) end date = current day
# 3) for each day, pull average price per ticker from
#     3a) ticker list: combination of penny stocks, blue chip stocks
# 4) load into csv as
#     4a) ticker
#     4b) price
#     4c) score: value of stock everyday
#     4d) type of stock
#     4e) market
#     4f) current event
#     4g) newline

# Phase 2: Start a realtime streaming job that runs our script daily

# Phase 3: Algorithm

# getting stock ticker info from api per ticker, per day


def get_stock_price_for_day(ticker, day):
    apiKey = '59QUbittfbkmR4n3z9h4vBcTV8euOkRh'
    api_url = f'https://api.polygon.io/v1/open-close/{ticker}/{day}?adjusted=true&apiKey={apiKey}'
    data = requests.get(api_url).json()
    return data

# returning an array of the average price per non holiday per ticker


def get_array_of_prices(ticker, start_date, end_date, market, stock_type, current_event):

    # sets time intervals for date time
    delta = datetime.timedelta(days=1)

    while (start_date <= end_date):
        stock_val = get_stock_price_for_day(
            ticker, start_date.strftime("%Y-%m-%d"))

        # check if there is a value (non holiday)
        if (stock_val.get('high') != None):
            row = ticker + '|' + start_date.strftime("%Y-%m-%d") + '|' + str(
                (stock_val['high'] + stock_val['low']) / 2) + '|' + market + '|' + stock_type + '|' + current_event
            print(row)

            # write to a new file

        # iterate through days
        start_date += delta
    return 0

# def juan:
#     # read fil
#     for line in csv file:
#         ticker = substr(start, '|')
#         stock_name = 2
#         market = 3
#         stock_type_arr = 4
#         current_event_arr = 5
#         get_array_of_prices(ticker, start_date, end_date, market, stock_type, current_event)


# set historical data set and ticker
start_date = datetime.date(2022, 2, 1)
end_date = datetime.date(2022, 3, 1)
ticker = 'AAPL'
market = 'tech'
stock_type = 'blue chip'
current_event = 'none'
print(get_array_of_prices(ticker, start_date,
      end_date, market, stock_type, current_event))

# https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=*
