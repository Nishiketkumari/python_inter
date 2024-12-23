import numpy as np
from scipy import stats
import pandas as pd

array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

mean_1d = np.mean(array_1d)
median_1d = np.median(array_1d)
mode_1d = stats.mode(array_1d, keepdims=True).mode[0]
std_dev_1d = np.std(array_1d)

mean_2d = np.mean(array_2d)
median_2d = np.median(array_2d)
mode_2d = stats.mode(array_2d, axis=None, keepdims=True).mode[0]
std_dev_2d = np.std(array_2d)

mean_3d = np.mean(array_3d)
median_3d = np.median(array_3d)
mode_3d = stats.mode(array_3d, axis=None, keepdims=True).mode[0]
std_dev_3d = np.std(array_3d)


data = {
    'ord_no': [70001, np.nan, 70002, 70004, np.nan, 70005, np.nan, 70010, 70003, 70012, np.nan, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', np.nan, '2012-08-17', '2012-09-10', '2012-07-27', '2012-09-10',
                 '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002, 5003, 5001, np.nan, 5002, 5001, 5001, np.nan, 5003, 5002, 5003, np.nan]
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull())

df.to_csv('csv1.csv', index=False)
df_read = pd.read_csv('csv1.csv')
print("\nDataFrame from CSV:")
print(df_read)

columns_with_missing = df.columns[df.isnull().any()]
print("\nColumns with at least one missing value:")
print(columns_with_missing)

missing_count = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_count)

df = df.replace({np.nan: np.nan})

df_no_missing_rows = df.dropna()
print("\nDataFrame with rows having any missing value dropped:")
print(df_no_missing_rows)

df_no_missing_cols = df.dropna(axis=1)
print("\nDataFrame with columns having any missing value dropped:")
print(df_no_missing_cols)

df_no_all_missing_rows = df.dropna(how='all')
print("\nDataFrame with rows where all elements are missing dropped:")
print(df_no_all_missing_rows)

df_at_least_2_nan = df[df.isnull().sum(axis=1) >= 2]
print("\nDataFrame with rows having at least 2 NaN values:")
print(df_at_least_2_nan)

total_missing = df.isnull().sum().sum()
print("\nTotal missing values in the DataFrame:")
print(total_missing)
