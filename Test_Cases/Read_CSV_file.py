import pandas as pd

def read_csv_file(file):
    data = pd.read_csv(file)
    print(data)

    # how many  row and column are available in dataframe
    print(data.shape)

# calling
file = "D:\\CREDENCE CLASS\\AUTOMATION\\Pandas\\Resources\\sample_dataframe.csv"
read_csv_file(file)

def read_json_file(file2):
    data = pd.read_json(file2)
    print(data)

file2= "D:\\CREDENCE CLASS\\AUTOMATION\\Pandas\\Resources\\sample_dataframe.json"
#read_json_file(file2)