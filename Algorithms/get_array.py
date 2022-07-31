import requests
# from polygon import RESTClient
import polygon

# Date Time Functions
import datetime

# Statistics Functions
import numpy


def get_stock_price_for_day(ticker, day):
    apiKey = '59QUbittfbkmR4n3z9h4vBcTV8euOkRh'
    api_url = f'https://api.polygon.io/v1/open-close/{ticker}/{day}?adjusted=true&apiKey={apiKey}'
    data = requests.get(api_url).json()
    return data


def get_array_of_prices(ticker, stock_name, start_date, end_date, market, stock_type, current_event, csvd):

    # sets time intervals for date time
    delta = datetime.timedelta(days=1)

    while (start_date <= end_date):
        stock_val = get_stock_price_for_day(
            ticker, start_date.strftime("%Y-%m-%d"))

        # check if there is a value (non holiday)
        if (stock_val.get('high') != None):
            row = ticker + '|' + stock_name + '|' + start_date.strftime("%Y-%m-%d") + '|' + str(
                (stock_val['high'] + stock_val['low']) / 2) + '|' + market + '|' + stock_type + '|' + current_event + '\n'
            csvd.write(row)

            # write to a new file

        # iterate through days
        start_date += delta
    return 0


def get_array():
    stockType = 'blue chip'
    startDate = datetime.date(2022, 2, 1)
    endDate = datetime.date(2022, 2, 5)
    currentEvent = 'none'
    with csvStocks as csvs, csvData as csvd:
        for line in csvs:
            i = 0
            index = 0
            column = 0
            ticker = ''
            market = ''
            stockName = ''
            while i < len(line):
                if column != 3:
                    if line[i] == '"':
                        i += 1
                        while line[i] != '"':
                            i += 1
                    if line[i] == ',':
                        # csvd.write(line[index:i] + '|')
                        if column == 0:
                            ticker = line[index:i]
                        elif column == 1:
                            stockName = line[index:i]
                        else:
                            market = line[index:i]
                        # row = line[index:i] + '|'
                        index = i + 1
                        column += 1
                    i += 1
                else:
                    i += 1
            get_array_of_prices(ticker, stockName, startDate, endDate,
                                market, stockType, currentEvent, csvd)


csvData = open('csvData.csv', 'w')
csvStocks = open('stocks-list.csv', 'r')
get_array()

csvData.close()
csvStocks.close()
