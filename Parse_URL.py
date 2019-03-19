import requests
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import urlopen


# r = requests.get('https://myanimelist.net/anime/6547')
# soup = BeautifulSoup(r.text, 'html.parser')
# score = soup.find_all('div', attrs={'class':'fl-l score'})
# new_data = score[0]
# str(new_data)
# print(new_data)
# decimal_val = re.findall(r"[-+]?\d*\.\d+|\d+", str(new_data))
# print(decimal_val)
