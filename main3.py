import pandas as pd
import matplotlib.pyplot as plt

file_path = "C:/Users/Vytautas/PycharmProjects/pythonKursas/products.csv"

products_df = pd.read_csv(file_path)
#print(products_df.head())

products_df['Price'] = products_df['Price'].replace('[€,]', '', regex=True).astype(float)
products_df['Quantity'] = products_df['Quantity'].replace('[+,]', '', regex=True).astype(int)

#print(products_df.head(10))
mean_price = products_df['Price'].mean()
# print(f'mean of the price is: {mean_price: .2f}€')
median_price = products_df['Price'].median()
#print('Median price:', median_price)
price_range = products_df['Price'].max() - products_df['Price'].min()
max_price = products_df['Price'].max()
min_price = products_df['Price'].min()
print(f'Price range: {min_price}€ - {max_price}€')
#print(f'The price range is: {price_range}')

filtered_products = products_df[products_df['Price'] <1000]
sorted_products = filtered_products.sort_values(by='Price', ascending=False).reset_index(drop=True)
# print(f'Sprted products: {sorted_products}')

# plt.figure(figsize=(12,6))
# plt.bar(sorted_products['Title'], sorted_products['Price'], color='teal')
# plt.xlabel('Product Title')
# plt.ylabel('Price(€)')
# plt.title('Top 10 most expensive products')
# plt.xticks(rotation=90)
# plt.show()

# plt.figure(figsize=(10, 6))
# plt.hist(products_df['Price'], bins=20, color="darksalmon")
# plt.title("Histogram of product prices")
# plt.xlabel('Price')
# plt.ylabel('Number of products')
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(10,6))
# plt.scatter(products_df['Price'], products_df['Quantity'], color="peru")
# plt.title('Scatter plot of price vs quantity')
# plt.xlabel('Price')
# plt.ylabel('Quantity')
# plt.grid(True)
# plt.show()

# import random
#
# students = ['Agne','Danute','Edita','Inga','Orinta','Ala']
#
# if len(students) % 2 != 0:
#     message = "The number of students is not even"
# else:
#     random.shuffle(students)
#
#     pairs = [(students[i], students[i+1])for i in range(0, len(students), 2)]
#     message = pairs
#
# print(message)


