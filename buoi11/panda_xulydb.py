import pandas as pd
# tạo data
students_df = pd.DataFrame({
    "Name": ['cu cu', 'ha ha', 'he he', 'hi hi', 'há há'],
    "Point": [0,0,2.6,5.9,9.0],
    "Qualify": [True, False, False, False, True]
})
# thay đổi giá trị trong dataframe
# thay the tung o
# students_df.loc[1, "Point"] = 6.8
# print(students_df)
# students_df.iloc[0, 1] = 5.8
# print(students_df)

# at (label)
# value = students_df.at[3, "Quanlify"]
# print(value)
#iat(index)
# students_df.iat[4, 0] = "lo lo"
# value = students_df.iat[4,0] 
# print(value)

# replace
# inplace
# students_df.replace([True, False], ['yes', 'no'], inplace=True)
# print(students_df)

# thay đổi giá trị nội dung
# thêm cột
# students_df["Gender"] pd.Series(1, 0, 1, 0, 1)
# print(students_df)
# xóa cột
# students_df.drop(cloumns=["Name", "Quanlify"], inplace=True)
# print(students_df)
# thêm dòng
# df = students_df.append({'Name': "Tran Van F", "Point": 10.0, "Qualify": False}, ignore_index=True)
# print(df)
# xóa dòng
students_df.drop(index=[1, 3], inplace=True)
print(students_df)