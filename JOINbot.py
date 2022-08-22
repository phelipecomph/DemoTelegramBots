from telebot.async_telebot import AsyncTeleBot
import os

#Load Secrets
API_KEY = os.environ['JOIN_API_KEY']

#t.me/nowcurrency_bot
bot = AsyncTeleBot(API_KEY)




def verify(message):
    return True

@bot.message_handler(func=verify)
async def answer(message):
    text = """Olá eu sou um bot que trás mensagens de grupos"""
    await bot.reply_to(message,text)

