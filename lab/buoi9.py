from data import col_list, province_list
import pandas as pd

data = {"a": -1.3, "b": 11.7, "d": 2.0, "f": 10, "g": 5}
ser = pd.Series(data, index=["a", "c", "d", "e", "f"])
print(ser[-3::])

#dataFrames
# data = pd.DataFrame(, index=col_list)
# print(data.head(10))

data = pd.DataFrame(
    data=[
        ("abc", "abc", "abc", 7929.5, 858.1),
        ("abc", "abc", "abc", 6700.3, 530.9),
        ("abc", "abc", "abc", 4860.0, 314.4),
    ],
    columns=col_list
)
print(data)

data.to_excel(excel_writer="buoi9/province.xlx", index=False)