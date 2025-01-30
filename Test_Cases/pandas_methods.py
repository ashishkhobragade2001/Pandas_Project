import pandas as pd

filename = "D://CREDENCE CLASS//AUTOMATION//Pandas//Resources//orders.csv"
data = pd.read_csv(filename)
#print(data)

##############@@@@@@@@@@@@@@ duplicate records @@@@@@@@@
def duplicate_Records_find(data):
    duplicates = data[data.duplicated(keep=False)]
    print(duplicates)
#duplicate_Records_find(data)

def duplicate_records_base_on_column(data):
    duplicate = data[data.duplicated(subset=['name', 'date_of_birth'], keep=False)]
    print(duplicate)
#duplicate_records_base_on_column(data)

##@@@@@ drop duplicate @@@@@
def drop_duplicate(data,filename):
    new_data = data.drop_duplicates(keep=False)
    new_data.to_csv(filename, index=False)
    print("delete duplicate succefull.")
#drop_duplicate(data,filename)

#####################@@@@ unique records@@@@@@@@@@@@
def unique_records_find(data):
    unique = data[~data.duplicated(keep=False)]
    print(unique)
#unique_records_find(data)

###@@@@@@@@@@@ count missing values
def null_count(data):
    missing=data.isnull().sum()
    print(missing)
#null_count(data)


##@@@@@@@@@@@@ sorting data in ascending order
def sorting_data(data):
    output = data.sort_values(by='amount', ascending=True)     #ascending
   # output = data.sort_values(by='amount', ascending=False)    #descending
    print(output)
#sorting_data(data)

##@@@@@@@@@@@@ group by
def group_by(data):
    output = data.groupby('gender')['amount'].sum()  # Group by a column and sum values
    #data.groupby(['col1', 'col2']).agg({'sales': 'sum', 'profit': 'mean'})  # Aggregate multiple columns
    print(output)
#group_by(data)

##@@@@@@@@@@@ column rename@@@@@
def rename_column(data, filename):
   data.rename(columns={'gender': 'GENDER'}, inplace=True)
   data.to_csv(filename, index=False)       ## to save this changes in original file
#rename_column(data,filename)
#print(data)

##@@@@@@@@@@@@ value change or Replace
def rename_or_Replace_values(data):
    data["name"] = data["name"].replace("Michael", "Ashish khobragade")
    data.to_csv(filename, index=False)
    print("chages successfull ...")
rename_or_Replace_values(data)

##@@@@@@@@@@@@ joing and merging
def join_and_merge(data):
    df_merged = pd.merge(data, data, on='id', how='inner')  # Inner Join
    print(df_merged)
#join_and_merge(data)

##end of method

