import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from wordcloud import WordCloud

from PIL import Image
import numpy as np

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.tottenhamhotspur.com/teams/men/players/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

text = ""

players = soup.select('#react_YFzEXth7UC2oZ7lkLILHg > div > div:nth-child(1) > a')

for player in players :
    number = player.select_one('div.PlayersPlayer__info > div.PlayersPlayer__number').text
    name = player.select_one('div.PlayersPlayer__info > div.PlayersPlayer__name').text

    text+=number

    print(number,name)

logo_mask = np.array(Image.open('/Users/yang-ingyu/Desktop/pythonstudy/apple.png'))

font_path = '/Volumes/Machintosh HD/System/Library/Fonts/Helvetica.ttc'

wc = WordCloud(font_path=font_path, background_color = 'white', height = 800, mask=logo_mask)
wc.generate(text)

wc.to_file('spurs_wordcloud.png')
