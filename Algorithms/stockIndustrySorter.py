# This algo. will move data from stocks-list.csv to csvData.csv.  Industry column

import csv

csvData = open('csvData.csv', 'w')
csvStocks = open('stocks-list.csv', 'r')
stockList = csv.DictReader(csvStocks)

# bug on line 14 of csv

with csvStocks as csvs, csvData as csvd:
    for line in csvs:
        i = 0
        index = 0
        column = 0
        while i < len(line):
            if column == 0 or column == 2:
                if line[i] == ',':
                    if column == 0:
                        csvd.write(line[index:i] + '|')
                    else:
                        csvd.write(line[index:i] + '\n')
                    i += 1
                    index = i
                    column += 1
                i += 1
            elif column == 1:
                if line[i] == ',':
                    i += 1
                    index = i
                    column += 1
                i += 1
            else:
                i += 1

csvData.close()
csvStocks.close()
