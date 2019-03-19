import requests
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import urlopen
f = open('NEW_URLS.txt', 'r')

for child in f:
    str(child)
    r = requests.get(child)
    soup = BeautifulSoup(r.text, 'html.parser')
    score = soup.find_all('div', attrs={'class': 'fl-l score'})
    str(score)
    # print(new_data)
    decimal_val = re.findall(r"[-+]?\d*\.\d+|\d+", str(score))
    


# r = requests.get('https://myanimelist.net/anime/6547')
# soup = BeautifulSoup(r.text, 'html.parser')
# score = soup.find_all('div', attrs={'class':'fl-l score'})
# new_data = score[0]
# str(new_data)
# print(new_data)
# decimal_val = re.findall(r"[-+]?\d*\.\d+|\d+", str(new_data))
# print(decimal_val)
