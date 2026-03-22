import pandas as pd;

df= pd.DataFrame({
    "Name": ["Ravi", "Kiran", "Kumar"],
    "Age": [23, 24, 25],
    "Location": ["Bangalore", "Hyderabad", "Chennai"]
})

# print(df["Name"])
# print(df[df["Age"]>24])
# print(df)

#print(df["Name"][0])
#print(df["Age"]+10)
print(df.loc[0] )       
print(df.iloc[0] )
# print((df["Age"].mean()))
# print(df["Age"].max())
# print(df["Age"].min())
# print(df["Age"].std())
# print(df["Age"].var())
# print(df["Age"].describe())
# print(df["Age"].value_counts())
# print(df["Age"].sum())