# importuojamos bibliotekos

from bs4 import BeautifulSoup
import requests
import pandas as pd

products_data = []
for i in range(1, 4):
    target = f"https://varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/?p={i}"
    response = requests.get(target)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', class_='GRID_ITEM')

    for product in products:
        title = product.find('div', class_='product-title').text.strip()
        price = product.find('span', {'class': 'price-value'}).text.strip().replace('\xa0', '').replace('\n', '')
        stock_quantity = product.find('b').text.strip().replace(' vnt.', '')

        products_data.append({
            'Title': title,
            'Price': price,
            'Quantity': stock_quantity
        })

df = pd.DataFrame(products_data)
df.to_csv('products.csv', index=False)
print(df)

