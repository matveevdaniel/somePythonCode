#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import python_weather
import asyncio
import os
import telebot

str_weather = 0
strung = ''
list=[]
async def getweather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
    weather = await client.get('Gomel')
    str_weather = weather.current.temperature
    
    print(type(str_weather))
    strung = str(str_weather)
    print(type(strung))
    print(strung)
    
    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        list.append(str(forecast))
#     print(list[0])  

if __name__ == '__main__':
  # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
  # for more details
  if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
  asyncio.run(getweather())



API_TOKEN = '6424255200:AAH_d766D0d3mX2LVYyWHnaWcRi7RuI2viY'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Старт бота.
Давай поболтаем!\
""")
   

@bot.message_handler(commands=['help'])
def send_welcome(message):
    #for m in range(5):
    bot.reply_to(message,"Чем могу помочь?")
    
    
    
@bot.message_handler(commands=['weather'])
def send_welcome(message):
    #for m in range(5):
    bot.reply_to(message,strung)    
    
    
    
@bot.message_handler(commands=['погода'])
def send_welcome(message):
    #for m in range(5):
    bot.reply_to(message,list[0])    


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()