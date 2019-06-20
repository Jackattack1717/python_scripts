from requests import get
from bs4 import BeautifulSoup
import urllib.request
import webbrowser
import datetime
import json
import time

s = input("paste link: ")

print(s)
r = get(s)
print(r)
soup = BeautifulSoup(r.content, "html.parser")
print(soup.prettify())
"""
for i in soup.find_all("video-mirrors"):
    n = i.attrs.get(":mirrors")
    f = json.loads(n)
    h=f[0]
    print(h["embed_id"])
    #print(i)
        m=i.attrs.get("href")
        url = m
        print(m)
        filename = "Cowboy-Bebop-episode"+str(w)+".mp4"
        s = ("C:/Users/Jackson/Videos/Cowboy_Bebop/" + filename)
        urllib.request.urlretrieve(url, s)
    print()
    print("-" * 20)
    time.sleep(3)
    w = w + 1
"""
