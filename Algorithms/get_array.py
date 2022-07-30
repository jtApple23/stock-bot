# read file
# import csv
ticker_arr = []
stock_name_arr = []
market_arr = []
stock_type_arr = []
current_event_arr = []


csvData = open('csvData.csv', 'w')
csvStocks = open('stocks-list.csv', 'r')
# read fil
# for line in csvStocks:
# ticker = substr(start, '|')
# stock_name = 2
# market = 3
# stock_type_arr = 4
# current_event_arr = 5

with csvStocks as csvs, csvData as csvd:
    for line in csvs:
        i = 0
        index = 0
        column = 0
        while i < len(line):
            if column != 3:
                if line[i] == '"':
                    i += 1
                    while line[i] != '"':
                        i += 1
                if line[i] == ',':
                    csvd.write(line[index:i] + '|')
                    index = i + 1
                    column += 1
                i += 1
            else:
                i += 1
        csvd.write('stockType' + '|' + 'currentEvent' + '|' + '\n')

csvData.close()
csvStocks.close()
