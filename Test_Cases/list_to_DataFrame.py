import pandas as pd

ls = [["Ashish", 123], ["Babubhai", 456], ["Shivaji", 789]]
di = { 'Name' : ['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'],
          'Marks' : [98, 89, 99, 87, 90, 83, 99],
          'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female'] }
def conver_list_to_Dataframe(ls):
    data = pd.DataFrame(ls, columns=["Name", "number"])
    print(data)

# calling
conver_list_to_Dataframe(ls)

def dict_to_DataFrame(di):
    data = pd.DataFrame(di)
    print(data)

# calling 
dict_to_DataFrame(di)

import pandas as pd
from datetime import datetime


def get_current_date_and_next_leap_year():
    # Get current date using pandas
    current_date = pd.Timestamp(datetime.now()).date()

    # Determine the next leap year
    current_year = current_date.year
    next_leap_year = current_year + (4 - current_year % 4)
    if (current_year % 4 == 0 and current_year % 100 == 0 and current_year % 400 != 0):
        next_leap_year += 4  # Skip if the current year is divisible by 4 but not a leap year

    return current_date, next_leap_year


# Example usage
current_date, next_leap_year = get_current_date_and_next_leap_year()
print(f"Current Date: {current_date}, Next Leap Year: {next_leap_year}")
