# importing libraries
from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://www.amazon.de/b?ie=UTF8&node=17327952031&pf_rd_r=0FT01ZD4NM0ATZB18SQ0&pf_rd_p=919231e9-7c1a-4fb0-ab54-2fe548e8e8c1"

page = urllib.request.urlopen(url) # conntect to website

try:
    page = urllib.request.urlopen(url)
except:
    print("An error occured.")

soup = BeautifulSoup(page, 'html.parser')
 
 
contentlist = soup.find_all('div', class_='s-item-container')

for content in contentlist:
    product = content.find_all('div', class_='a-fixed-left-grid-col')
    for detiali in product:
        productTitle = detiali.find('h2', class_='s-access-title', text=True)
        productPrice = detiali.find('span', class_='s-price', text=True)
        productlink = detiali.find('a', class_='a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal')
        productImage = detiali.find('img', class_='s-access-image cfMarker')
        if productTitle is not None:
            title = productTitle.get_text()
            print(title)
        if productPrice is not None:
            price = productPrice.get_text()
            print(price)
        if productlink is not None:
            link = productlink['href']
            print(link)
        # if productImage is not None:
            # linkimg = productImage['src']
            # print(linkimg)