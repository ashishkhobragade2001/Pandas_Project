import pandas as pd

di = { 'Name' : ['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'],
          'Marks' : [98, 89, 99, 87, 90, 83, 99],
          'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female'] }
def aggregate_operation(di):
    data = pd.DataFrame(di)

    # sum of marks
    sum_marks = data["Marks"].sum()
    print("sum of marks is : ", sum_marks)

    # average marks
    avg_marks = data["Marks"].mean()
    print("Avarage marks is : ", avg_marks)

    # describe
    describe = data["Marks"].describe()
    print("describe marks  : ", describe)

    # cumsum
    cumsum = data["Marks"].cumsum()     # 1,2, 3, 5, 8, 13, 21..........
    print("cumsum is : ", cumsum)

    # max marks is
    max_marks = data["Marks"].max()
    print("Max marks is : ", max_marks)

    # count values
    count_val = data["Marks"].count()
    print("total count is : ", count_val)

    # first five marks
    fist_five_marks = data["Marks"].head()
    print("First five marks add : \n", fist_five_marks)

    # last 6 records
    last_six_marks = data["Marks"].tail(6)
    print("last six marks is :\n", last_six_marks)

    # check whether in data contain is null
    is_null  = pd.isna(data)
    print("null present or not : ",is_null)

    # drop null
    print(data.dropna(how="any"))

## calling
#aggregate_operation(di)

file = "D:\\CREDENCE CLASS\\AUTOMATION\\Pandas\\Resources\\orders.csv"
def read_csv_file(file):
    data = pd.read_csv(file)

    # aggrigate function apply
    ag = data.groupby("gender").agg(median_amount=("amount", "median"))
    print("median is :\n", ag)

    #

read_csv_file(file)
