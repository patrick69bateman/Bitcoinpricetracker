import requests
from bs4 import BeautifulSoup

url = 'https://www.coingecko.com/en/coins/bitcoin'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

print("B I T C O I N")
price = soup.find('span', {'class':"tw-text-gray-900 dark:tw-text-white tw-text-3xl"})
print(price.text)
percent = soup.find('span', {'class':'live-percent-change tw-ml-2 tw-text-xl'})
print(percent.text)