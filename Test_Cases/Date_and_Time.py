import pandas as pd
from datetime import datetime
def date_and_time(file):
    data = pd.read_csv(file)

    # fetch perticular date column
    date_ = pd.to_datetime(data["order_date"])
    #print(date_)

    ###@@@@@@@@@@@@@@@ calculate age
    #today date
    today_date = datetime.now()
    print(today_date)
    data["date_of_birth"] = pd.to_datetime(data["date_of_birth"], format="%d-%m-%y")
    data["Age"] = (today_date - data["date_of_birth"]).dt.days // 365
    print(data)

file = "D:\\CREDENCE CLASS\\AUTOMATION\\Pandas\\Resources\\orders.csv"
date_and_time(file)
##@@@@@@@@@@ map function
def map_fun(amount):
    return  amount*2

def test_map_fun(file):
    data = pd.read_csv(file)
    data["amount"] = data["amount"].map(map_fun)
    print(data)
test_map_fun(file)

