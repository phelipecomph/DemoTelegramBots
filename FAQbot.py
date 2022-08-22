from telebot.async_telebot import AsyncTeleBot
import os

#Load Secrets
API_KEY = os.environ['FAQ_API_KEY']

# t.me/phelipecomphFAQ_bot
bot = AsyncTeleBot(API_KEY)

@bot.message_handler(commands=['geral'])
async def answer_geral(message):
    text = "O Phelipe é um desenvolvedor focado em Dados e Automação"
    await bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['habilidades'])
async def answer_skills(message):
    text = "O Phelipe sabe muuito de Python, SQL, criação de DashBoards e ChatBots"
    await bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['contato'])
async def answer_contact(message):
    text = """Você pode falar com o Phelipe por um dos canais a baixo:
Linkedin: https://www.linkedin.com/in/phelipecomph/
Email: phelipecomph42@gmail.com
WhatsApp: (34) 984256742
Telegram: https://t.me/phelipecomph"""
    await bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['projetos'])
async def answer_projects(message):
    text = """Tem 4 projetos que conheço bem, clique eu um dele para saber mais!:
/projeto1 Dashboard de Métricas Ágeis
/projeto2 Chatbot de Resultados no Discord
/projeto3 Bot de Telegram que centraliza mensagens
/projeto4 Eu!
"""
    await bot.send_message(message.chat.id,text)
    
@bot.message_handler(commands=['projeto1'])
async def answer_project1(message):
    text = """Dashboard de Métricas Ágeis"""
    await bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['projeto2'])
async def answer_project2(message):
    text = """Chatbot de Resultados no Discord"""
    await bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['projeto3'])
async def answer_project3(message):
    text = """Bot de Telegram que centraliza mensagens"""
    await bot.send_message(message.chat.id,text)

@bot.message_handler(commands=['projeto4'])
async def answer_project4(message):
    text = """Eu sou um simples bot Portfolio, respondo perguntas no formato de FAQ sobre meu desenvolvedor e outros projetos dele!
Obrigado por perguntar!
É um prazer te conhecer"""
    await bot.send_message(message.chat.id,text)

def verify(message):
    return True

@bot.message_handler(func=verify)
async def answer(message):
    text = """Olá eu sou o Bot do Phelipe com Ph!
Eu funciono como um portfolio!
Clique nas opções abaixo e eu te contarei um pouco mais sobre o Phelipe
/geral
/projetos
/habilidades
/contato
E se quiser ver com mais detalhes dá uma olhada no portfolio completo dele!
https://phelipecomph.github.io/"""
    await bot.reply_to(message,text)

    