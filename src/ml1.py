import csv

#https://pythonprogramming.net/reading-csv-files-python-3/
def getRows():
    rows = []
    with open('D:\dev\data\irisorig.data') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            rows.append(row)
    return rows

def printall():
    rows = getRows()
    for row in rows:
        print(row)

def getRows2():
    with open('D:\dev\data\irisorig.data') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            yield row


def printall2():

    for row in getRows2():
        print(row)

printall2()





