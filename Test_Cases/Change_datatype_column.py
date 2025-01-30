import pandas as pd

di = { 'Name' : ['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'],
          'Marks' : [98, 89, 99, 87, 90, 83, 99],
          'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female'] }

def change_datatype(di):
    data = pd.DataFrame(di)
    data['Marks'] = data['Marks'].astype(float)
    print(data)

# calling
#change_datatype(di)


#### @@@@@@@@@@@@@@@@ create empty dataframe
def create_empty_dataframe():
    data = pd.DataFrame()
    print(data)
# calling
create_empty_dataframe()