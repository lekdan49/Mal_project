from requests.compat import urljoin
import os
f = open('Done_ani/output.txt', 'r')

for child in f:
    url_joining = 'https://myanimelist.net/anime/'
    new_var = str(child)
    url_new = urljoin
    final_url = url_new(url_joining, new_var)
    print(final_url)
    f = open("URLS.txt", "a")

    f.write("%r\n" %final_url)

    f.close()
    with open('URLS.txt', 'r') as f, open('Cleaned_URLS.txt', 'w') as fo:
        for line in f:
            fo.write(line.replace('"', '').replace("'", ""))

os.remove('URLS.txt')

# https://myanimelist.net/anime/37033
# //*[@id="content"]/table/tbody/tr/td[2]/div[1]/table/tbody/tr[1]/td/div[1]/div[1]/div[1]/div[1]/div[1]/text()




with open('Cleaned_URLS.txt', 'r') as infile, open('NEW_URLS.txt', 'w') as outfile:
    temp = infile.read().replace("\\n", "")
    outfile.write(temp)
os.remove('Cleaned_URLS.txt')