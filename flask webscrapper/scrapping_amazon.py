from autoscraper import AutoScraper
import pandas as pd

amazon_url="https://www.amazon.fr/s?k=headphones"

wanted_list=["https://m.media-amazon.com/images/I/51V0YBmQ4WL._AC_UL320_.jpg","JBL Tune 230 NC TWS – Écouteurs intra-auriculaires sans fil, Bluetooth, Son Pure Bass JBL, étanche et avec réduction du bruit, jusqu'à 40 heures d'autonomie, en noir","69,99€"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)
print(result)

scraper.get_result_similar(amazon_url,grouped=True)

scraper.set_rule_aliases({'rule_fp89':'Image','rule_hnmr':'Title','rule_6w63': 'Price'})
scraper.keep_rules(['rule_fp89','rule_hnmr','rule_6w63'])
scraper.save('amazon_search')
scraper.load('amazon_search')

results=scraper.get_result_similar('https://www.amazon.fr/s?k=headphones',group_by_alias=True)

#the dataset
search_data = tuple(zip(results['Title'],results['Price'],results['Image']))
print(search_data)

df = pd.DataFrame(search_data, columns = ['Title' , 'Price', 'ImageUrl'])
print(df)

list = []

for price in results["Price"]:
    value = float(price.replace(',', '.').replace('€', '').replace(' ', ''))
    print(value)
    list.append(value)

print(min(list))

i=0
indice=0
for price in results["Price"]:
    value = float(price.replace(',', '.').replace('€', '').replace(' ', ''))
    if(value== min(list)):
        indice=i
    else:
        i=i+1
print('*------------------------------------------resultat de recherche---------------------------------------------------*\n')
print("le meilleur choix des écouteurs dans amazone est ",results["Title"][indice]," avec un prix = ",results["Price"][indice])
print("image URL : \n",results["Image"][indice])
print('----------------------------------------------------------------------------------------------------------------------')




