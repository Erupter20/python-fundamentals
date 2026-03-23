# # 6. Basic Operations on DataFrames
# # •Calculate the average age of all the people in the DataFrame.
# # •Add 1000 to each salary and print the updated DataFrame.


# import pandas as pd

# data = {'Name' : ['Alice' , 'Bob', 'Charlie'], 'Age' : [25, 30, 35], 'Department' : ['HR', 'IT', 'Finance']}
# df = pd.DataFrame(data)
# df['Salary'] = [50000,60000,55000]

# # calculating average

# df = pd.DataFrame(data)

# avg_age = df['Age'].mean()
# print(avg_age)
# # add 1000 to each salary

# df['increasedSalary'] = df['Salary'] +1000
# print(df)


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Department': ['HR', 'IT', 'Finance']
}

df = pd.DataFrame(data)
df['Salary'] = [50000, 60000, 55000]

# average age
avg_age = df['Age'].mean()
print(avg_age)

# add 1000 to salary
df['Salary'] = df['Salary'] + 1000

print(df)