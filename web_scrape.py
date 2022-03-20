"""
Scraper for graphic cards on Newegg
Arrange by price
"""


from cgitb import text
from bs4 import BeautifulSoup
import requests


#ask user what they're searching for - e.g 'rtx 3060', 'rtx 3090' etc...
#add that string into the url

newegg_url = 'https://www.newegg.com/'
searching_for = input("What are you looking for?: ")
searching_for = searching_for.replace(' ', '+')
graphics_card_url = '&N=100007709&isdeptsrh=1'

new_link = newegg_url + '/p/pl?d=' + searching_for + graphics_card_url
print(new_link)

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}

page = requests.get(new_link, headers=headers)

soup = BeautifulSoup(page.content, 'lxml')

for item in soup.find_all(class_='item-info'):
#display product name
    product_name = soup.find('a', class_="item-title").text
    print(product_name)

# #display price
    price = soup.find('li', class_="price-current").text
    print(price)

# #checks to see if the item is in stock
    stock_availability = soup.find("div", class_="item-button-area").text
    if stock_availability == 'View Details':
        print("Unavailable")
    else:
        print("Available")
    print()









