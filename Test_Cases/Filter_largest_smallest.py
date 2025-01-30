import pandas as pd
from datetime import datetime

file = "D:\\CREDENCE CLASS\\AUTOMATION\\Pandas\\Resources\\orders.csv"
def filter(file):
    data = pd.read_csv(file)

    # smallest value
    smallest_amount = data["amount"].nsmallest(1)
    print("smallest val is :\n", smallest_amount)

    # max 3 amount value
    max_amount = data["amount"].nlargest(3)
    print("max 3 amount is :\n", max_amount)

    # gender or department count
    gender_count = data["gender"].value_counts()
    print("gender count : ", gender_count)

    ## group by
    group_by = data[["gender","amount"]].groupby("gender").describe()
    print("group by function :\n",group_by)

    ## where
    where_fun = data[["name","gender","amount"]].where(data["amount"]>5000)
    print("greater than 5000 : \n",where_fun)
filter(file)