from requests import get
from bs4 import BeautifulSoup
import urllib.request
import webbrowser
import datetime

s = input("paste thread link: ")
r = get(s)
### r = get("https://boards.4channel.org/g/thread/69042897")
soup = BeautifulSoup(r.content, "html.parser")
for i in soup.find_all('a'):
    if i.attrs.get("class") != None:
        r = i.attrs.get("class")
        for n in r:
            if n == "fileThumb":
                """
                print(i)
                print("_____________________________")
                """
                m=i.attrs.get("href")
                url = "http:" + m
                print(m)
                #k = m.lstrip("//i.4cdn.org/g/b/")
                k = m.rsplit(".")
                filetype = k[3]
                td = str(datetime.datetime.today())
                td_final = td.replace(":","-")
                filename = td_final + "." + filetype
                s = ("C:/Users/Jackson/Pictures/4chanshit/" + filename)
                urllib.request.urlretrieve(url, s) 
#4chanshit
#Wallpapers
