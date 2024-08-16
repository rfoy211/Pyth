import pandas as pd

df = pd.read_excel("C:/Users/Windows 10 Home/Downloads/Python2/buoi10/pokemon_data.xlsx")

# data = df.Name
# data = df["HP"]
# print(data.head(10))
# print(type(data))

# data = df[4:30:5]
# print(data)
# print(type(data))

# data = df[["Name", "HP"]]
# print(data.head(3))
# print(type(data))

# data = df.loc[:,"Name"]
# print(data.head(3))
# print(type(data))

# data = df.loc[10]
# print(data)
# print(type(data))

# data = df.loc[10, "HP"]
# print(data)
# print(type(data))

# data = df.loc[:, "HP":"Speed"]
# print(data.head(2))

# data = df.loc[:, ["HP", "Speed"]]
# print(data.head(2))

# data = df.loc[1:3]
# print(data.loc[:, ["HP", "Attack"]])

# print(df["HP"].describe())
# print("sum", df.HP.sum())
# print("value counts", df.Legendary.value_counts())

filtered_df = df[df.HP > 150]
print(filtered_df.Name)

filtered_df = df[df.Name == "Chansey"]
print(filtered_df)