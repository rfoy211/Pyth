import pandas as pd

# df = pd.read_excel("C:/Users/Windows 10 Home/Downloads/Python2/lab/provinces.xls")
# print(df.head(2))

# print(df.loc['Name'])
# for i in df.loc[:, "Name"]
#     print(i)

# rs = "List of provinces and cities: "+" , ".join[i for i in df.loc[:, "Name"]]
# print(rs)
#lambda
# def abc1 ():
#     return 1

# abc = lambda a, b: a +b

# cau 2 
# rs = "List of cities: " + ", ".join([i for i in df.loc[:, "Name"] if "Thanh pho" in i])
# print(rs)


# cites_df1 = df.loc[df["Division"] == "Thanh pho Trung uong", ["Name", "Region"]]
# print(cites_df1)

# cites_df = df.loc[df["Division"] == "Thanh pho Trung uong"]
# print(cites_df.loc[:, ["Name", "Region"]])

# cau 3
# regions_count = df["Region"].value_counts()
# print(regions_count)

# cau 4
# max_pop = df['Population'].max()
# min_pop = df['Population'].min()

# max_pop_province = df[df['Population'] == max_pop].iloc[0, :]
# min_pop_province = df[df['Population'] == min_pop].iloc[0, :]

# print(max_pop_province['Name'], str(int(max_pop_province["Population"]*1000)))
# print(min_pop_province['Name'], str(int(min_pop_province["Population"]*1000)))

# cau 5
regions_count = df["Region"].value_counts()

area_list = []
for r in regions_count.index:
    area_list.append(df[df["Region"] == r]["Area"].sum())
total_area = df["Area"].sum()
area_proportion_list = [area / total_area * 100 for area in area_list]

# create dataframe
area_df = pd.DataFrame(
    {
        "Region": regions_count.index,
        "Total Area": area_list,
        "Area Proportion": area_proportion_list,
    }
)

print(area_df)
