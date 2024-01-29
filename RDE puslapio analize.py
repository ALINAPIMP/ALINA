import pandas as pd
import matplotlib.pyplot as plt

file='saldikliai.csv'
df=pd.read_csv(file)

df['Ar populiari']=df['Populiariausia preke'].apply(lambda x:'Taip' if pd.notna(x) and x.strip()!='N/A' else 'Ne')
# print(df['Ar populiari'])
#
# # df['Price'].plot(kind='hist', bins=20)
# # plt.xlabel('Kaina')
# # plt.title('Kainu pasiskirstymas')
# # # plt.show()
#
# data_to_plot=df['Price'].head(10)
# plt.figure(figsize=(10,6))
# bars=plt.bar(data_to_plot.index,data_to_plot.values)
# for bar in bars:
#     yval=bar.get_height()
#     plt.text(bar.get_x()+bar.get_width()/2.0,yval,round(yval,2),va="bottom",ha="center")
# plt.title('Produktu kainos')
# plt.xlabel('Produktu indeksai')
# plt.ylabel('Kaina')
# plt.show()


sorted_df = df.sort_values(by='Price', ascending=False)
top_10_expensive=sorted_df.head(10)
print(top_10_expensive)