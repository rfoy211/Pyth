import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file csv
df = pd.read_csv('ck/songs_normalize.csv')

# Tính tổng lượt nghe của mỗi ca sĩ
artist_year = df.groupby('artist')['year'].sum().reset_index()

# Sắp xếp lượt nghe giảm dần
artist_year = artist_year.sort_values(by='year', ascending=False)

# In ra ca sĩ có lượt nghe nhiều nhất
print(artist_year.head(1))


# Tính số lượng bài hát của mỗi thể loại
genre_counts = df['genre'].value_counts()

# Tạo biểu đồ tròn
plt.figure(figsize=(10, 8))
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%')
plt.title('Thể loại được nghe')
plt.show()

# Sắp xếp lượt nghe giảm dần
top_songs = df.sort_values(by='year', ascending=False)

# Lấy 10 bài hát đầu tiên
top_songs = top_songs.head(10)

# In ra top 10 bài hát có lượt nghe cao nhất
print(top_songs)

# Tính hệ số tương quan giữa lượt nghe và năng lượng
energy_corr = df['year'].corr(df['energy'])

# Tính hệ số tương quan giữa lượt nghe và bắt tai
danceability_corr = df['year'].corr(df['danceability'])

# In ra hệ số tương quan
print(f'Hệ số tương quan giữa lượt nghe và năng lượng: {energy_corr}')
print(f'Hệ số tương quan giữa lượt nghe và bắt tai: {danceability_corr}')


# Số liệu
labels = ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Classic']
sizes = [25, 20, 15, 10, 30]

# Tạo biểu đồ tròn
plt.figure(figsize=(8, 8))
sns.set_style('whitegrid')
sns.set_color_codes('pastel')
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Thể loại âm nhạc')
plt.show()