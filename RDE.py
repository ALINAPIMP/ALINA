from bs4 import BeautifulSoup
import requests
import pandas as pd
alldata=[]
for i in range(1,7):
    url=f"https://www.rde.lt/categories/lt/217/sort/5/filter/0_0_0_0/page/{i}/%C5%A0aldikliai.html"
    response=requests.get(url)
    # print(response.status_code)
    soup=BeautifulSoup(response.content,'html.parser')

    products=soup.find_all('li', class_='col col--xs-4 product js-product js-touch-hover')

    for product in products:
        title=product.find('h3',class_='product__title').text.strip()
        price=product.find('p', class_='price').text.strip().replace(' €','')
        category=product.select_one('div.product__info__part nav').text.strip()

        product_tags=product.find('ul',class_='product-tags')
        lizingas_tag='N/A'
        naujiena_tag='N/A'
        populiari_tag='N/A'
        # print(product_tags)
        if product_tags:
            for tag in product_tags.find_all('li'):
                if 'product-tags__s' in tag.get("class",[]):
                    lizingas_tag=tag.get("data-type-s",'N/A')
                elif 'product-tags__n' in tag.get("class",[]):
                    naujiena_tag=tag.get("data-type-n","N/A")
                elif 'product-tags__ts' in tag.get('class',[]):
                    populiari_tag=tag.get('data-type-ts','N/A')


        alldata.append({
            'Title':title,
            'Price':price,
            'Category':category,
            "Lizingas":lizingas_tag,
            "Populiariausia preke":populiari_tag,
            "Naujiena":naujiena_tag
        })

#print(alldata)

df=pd.DataFrame(alldata)
df.to_csv('saldikliai.csv', index=False)
#print(df)

# print(alldata)
df = pd.DataFrame(alldata) #DataFrame sukuria grazu lenteles vaizda
df.to_csv('saldikliai1.csv', index=False)
print(df)




