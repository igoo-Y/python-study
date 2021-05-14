import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from wordcloud import WordCloud

from PIL import Image
import numpy as np

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.melon.com/chart/month/index.htm')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

text = ""

musics = soup.select('#lst50')

for music in musics :
    title = music.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    rank = music.select_one('td:nth-child(2) > div > span.rank').text
    singer = music.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    text+=singer

    print(rank,title,singer)

apple_mask=np.array(Image.open('/Users/yang-ingyu/Desktop/pythonstudy/spurs.jpeg'))

font_path = '/Volumes/Machintosh HD/System/Library/Fonts/AppleSDGothicNeo.ttc'

wc = WordCloud(font_path = font_path, background_color="white", width=600, height=400, mask=apple_mask)
wc.generate(text)

wc.to_file("melon_wordcloud.png")