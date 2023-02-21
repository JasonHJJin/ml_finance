# (b)
# Question 1
# Simply execute this line to start using Python.
print("Hello world!")

# Question 2
# Define variable x, y, z to be of int, float, string type respectively.

x = 10
y = 10.0
z = "string"

print(type(x))
print(type(y))
print(type(z))

# Define variable ls, tp, dic to be of list, tuple and dictionary type respectively.

ls = [1, 2, 3]
tp = (1, 2)
dic = {1: 2}

print(type(ls))
print(type(tp))
print(type(dic))

# Question 3
# Write a function that calculates x^2 + y^2, and print out results of x=3 and y=4.
def firstfunc(x, y):
    return x^2 + y^2

print(firstfunc(3, 4))

# Question 4: Basic Pandas
# 1. import pandas and print the version of pandas
import pandas as pd
print(pd.__version__)

# 2. create a pandas dataframe from provided dictionary and index. 

data = {
  "name": ["John", "Mary", "Bob", "Alice", "Lisa"],
  "calories": [420, 380, 390, 500, 150],
  "duration": [50, 40, 45, 48, 20],
  "sportstype": ["cardio", "scrupt", "cardio", "scrupt", "scrupt"]
}
index = ["day1", "day2", "day3", "day4","day5"]

df = pd.DataFrame(data, index=index)
print(df)

# 3. use the named index in the 'loc' attribute to return row of index "day2" and print out.
print(df.loc['day2'])

# 4. use one line to group the dataframe by "sportstype" and calculate the maximum of "calories" and the average of "duration".
df1 = df.groupby(['sportstype'])
print(df1['calories'].max())
print(df1['duration'].mean())

# 5. merge the first dataframe with below dataframe on "name" and use right-join method. Print out the merged dataframe.
df2 = pd.DataFrame({
    "name": ["Aaron", "John", "Mary", "Tim", "Bob", "Alice", "Tom", "Lisa"],
    "zipcode": [10023, 10012, 10046, "{:05d}".format(3244), "{:05d}".format(7302), "{:05d}".format(3312), 21901, 10124]})

merged_df = df.merge(df2, how="right", on="name")
print(merged_df)

arr = [10, 20, 30, 40]
df3 = pd.DataFrame(arr)
print(df3)