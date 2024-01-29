#name, bedroom, bathroom, living space, price

from bs4 import BeautifulSoup
import requests
import pandas as pd

products_data = []
for i in range(1, 14):
    target = f"https://spain-real.estate/property/balearic-islands/ibiza/page/{i}/#objects"
    response = requests.get(target)
    soup=BeautifulSoup(response.content,'html.parser')
    # print(soup.prettify())

    products = soup.find_all('li', {'data-object':True})

    for product in products:
        name = product.find('div', class_='title').text.strip()
        bedroom_text = product.find('span', class_='bedrooms')
        bathrooms_text = product.find('span', class_='bathrooms')
        living_space_text = product.find('span', class_='area')
        price = product.find('div', class_='price js-list-for-show').text.strip()
        first_currency=price.split('\n')[0].strip()
        first_currency = first_currency.replace('\xa0', '').replace('Sold out', '0').replace('€ ', '')

        if bedroom_text:
            bedroom = bedroom_text.text.strip().replace('Bedrooms:', '')
        else:
            bedroom = 'N/A'

        if bathrooms_text:
            bathrooms = bathrooms_text.text.strip().replace('Bathrooms:', '')
        else:
            bathrooms = 'N/A'

        if living_space_text:
            living_space_parts = living_space_text.text.strip().split(' ')
            living_space = living_space_parts[2] if len(living_space_parts) > 1 else 'N/A'
        else:
            living_space = 'N/A'

        products_data.append({
            'Name': name,
            'Bedroom': bedroom,
            'Bathrooms': bathrooms,
            'Living space': living_space,
            'Price': first_currency
        })

# print(products_data)
df = pd.DataFrame(products_data) #DataFrame sukuria grazu lenteles vaizda
df.to_csv('namai.csv', index=False)
print(df)