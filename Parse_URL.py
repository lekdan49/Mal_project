import requests
from bs4 import BeautifulSoup
import re
import textwrap
import time
from tqdm import tqdm

import urllib
from urllib.request import urlopen
f = open('NEW_URLS.txt', 'r')
num_lines = sum(1 for line in open('NEW_URLS.txt'))
print(num_lines)
global title
global var_num
var_num = 0
for child in f:
    title = ''
    str(child)
    var_num = var_num + 1
    print(var_num)
    r = requests.get(child)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find_all('span', attrs={'itemprop':'name'})
    score = soup.find_all('div', attrs={'class': 'fl-l score'})

    # <div class="fl-l score" data-title="score" data-user="704,869 users" title="indicates a weighted score. Please note that 'Not yet aired' titles are excluded.">
    #         8.28
    #       </div>

    title = title[3]
    title = str(title)

    title = re.sub('\<.*?\>', '', title)
    title = textwrap.dedent(title)

    # print(new_data)

    decimal_val = re.findall(r"[-+]?\d*\.\d+|\d+", str(score))

    decimal_val = str(decimal_val[-1])

    title = str(title)
    decimal_val = str(decimal_val)

    list_a = [title, decimal_val, child]

    list_a = [(el.strip()) for el in list_a]

    print(list_a)
    f = open("DATA.txt", "a")
    f.write("%s\n" % list_a)

# r = requests.get('https://myanimelist.net/anime/6547')
# soup = BeautifulSoup(r.text, 'html.parser')
# score = soup.find_all('div', attrs={'class':'fl-l score'})
# new_data = score[0]
# str(new_data)
# print(new_data)
# decimal_val = re.findall(r"[-+]?\d*\.\d+|\d+", str(new_data))
# print(decimal_val)
