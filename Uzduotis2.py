# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'}
# url='https://www.coinbase.com/explore'
# response = requests.get(url, headers=headers)
# # print(response.status_code)
#
# soup = BeautifulSoup(response.content, 'html.parser')
# crypto = []
# table = soup.find('table')
# if table:
#     rows = table.find_all('tr')
#     for row in rows:
#         cells = row.find_all('td') #table data
#         if len(cells) > 1:
#             name = cells[0].text.strip()[1:] #nuo 1 elemento - isvalo elem pries teksta
#             price = cells[1].text.strip().replace('€', '') #visuomet tekstas, tik paskui konvertuojam
#             change = cells[3].text.strip()[1:].replace('%', '')
#             market_cup = cells[4].text.strip().replace('€', '')
#             volume = cells[5].text.strip().replace('€', '')
#             supply = cells[6].text.strip()
#             crypto.append({
#                 'Name': name,
#                 'Price': price,
#                 'Change': change,
#                 'Market cap': market_cup,
#                 'Volume(24h)': volume,
#                 'Supply': supply
#             })
# # print(crypto)
# df = pd.DataFrame(crypto)
# df.to_csv('crypto.csv', index=False)
# print(df)


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('crypto.csv')

def adjust_prices(value):
    if 'B' in value:
        return float(value.replace('B',''))*1e9 #bilionai
    elif 'M' in value:
        return float(value.replace('M',''))*1e6 #milionai
    elif 'T' in value:
        return float(value.replace('T',''))*1e12
    else:
        return float(value)
df['Market cap'] = df['Market cap'].apply(adjust_prices)
highest_market_cap = df[df['Market cap'] == df['Market cap'].max()]
print(highest_market_cap)


top_cryptos = df.nlargest(5,'Market cap')
plt.figure(figsize = (12,6))
plt.bar(top_cryptos['Name'],top_cryptos['Market cap'])
plt.title('Top 5 crypto currencies by Market cap')
plt.xlabel('Crypto currency')
plt.ylabel('Market cap')
plt.grid(True)
plt.show()