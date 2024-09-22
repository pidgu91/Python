import requests
import random
from bs4 import BeautifulSoup
import datetime

url = 'https://pixelford.com/blog/'


response = requests.get(url, headers={'User-Agent': '31957582'})
html = response.content
soup = BeautifulSoup(html, 'html.parser')
blogs = soup.find_all('article', class_='type-post')

# results = list(map(lambda x: x.get_text(), a_tags))
# print(results)
#
for blog in blogs:
    title = blog.find('a', class_='entry-title-link').get_text()
    blog_datetime_string = blog.find('time', class_="entry-time").get('datetime')
    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_string)
    pretty_date = blog_datetime.strftime("%b %m/%Y")
    print(f"{pretty_date} - {title}")