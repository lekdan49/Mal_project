import xml.etree.ElementTree as ET
import shutil
import os

tree = ET.parse('animelist_1552948095_-_5559128.xml')
root = tree.getroot()

for child in root.findall('anime'):
    anime_number = child.find('series_animedb_id').text
    f = open("anidbid.txt", "a")
    f.write("%r\n" % anime_number)
    f.close()
with open('anidbid.txt', 'r') as f, open('output.txt', 'w') as fo:
    for line in f:
        fo.write(line.replace('"', '').replace("'", ""))

shutil.move("output.txt", "Done_ani/output.txt")
os.remove("anidbid.txt")

