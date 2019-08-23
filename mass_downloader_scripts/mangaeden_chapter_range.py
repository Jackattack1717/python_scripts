from requests import get
from bs4 import BeautifulSoup
from fpdf import FPDF
import urllib.request
import webbrowser
import datetime

manga_name = input("what manga do you want?: ")
manga_starting_ch = input("what chapter do you want to start with?: ")
manga_ending_ch = input("what chapter do you want to end with?: ")

manga_starting_ch = int(manga_starting_ch)
manga_ending_ch = int(manga_ending_ch)

pdf = FPDF('P', 'mm', 'A3')
pdf.set_auto_page_break(0)

if(manga_starting_ch == manga_ending_ch):
    manga_ending_ch += 1

for chapter in range(manga_starting_ch, manga_ending_ch + 1):
    print("Chapter: " + str(chapter))
    link = "https://www.mangaeden.com/en/en-manga/" + manga_name + "/" + str(chapter) + "/1"
    r = get(link)
    soup = BeautifulSoup(r.content, "html.parser")
    for i in soup.find_all("option"):
        if i.attrs.get("data-page") != None:
            pages_in_ch = i.attrs.get("data-page")
    print("pages:" + pages_in_ch)
    for page in range(1, int(pages_in_ch) + 1):
        link = "https://www.mangaeden.com/en/en-manga/" + manga_name + "/" + str(chapter) +"/" + str(page)
        r = get(link)
        soup = BeautifulSoup(r.content, "html.parser")
        for i in soup.find_all('img'):
            if i.attrs.get("id") == "mainImg":
                # print(i.attrs.get("src"))
                pagefilename = "Ch" + str(chapter) + "pg" + str(page) +".jpg"
                s = ("C:/Users/Jackson/Documents/Manga/OnePunchMan/" + pagefilename)
                urllib.request.urlretrieve("https:" + i.attrs.get("src"), s)
                pdf.add_page()
                pdf.image(s, w = 280)

pdf.output('C:/Users/Jackson/Documents/Manga/OnePunchMan/'+ manga_name + "ch" + str(manga_starting_ch)+ "-" + str(manga_ending_ch) + ".pdf", 'F')
