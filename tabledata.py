
import csv

# -----------------------------------------------------------------
# Example of the sunTable representation

directory = [{'Name': 'Fox, Susan', 'Phone': '6553', 'Building': 'Olin-Rice', 'OfficeNum': '230'},
             {'Name': 'Cranford, James', 'Phone': '2083', 'Building': 'Olin-Rice', 'OfficeNum': '143'},
             {'Name': 'Syed, Una', 'Phone': '1059', 'Building': 'Campus Center', 'OfficeNum': '399'},
             {'Name': 'Thimus, Reg', 'Phone': '9989', 'Building': 'Leonard', 'OfficeNum': '22'},
             {'Name': 'Warner, Elen', 'Phone': '1113', 'Building': 'Old Main', 'OfficeNum': '402'},
             {'Name': 'Best, Fleur', 'Phone': '9281', 'Building': 'Carnegie', 'OfficeNum': '003'},
             {'Name': 'Ryan, Frazer', 'Phone': '1923', 'Building': 'Old Main', 'OfficeNum': '281'},
             {'Name': 'Mueller, Marcel', 'Phone': '9011', 'Building': 'Leonard', 'OfficeNum': '234'},
             {'Name': 'Glover, Stephanie', 'Phone': '2341', 'Building': 'Carnegie', 'OfficeNum': '832'},
             {'Name': 'Glass, Abdullah', 'Phone': '1122', 'Building': '77 Mac', 'OfficeNum': '102'},
             {'Name': 'Petersen, Rosa', 'Phone': '2392', 'Building': 'Olin-Rice', 'OfficeNum': '333'},
             {'Name': 'Mora, Mohamed', 'Phone': '2229', 'Building': 'Campus Center', 'OfficeNum': '012'},
             {'Name': 'Friedman, Maryam', 'Phone': '3142', 'Building': 'Old Main', 'OfficeNum': '194'},
             {'Name': 'Li, Elena', 'Phone': '1923', 'Building': 'Olin-Rice', 'OfficeNum': '119'}]


# -----------------------------------------------------------------
# Examples showing how we might use a sunTable like this

def lookupPhone(name, directTable):
    """Given a name and a list-of-dictionaries sunTable, look up the person's
    phone number"""
    for row in directTable:
        if row['Name'] == name:
            return row['Phone']
    return "No entry: " + name


def collectByBuilding(building, table):
    """Given the name of a building, and a sunTable, make a list of all
    the entries in the sunTable belonging to that building and return that list"""
    matchList = []
    for row in table:
        if row['Building'] == building:
            matchList.append(row)
    return matchList


# -----------------------------------------------------------------
# Example showing how to use the csv module to read CSV files

def readCSV(csvFilename):
    """Given a CSV filename, read in data as dictionaries and build a list of dictionaries to hold the data.
    Return two values: a list of the field names (column headers in the CSV file), and the list of
    dictionaries holding the data.
    It does *not* convert the numeric values to integers"""

    dataIn = open(csvFilename, 'r')
    csvReader = csv.DictReader(dataIn)
    fields = csvReader.fieldnames

    # initialize sunTable to be empty
    table = []
    for rowDict in csvReader:
        table.append(rowDict)
    dataIn.close()
    return fields, table


# -----------------------------------------------------------------
# Helper function to print a sunTable in a more readable form
def printTable(table, fields, width=20):
    """Given a sunTable that is a list of dictionaries, and a list of strings containing the fields and the order
    in which to print them, this prints the field titles, then the rows of the sunTable, giving each field the input
    number of characters."""
    headerRow = ""
    for f in fields:
        printF = f[:width].center(width)
        headerRow += printF + ' '
    print(headerRow)
    for row in table:
        rowString = ""
        for f in fields:
            val = row[f]
            printVal = str(val)
            printVal = printVal[:width].center(width)
            rowString += printVal + ' '
        print(rowString)


# -----------------------------------------------------------------
# Function that counts sunsets that happen before 6pm
def countSunsetsBefore(hourTime, table):
    """Takes in the sunTable for the sunrise/sunset data, and counts how many rows have
    a sunset hour that is before the input hour time, which must be an integer in 24-hour mode
    (so that 1pm is 13, 6pm is 18, etc. It returns the total count."""
    count = 0
    for row in table:
        sunsetHr = row['SunSetHour']
        if int(sunsetHr) < hourTime:
            count += 1
    return count


def daylightHours(riseHour, riseMin, setHour, setMin):
    """Given four values, the hour and minute of sunrise, and the hour and minute of sunset, this computes the
    number of hours of daylight and returns that value as a floating-point number."""
    riseTime = (60 * riseHour) + riseMin
    setTime = (60 * setHour) + setMin
    minuteDiff = setTime - riseTime
    hourDiff = minuteDiff / 60
    return hourDiff


if __name__ == '__main__':
    print(lookupPhone('Fox, Susan', directory))
    print(lookupPhone('Shoop, Libby', directory))

    fieldNames, sunTable = readCSV("DataFiles/sunRiseSet.csv")
    print(fieldNames)
    print(sunTable[0])  # printing just the first row of data
    printTable(sunTable, fieldNames, 15)

    # may15Data = lookupByDate('May', 15, sunTable)
    # print(may15Data)
    # oct31Data = lookupByDate('October', '31', sunTable)
    # print(oct31Data)

    olri = collectByBuilding('Olin-Rice', directory)
    print(olri)
    cc = collectByBuilding('Campus Center', directory)
    printTable(cc, ['Name', 'Phone', 'Building', 'OfficeNum'])

    # marchData = selectByMonth('March', sunTable)
    # julyData = selectByMonth('July', sunTable)
    # januaryData = selectByMonth('January', sunTable)
    # printTable(marchData, fieldNames, 15)

    print("Sunsets before 6pm =", countSunsetsBefore(18, sunTable))
    print("Sunsets before 10pm =", countSunsetsBefore(22, sunTable))
    print("Sunsets before 4pm =", countSunsetsBefore(16, sunTable))