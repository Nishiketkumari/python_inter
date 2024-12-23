import pandas as pd

data = {
    'Name': ['Ajay', 'Vijay', 'Sanjay', 'Ajit', 'Vikas', 'Vipul', 'Rakesh'],
    'Jan': [10, 13, 17, 45, 22, 12, 31],
    'Feb': [21, 17, 15, 21, 56, 17, 86],
    'Mar': [23, 12, 16, 7, 76, 22, 27],
    'Apr': [31, 29, 13, 34, 34, 36, 41],
    'May': [7, 14, 18, 22, 22, 31, 32],
    'Jun': [22, 16, 10, 34, 16, 23, 22],
    'Jul': [20, 23, 27, 55, 32, 22, 41],
    'Aug': [31, 27, 25, 31, 66, 27, 33],
    'Sep': [33, 86, 26, 17, 86, 32, 37],
    'Oct': [41, 39, 23, 44, 44, 46, 51],
    'Nov': [17, 24, 28, 32, 32, 41, 42],
    'Dec': [32, 26, 20, 44, 26, 33, 32]
}

df = pd.DataFrame(data)
df['Total Sales'] = df.drop(columns='Name').sum(axis=1)

max_sales = df.drop(columns='Name').max(axis=1)
vikas_sales = df[df['Name'] == 'Vikas'].drop(columns='Name')
ajit_sales = df[df['Name'] == 'Ajit'][['Apr', 'May', 'Jun']]
selected_months = df[['Name', 'Apr', 'Aug', 'Dec']]

df['Average Sales'] = df.drop(columns=['Name', 'Total Sales']).mean(axis=1)
min_sales = df.drop(columns='Name').min(axis=1)
min_sales_per_month = df.drop(columns='Name').min(axis=0)
average_sales_value = df['Average Sales'].mean()
above_average_sales = df.loc[df['Total Sales'] > average_sales_value]
max_sales_value = df['Total Sales'].max()
max_sales_persons = df[df['Total Sales'] == max_sales_value]['Name']

print("1. Total Sales of Each Sales Person:")
print(df[['Name', 'Total Sales']])

print("\n2. Maximum Sales of Each Sales Person:")
print(max_sales)

print("\n3. Sales Data of Vikas for All Months:")
print(vikas_sales)

print("\n4. Sales Data of Ajit for the month of Apr, May, Jun:")
print(ajit_sales)

print("\n5. Sales Data for the month of Apr, Aug, and Dec for all Sales Persons:")
print(selected_months)

print("\n6. Average Sales of Each Sales Person:")
print(df[['Name', 'Average Sales']])

print("\n7. Minimum Sales of Each Sales Person:")
print(min_sales)

print("\n8. Minimum Sales for Each Month:")
print(min_sales_per_month)

print("\n9. Sales Greater Than the Average of Sales Data:")
print(above_average_sales[['Name', 'Total Sales']])

print("\n10. Sales Persons Who Have Achieved Maximum Sales in a Year:")
print(max_sales_persons)
