import telebot
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot(token = '5838533107:AAEQ3cz1Mem5ThFU1X6uBdsThW2sn5BWVXM')
url = "https://arzdigital.com/coins/"
@bot.message_handler(commands=['start'])

def start_command(message):
   bot.send_message(
       message.chat.id,
       'به ربات قیمت لحظه ای ارزهای دیجیتال خوش آمدید\n' +
       'برای مشاهده قیمت ها دستور /getPrice را وارد کنید\n' 
   )

@bot.message_handler(commands=['getPrice'])

def start_command(message):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    allCoinsTrTag = soup.find_all('tr', class_='arz-coin-tr arz-sort-value-row arz-fiat-parent')
    for index in range(len(allCoinsTrTag)):
      if index == 15 :
         break
      coinName = allCoinsTrTag[index]['data-faname']
      coinPricesData  = allCoinsTrTag[index].find_all('td' , class_ = 'arz-coin-table__rial-price-td arz-sort-value')
      coinPrice = coinPricesData[0].find_all('span')[0].getText()
      coinSwingData  = allCoinsTrTag[index].find_all('td' , class_ = 'arz-coin-table__daily-swing-td arz-sort-value')
      percentOfDailySwing = coinSwingData[0].find_all('span')[0].getText()
      bot.send_message(
       message.chat.id,
      coinName + ' ' + coinPrice + ' ' + percentOfDailySwing +'\n')
bot.polling(none_stop=True)
