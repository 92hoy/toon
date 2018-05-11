import requests
from bs4 import BeautifulSoup
import urllib

bo_table = '2963'
wr_id = '2'
url = 'http://minitoon.net/bbs/board.php?bo_table='+ bo_table + '&wr_id=' + wr_id

img_url = []

r = requests.get(url)
html = r.text

soup = BeautifulSoup(html, "lxml")

links = soup.find_all("img", { "border" : "0" })

for link in links:
    if link['src'].find("comic.minitoon.net") != -1:
        img_url.append(link['src'])



lock = 0
for url in img_url:
    print(url)
    img_file = urllib.urlopen(url)

    f = open("/Volumes/HDD/jhytest/"+ str(lock) +".jpg", 'wb')
    f.write(img_file.read())

    lock += 1

f.close()