import pandas as pd
import matplotlib.pyplot as plt


#
# df1=pd.DataFrame({
#     'ID':[1, 2, 3, 4, 5],
#     'Vardas': ['Jonas', 'Ona', 'Antanas', 'Petras', 'Mykolas'],
#     'Anzius': [22, 38, 14, 52, 18]
# })
#
# df2=pd.DataFrame({
#     'ID':[3, 4, 5, 6, 7],
#     'Vardas': ['Antanas', 'Petras', 'Mykolas', 'Tadas', 'Urte'],
#     'Atlyginimas': [1500, 2100, 100, 3200, 1980]
# })
#
# df3=df1.merge(df2,on='ID', how='outer', indicator=True)
# print(df3)

File_name = 'os_worldwide.csv'
df = pd.read_csv(File_name)
# print(df.head())

df['Date'] = pd.to_datetime(df['Date'])
#
# plt.figure(figsize=(12,8))
# plt.plot(df['Date'], df['Windows'], label='Windows', marker='o')
# plt.plot(df['Date'], df['Android'], label='Android', marker='o')
# plt.plot(df['Date'], df['iOS'], label='iOS', marker='o')
# plt.plot(df['Date'], df['OS X'], label='OS X', marker='o')
# plt.plot(df['Date'], df['Linux'], label='Linux', marker='o')
# plt.title('Operating system usage trends over time')
# plt.xlabel('Date')
# plt.ylabel('Usage percentage')
# plt.legend()
# plt.grid(True)
# plt.show()


# os_change = df.iloc[-1, 1:] - df.iloc[0,1:] # pasiekti paskutine eilute
# os_change_sorted = os_change.sort_values()
# plt.figure(figsize=(12, 6))
# os_change_sorted.plot(kind='bar', color='skyblue')
# plt.title('Rise and decline of operating system usage (2009 to latest')
# plt.xlabel('Operating system')
# plt.ylabel('Change in usage percentage')
# plt.grid(True)
# plt.show()

# os_change = df.iloc[-1, 1:] - df.iloc[0,1:] # pasiekti paskutine eilute
# os_change_sorted = os_change.sort_values()
#
# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month
#
#yearly_data = df.groupby('Year').mean()
#monthly_data = df.groupby(['Year','Month']).mean().reset_index()
#
# plt.figure(figsize=(12,8))
# plt.plot(yearly_data.index,yearly_data['Windows'], label='Windows', marker='o')
# plt.plot(yearly_data.index,yearly_data['Android'], label='Android', marker='o')
# plt.plot(yearly_data.index,yearly_data['iOS'], label='iOS', marker='o')
# plt.plot(yearly_data.index,yearly_data['OS X'], label='OS X', marker='o')
# plt.plot(yearly_data.index,yearly_data['Linux'], label='Linux', marker='o')
# plt.title('Yearly operating system usage trends')
# plt.xlabel('Year')
# plt.ylabel('AVG usage percentage')
# plt.legend()
# plt.grid(True)
# plt.show()

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
yearly_data = df.groupby('Year').mean()
monthly_data = df.groupby(['Year','Month']).mean().reset_index()
most_recent_year = df['Year'].max()
monthly_trend_data = monthly_data[monthly_data['Year'] == most_recent_year]

plt.figure(figsize=(12,8))
plt.plot(monthly_trend_data['Month'], monthly_trend_data['Windows'], label='Windows', marker='o')
plt.plot(monthly_trend_data['Month'], monthly_trend_data['Android'], label='Android', marker='o')
plt.plot(monthly_trend_data['Month'], monthly_trend_data['iOS'], label='iOS', marker='o')
plt.plot(monthly_trend_data['Month'], monthly_trend_data['OS X'], label='OS X', marker='o')
plt.plot(monthly_trend_data['Month'], monthly_trend_data['Linux'], label='Linux', marker='o')
plt.title(f'Monthly operating systems usage trend in {most_recent_year }')
plt.xlabel('Month')
plt.ylabel('Usage percentage')
plt.legend()
plt.grid(True)
plt.show()