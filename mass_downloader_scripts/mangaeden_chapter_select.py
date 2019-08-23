#from requests import get
from bs4 import BeautifulSoup
from fpdf import FPDF
import urllib.request
import webbrowser
import datetime
import time
import requests

manga_name = input("what manga do you want?: ")


#pdf = FPDF('P', 'mm', 'A3')
#pdf.set_auto_page_break(0)


link = "https://www.mangaeden.com/en/en-manga/" + manga_name + "/1/1"
r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
chapters = []


for i in soup.find_all("select"):
    if(i.attrs.get("id") == "combobox"):
        for n in i.contents:
            #print(n.attrs.get("value"))
            chapters.insert(0,n.attrs.get("value"))

print("Available Chapters:" + str(chapters))

selected_chapters = []
while True:
    selected_chapter = input("What chapters do you want?: ")
    if selected_chapter == "":
        break
    selected_chapters.append(selected_chapter)

for chapter in selected_chapters:
    pdf = FPDF('P', 'mm', 'A3')
    pdf.set_auto_page_break(0)
    print("Chapter: " + str(chapter))
    link = "https://www.mangaeden.com/en/en-manga/" + manga_name + "/" + str(chapter) + "/1"
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    pages = []
    for i in soup.find_all("option"):
        if i.attrs.get("data-page") != None:
            pages.append(i.attrs.get("data-page"))
            pages_in_ch = i.attrs.get("data-page")
    print("pages: " + pages_in_ch)
    for page in pages:
        link = "https://www.mangaeden.com/en/en-manga/" + manga_name + "/" + str(chapter) +"/" + str(page)
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        for i in soup.find_all('img'):
            if i.attrs.get("id") == "mainImg":
                # print(i.attrs.get("src"))
                m = i.attrs.get("src")
                k = m.rsplit(".")
                filetype = k[len(k)-1]
                pagefilename = "Ch" + str(chapter) + "pg" + str(page) + "."  + filetype
                pageurl = "https:" + m
                s = ("C:/Users/Jackson/Documents/Manga/temp/" + pagefilename)
                response = requests.get(pageurl)
                urllib.request.urlretrieve(pageurl, s)
                pdf.add_page()
                pdf.image(name = s, x = 38, y = 0, w = 220, h = 0, link = '')
    pdf.output('C:/Users/Jackson/Documents/Manga/'+ manga_name + "_chapter_" + str(chapter)+ ".pdf", 'F')
#pdf.output('C:/Users/Jackson/Documents/Manga/'+ manga_name + "_complete.pdf", 'F')

