import telebot
from telebot.types import ReactionTypeEmoji
import random
import os

bot = telebot.TeleBot("8554078106:AAGOcgYMxS3YK_NPPmQ3wEPVvlz-W2yFS5w")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    imgs = os.listdir(r'C:\Users\Ирина\проекты VS code\meme_bot\images')
    bot.reply_to(message, imgs)
    print(imgs)
    with open(fr'C:\Users\Ирина\проекты VS code\meme_bot\images\{random.choice(imgs)}', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    

bot.polling()  
