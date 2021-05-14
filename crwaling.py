import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from wordcloud import WordCloud

driver = webdriver.Chrome('')
driver.get('https://www.tottenhamhotspur.com/teams/men/players/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

text = ""

players = soup.select('#react_YFzEXth7UC2oZ7lkLILHg > div > div:nth-child(1)')

for player in player :
    name = player.select_one('div.PlayersPlayer__info > div.PlayersPlayer__name').text
    number = player.select_one('div.PlayersPlayer__info > div.PlayersPlayer__number').text
    text += name

    print(number,name)