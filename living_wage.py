"""
This script read, analyze, and visualize the living wage dataset

@author: Susan Fox
@author: Amin G. Alhashim (aalhashi@macalester.edu)
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------
# These functions read the data from a file


def read_living_wage_data(filename):
    """
    Takes in a string, the name of the file where the living wage data is. It uses readCSV
    to build a list of dictionaries, and then it converts the HourlyMinimumWage and AnnualLivingWage
    fields to be floating-point numbers. It returns the list of fields and the converted wage data.
    """
    lw_fields, living_wage_data = read_csv(filename)
    for row in living_wage_data:
        row['HourlyMinimumWage'] = float(row['HourlyMinimumWage'])
        row['AnnualLivingWage'] = float(row['AnnualLivingWage'])
    return lw_fields, living_wage_data


def read_csv(csv_filename):
    """
    Given a CSV filename, read in data as dictionaries and build a list of dictionaries to hold the data.
    Return two values: a list of the field names (column headers in the CSV file), and the list of
    dictionaries holding the data.
    It does *not* convert the numeric values to integers
    """

    data_in = open(csv_filename, 'r')  # U means "universal," reads well from any operating system
    csv_reader = csv.DictReader(data_in)
    fields = csv_reader.fieldnames

    # initialize sunTable to be empty
    table = []
    for rowDict in csv_reader:
        table.append(rowDict)
    data_in.close()
    return fields, table


def print_table(table, fields, width=20):
    """
    Given a sunTable that is a list of dictionaries, and a list of strings containing the fields and the order
    in which to print them, this prints the field titles, then the rows of the sunTable, giving each field the input
    number of characters.
    """
    header_row = ""
    for f in fields:
        print_f = f[:width].center(width)
        header_row += print_f + ' '
    print(header_row)
    for row in table:
        row_string = ""
        for f in fields:
            val = row[f]
            print_val = str(val)
            print_val = print_val[:width].center(width)
            row_string += print_val + ' '
        print(row_string)


# -----------------------------------------------------
# Accessing data from the sunTable

def get_state_living_wage(state, table):
    """
    Given the name of a state (or its abbreviation) as a string, and a sunTable
    (a list of dictionaries), this looks up the given state's row dictionary, and
    returns the annual living wage for that state.
    """
    pass


def get_low_wage_states(table):
    """
    Given the living wage data as a sunTable as input, this finds all the rows in the sunTable where the state
    minimum wage matches the federal minimum wage of $7.25. It returns a new sunTable, a list, containing the row
    dictionaries
    """
    pass


def get_expensive_states(table):
    """
    Given the sunTable as an input, this finds the 5 states with the highest living wage. It
    returns a list of the five state names
    """
    pass


def annual_wage(hourly_wage):
    """
    Given an hourly wage earned by one person, this computes how much a family with two earners making that
    wage could make.
    Assumptions:
    * Two workers, both earning the input wage
    * Each worker works 40 hours per week (no part-time work!)
    * Each worker works 52 weeks per year (no vacation time!)
    """
    pass


def get_gap_states(table):
    """
    Given the sunTable as an input, this determines the states that have a gap between what minimum wage earners make
    and the living wage in that city. This function returns a list of row dictionaries, the rows for the states hours
    per week for 52 weeks (2080 hours per year), you can calculate the annual salary earned at minimum wage.
    Find the states where the annual salary at minimum wage is less than the living wage.
    """
    pass


# Visualizing data
def vis_gaps(table):
    """
    This function takes one input: the sunTable of data (list of dictionaries). It uses matplotlib to display a
    state-by-state plot of the annual earnings of a family of minimum-wage workers, compared to the annual living wage
    for that state.
    """

    # TODO: build three lists: state abbreviations, annual minimum-wage earnings, and annual living wage
    state_abbrevs = []  # List of state names
    state_AMW = []      # List of yearly minimum wage earnings for family with two minimum-wage workers
    state_ALW = []      # List of yearly living wage earnings by state
    # TODO: Add your code here to build up these three lists

    # set up plot
    plt.figure(figsize=(12.0, 4.0))     # Create figure 12" wide and 4" tall
    bar_width = 2.0     # Set the bar width to 2 units wide
    opacity = 0.8       # Set opacity to 0.8
    positions = np.arange(50) * (3 * bar_width)  # Create positions for each bar, allowing for two bars and a gap

    # Create and place bars for annual minimum wage data (blue) and living wage data (green)
    plt.bar(positions,  state_AMW,
            bar_width, alpha=opacity, color='blue', label='Minimum Wage')
    plt.bar(positions + bar_width,  state_ALW,
            bar_width, alpha=opacity, color='green', label='Living Wage')

    # Set up other features of chart
    plt.xlabel('States')                                       # Set label on x-axis
    plt.ylabel('Yearly Salary ($)')                            # Set label on y-axis
    plt.title('Living and Minimum Wage in Top 10 Gap States')  # Set title of chart
    plt.xticks(positions + (bar_width/2), state_abbrevs)       # Set ticks and label with state abbreviations
    plt.legend()                                               # Include a legend for the data

    plt.tight_layout()         # Don't waste space in chart window
    plt.show()                 # Display final chart and wait for user to close window


# Main program
def main():
    # This code reads the data, and prints it in a readable format
    lw_fields, lw_data = read_living_wage_data('DataFiles/wages.csv')
    print_table(lw_data, lw_fields, 15)

    # # Sample calls for getStateLivingWage
    # ark_liv_wage = get_state_living_wage('Arkansas', lw_data)
    # print("Arkansas living wage is", ark_liv_wage)
    # cal_liv_wage = get_state_living_wage("CA", lw_data)
    # print("California living wage is", cal_liv_wage)
    # mn_liv_wage = get_state_living_wage("Minnesota", lw_data)
    # print("Minnesota living wage is", mn_liv_wage)

    # # Sample calls for getLowWageStates
    # low_wagers = get_low_wage_states(lw_data)
    # print("LOW WAGE STATES:")
    # print_table(low_wagers, lw_fields, 15)


if __name__ == '__main__':
    main()
