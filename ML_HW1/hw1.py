import pandas as pd
from sys import path
print(path)

df = pd.read_csv("/Users/jasonjin/Desktop/Spring 2023/MATH5430/ML_HW1/bank-additional-full.csv", sep=';')
df = df.dropna() 

target = df["y"] #36548 no's and 4640 yes's


print(target.value_counts())
'''
We probably have to increase the number of no's for the column y 
to balance out the categorical variable counts
'''

print(df.shape)

# Eliminating all the "unknown" strings inside the columns
df = df[~df.job.str.contains("unknown")]
df = df[~df.marital.str.contains("unknown")]
df = df[~df.education.str.contains("unknown")]
df = df[~df.default.str.contains("unknown")]
df = df[~df.housing.str.contains("unknown")]
df = df[~df.loan.str.contains("unknown")]
df = df[~df.contact.str.contains("unknown")]
df = df[~df.month.str.contains("unknown")]
df = df[~df.day_of_week.str.contains("unknown")]
df = df[~df.poutcome.str.contains("unknown")]

print(df.shape) #dataframe shape shrunk to 30488 rows

ohe_features = [
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "day_of_week",
    "poutcome"
] #One_hot_encoding

num_features = [
    "age",
    "duration",
    "campaign",
    "pdays",
    "previous"
]
float_features = [
    "emp.var.rate",
    "cons.price.idx",
    "cons.conf.idx",
    "euribor3m",
    "nr.employed"
]

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer
# from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

mixed_df = df[ohe_features+num_features+float_features]

encoder = OneHotEncoder()
target = encoder.fit_transform(target)

X_dev, X_test, y_dev, y_test = train_test_split(mixed_df, target, test_size=0.2, random_state=42)

preprocess = make_column_transformer(
    (LabelEncoder(), ohe_features),
    (StandardScaler(), num_features),
    (StandardScaler(), float_features)
)

model = LogisticRegression()
model = model.fit(X_dev, y_dev)

model.predict()


