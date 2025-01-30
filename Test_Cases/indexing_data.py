import pandas as pd
di = { 'Name' : ['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'],
          'Marks' : [98, 89, 99, 87, 90, 83, 99],
          'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female'] }

# iloc used for fetch perticular row from dataframe  by using ORDER INDEX
# loc is used to fetch perticular row from dataframe by using INDEX VALUE
def index_iloc(di):
    data = pd.DataFrame(di)
    var = data.iloc[3]
    print(var)
# calling
index_iloc(di)

def index_loc(di):
    data = pd.DataFrame(di)
    mittal_record = data.loc[3]
    print(mittal_record)

index_loc(di)