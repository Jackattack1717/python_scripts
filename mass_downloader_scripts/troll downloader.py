from requests import get
from bs4 import BeautifulSoup
import urllib.request
import webbrowser
import datetime

s = input("paste link: ")
r = get(s)
### r = get("https://boards.4channel.org/g/thread/69042897")
soup = BeautifulSoup(r.content, "html.parser")
for i in soup.find_all('img'):
    #print(i)
    print(i.attrs.get("src"))
    for n in r:
        print("_____________________________")
        m=i.attrs.get("src")
        url = "http:" + m
        print(m)
        #k = m.lstrip("//i.4cdn.org/g/b/")
        #k = m.rsplit(".")
        #filetype = k[3]
        td = str(datetime.datetime.today())
        td_final = td.replace(":","-")
        filename = td_final
        s = ("C:/Users/Jackson/Pictures/4chanshit/" + filename)
        urllib.request.urlretrieve(m, s)  
