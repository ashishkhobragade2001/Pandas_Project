import pandas as pd

# Create two dictionaries
dict1 = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
}

dict2 = {
    "id": [2, 3, 4],
    "age": [25, 30, 35]
}
def merge_operation(df1, df2):

    # Convert dictionaries to DataFrames
    df1 = pd.DataFrame(dict1)
    df2 = pd.DataFrame(dict2)

    # Perform a join using merge
    result = pd.merge(df1, df2, on="id", how="inner")  # Inner join on the "id" column
    print("Inner Join:\n", result)


    result_left = pd.merge(df1, df2, on="id", how="left")
    print("\nLeft Join:\n", result_left)

    # Perform an outer join
    result_outer = pd.merge(df1, df2, on="id", how="outer")
    # Perform a left join
    print("\nOuter Join:\n", result_outer)

    # transform data means row to column and column to row
    trasform = df1.T
    print("trasport data :\n", trasform)

merge_operation(dict1, dict2)