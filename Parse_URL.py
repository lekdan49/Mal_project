import requests
from bs4 import BeautifulSoup
import re
import textwrap
import urllib
from urllib.request import urlopen
f = open('NEW_URLS.txt', 'r')
global title
for child in f:
    title = ''
    str(child)
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
    f = open("DATA.txt", "a")
    list_a = [title, decimal_val]
    print(list_a)
    # with f as the_file:
    #     the_file.write(list_a)


# r = requests.get('https://myanimelist.net/anime/6547')
# soup = BeautifulSoup(r.text, 'html.parser')
# score = soup.find_all('div', attrs={'class':'fl-l score'})
# new_data = score[0]
# str(new_data)
# print(new_data)
# decimal_val = re.findall(r"[-+]?\d*\.\d+|\d+", str(new_data))
# print(decimal_val)
