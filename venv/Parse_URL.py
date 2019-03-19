import requests
from bs4 import BeautifulSoup
r = requests.get('https://myanimelist.net/anime/6547')
soup = BeautifulSoup(r.text, 'html.parser')
score = soup.find_all('div', attrs={'class':'fl-l score'})
new_data = score[0]
print(new_data)
