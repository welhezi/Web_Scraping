
from autoscraper import AutoScraper
import pandas as pd


flying_url="https://flyingtiger.com/collections/headphones"

wanted_list=["Wireless headphones","€20","Wireless over-ear headphones with microphone. Audio cable and USB charging cable included. Available in more designs. Not sold in Poland.","//cdn.shopify.com/s/files/1/0526/7144/7238/products/wireless-headphones-media-flying-tiger-copenhagen-356404.jpg?v=1665587239&width=450"]

scraper=AutoScraper()
result=scraper.build(flying_url,wanted_list)
print(result)


scraper.get_result_similar(flying_url,grouped=True)

scraper.set_rule_aliases({'rule_xx2x':'Title','rule_ju6w': 'Price','rule_ga3d': 'Description','rule_6ys6':'Image'})
scraper.keep_rules(['rule_xx2x','rule_ju6w','rule_ga3d','rule_6ys6'])
scraper.save('flying_search')
scraper.load('flying_search')


results=scraper.get_result_similar('https://flyingtiger.com/collections/headphones',group_by_alias=True)

#the dataset
search_data = tuple(zip(results['Title'],results['Price'],results['Description'],results['Image']))
search_data

df = pd.DataFrame(search_data, columns = ['Title' , 'Price','Description','ImageUrl'])
print(df)

list = []

for price in results["Price"]:
    value = float(price.replace(',', '.').replace('€', ''))
    print(value)
    list.append(value)


i=0
indice=0
for price in results["Price"]:
    value = float(price.replace(',', '.').replace('€', ''))
    if(value== min(list)):
        indice=i
    else:
        i=i+1

print('*------------------------------------------resultat de recherche---------------------------------------------------*\n')
print("le meilleur choix des écouteurs dans 'flying tiger' est ",results["Title"][indice]," avec un prix = ",results["Price"][indice])
print(" ---------------- description : ")
print(results["Description"][indice])
print(" ---------------- imageURL : ")
print(results["Image"][indice])
print('----------------------------------------------------------------------------------------------------------------------')




