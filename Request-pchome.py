import requests
from bs4 import BeautifulSoup

url = 'https://24h.pchome.com.tw/search/?q=Viewsonic&scope=all'

response = requests.get(url)

soup=BeautifulSoup(response.text, 'html.parser')

title = soup.find('title').get_text()

print(title)