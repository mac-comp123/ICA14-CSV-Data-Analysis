"""
File: LivingWageActivity.py

This file contains code for reading, analyzing, and visualizing the living wage dataset
"""

import csv
# To
# import matplotlib.pyplot as plt
# import numpy as np

# -----------------------------------------------------
# These functions read the data from a file


def readLivingWageData(filename):
    """Takes in a string, the name of the file where the living wage data is. It uses readCSV
    to build a list of dictionaries, and then it converts the HourlyMinimumWage and AnnualLivingWage
    fields to be floating-point numbers. It returns the list of fields and the converted wage data."""
    lwFields, livingWageData = readCSV(filename)
    for row in livingWageData:
        row['HourlyMinimumWage'] = float(row['HourlyMinimumWage'])
        row['AnnualLivingWage'] = float(row['AnnualLivingWage'])
    return lwFields, livingWageData


def readCSV(csvFilename):
    """Given a CSV filename, read in data as dictionaries and build a list of dictionaries to hold the data.
    Return two values: a list of the field names (column headers in the CSV file), and the list of
    dictionaries holding the data.
    It does *not* convert the numeric values to integers"""

    dataIn = open(csvFilename, 'r')  # U means "universal," reads well from any operating system
    csvReader = csv.DictReader(dataIn)
    fields = csvReader.fieldnames

    # initialize sunTable to be empty
    table = []
    for rowDict in csvReader:
        table.append(rowDict)
    dataIn.close()
    return fields, table


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


# -----------------------------------------------------
# Accessing data from the sunTable

def getStateLivingWage(state, table):
    """Given the name of a state (or its abbreviation) as a string, and a sunTable
    (a list of dictionaries), this looks up the given state's row dictionary, and
    returns the annual living wage for that state."""
    pass


def getLowWageStates(table):
    """Given the living wage data as a sunTable as input, this finds all the rows in the sunTable where the state
    minimum wage matches the federal minimum wage of $7.25. It returns a new sunTable, a list, containing the row
    dictionaries """
    pass


def getExpensiveStates(table):
    """Given the sunTable as an input, this finds the 5 states with the highest living wage. It
    returns a list of the five state names"""
    pass


def annualWage(hourlyWage):
    """Given an hourly wage earned by one person, this computes how much a family with two earners making that
    wage could make.
    Assumptions:
    * Two workers, both earning the input wage
    * Each worker works 40 hours per week (no part-time work!)
    * Each worker works 52 weeks per year (no vacation time!)
    """
    pass


def getGapStates(table):
    """Given the sunTable as an input, this determines the states that have a gap between what minimum wage earners make
    and the living wage in that city. This function returns a list of row dictionaries, the rows for the states hours
    per week for 52 weeks (2080 hours per year), you can calculate the annual salary earned at minimum wage.
    Find the states where the annual salary at minimum wage is less than the living wage."""
    pass

# -----------------------------------------------------
# Visualizing data


def visGaps(table):
    """This function takes one input: the sunTable of data (list of dictionaries). It uses matplotlib to display a
    state-by-state plot of the annual earnings of a family of minimum-wage workers, compared to the annual living wage
    for that state."""

    # TODO: build three lists: state abbreviations, annual minimum-wage earnings, and annual living wage
    stateAbbrevs = []  # List of state names
    stateAMW = []      # List of yearly minimum wage earnings for family with two minimum-wage workers
    stateALW = []      # List of yearly living wage earnings by state
    # TODO: Add your code here to build up these three lists

    # set up plot
    plt.figure(figsize=(12.0, 4.0))         # Create figure 12" wide and 4" tall
    barWidth = 2.0                          # Set the bar width to 2 units wide
    opacity = 0.8                           # Set opacity to 0.8
    positions = np.arange(50) * (3 * barWidth)  # Create positions for each bar, allowing for two bars and a gap

    # Create and place bars for annual minimum wage data (blue) and living wage data (green)
    plt.bar(positions,  stateAMW,
            barWidth, alpha=opacity, color='blue', label='Minimum Wage')
    plt.bar(positions + barWidth,  stateALW,
            barWidth, alpha=opacity, color='green', label='Living Wage')

    # Set up other features of chart
    plt.xlabel('States')                                       # Set label on x-axis
    plt.ylabel('Yearly Salary ($)')                            # Set labe on y-axis
    plt.title('Living and Minimum Wage in Top 10 Gap States')  # Set title of chart
    plt.xticks(positions + (barWidth/2), stateAbbrevs)         # Set ticks and label with state abbreviations
    plt.legend()                                               # Include a legend for the data

    plt.tight_layout()         # Don't waste space in chart window
    plt.show()                 # Display final chart and wait for user to close window


# -----------------------------------------------------
# Main program


if __name__ == '__main__':
    # This code reads the data, and prints it in a readable format
    lwFields, lwData = readLivingWageData('DataFiles/wages.csv')
    printTable(lwData, lwFields, 15)

    # # Sample calls for getStateLivingWage
    # arkLivWage = getStateLivingWage('Arkansas', lwData)
    # print("Arkansas living wage is", arkLivWage)
    # calLivWage = getStateLivingWage("CA", lwData)
    # print("California living wage is", calLivWage)
    # mnLivWage = getStateLivingWage("Minnesota", lwData)
    # print("Minnesota living wage is", mnLiWage)

    # # Sample calls for getLowWageStates
    # lowWagers = getLowWageStates(lwData)
    # print("LOW WAGE STATES:")
    # printTable(lowWagers, lwFields, 15)


