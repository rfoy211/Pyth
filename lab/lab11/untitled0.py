# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1elXy1m_niKiEUQxOOODYSei2H21hxGKm
"""

import pandas as pd

from google.colab import drive

border_file = "/content/borders.xls"
coastline_file = "/content/coastlines.xls"
province_file = "/content/provinces (1).xls"

province_df = pd.read_excel(province_file)
print(province_df.head(3))

coastline_df = pd.read_excel(coastline_file)
print(coastline_df.head(3))

borders_df = pd.read_excel(border_file)
print(borders_df.head(3))

print("Number of provinces & cities with coastline:",len(coastline_df))

"""Bài 2"""

# gộp  dữ liệu vòa bảng province
coastline=[]
# chạy vogng lập để lấy dữ liệu cho list coatsline
for name in province_df['Name']:
  matching_row = coastline_df['coastline_df'['Name']== Name]
  if not matching_row.empty:
    # số dữ liệu và duong bo bien
    coastline.append(matching_row['Coatline'].ist[o])
    else:
      coastline.append(0)

# them cot Coastline vao bang province
province_df['Coastline'] = coastlines

# in ra bang province
print(province_df)

# update du lieu cho file province
province_df.to_excel("provinces_updated.xlsx", index=False)

"""bai3

"""

# tao bang border_updated rieng
border_updated_df = pd.DataFrame(columns=['Name', 'BorderWith', 'BorderCount'])

# chay file de doc data trong tung sheet
border_list = (('CHN', 'China'), ('LAO', 'Laos'), ('KHM', 'Combodia'))

for coutry in border_list:
  inp_df = pd.read_excel(border_file, sheet_name=coutry[0])
# chay vong lap de ghi vao file province
  for name in inp_df['Tên tỉnh']:
    matching_row = border_updated_df[province_df['Name'] == name]
    if(not matching_row.empty):
      border_updated_df.at[matching_row.index[0], 'BorderWith'] += ", " + coutry[1]
      border_updated_df.at[matching_row.index[0], 'BorderCount'] += 1
    else:
      border_updated_df = pd.concat([border_updated_df, pd.DataFrame({'Name': [name], 'BorderWith': [coutry[1] + ','], 'BorderCount': [1]})], ignore_index=True)