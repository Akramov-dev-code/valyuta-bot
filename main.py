from telebot import TeleBot
from config import token
from telebot.types import Message
from utils import get_all_currency
from telebot.util import extract_arguments

bot = TeleBot(token)

currencies = get_all_currency()


#  start buyrug'i

@bot.message_handler(commands=["start"])
def start_handler(message: Message):
    bot.send_message(message.chat.id, f"Assalomu alaykum {message.from_user.full_name}👋\nMen valyuta botman💰\n/usd - dollar kursi\n/eur - euro kursi\n/rub - rubl kursi\n/all - barchasini ko'rish")
    

@bot.message_handler(commands=["all"])
def all_currency_handler(message: Message):
    if not currencies:
        bot.send_message(message.chat.id, "Menda ma'lumotlar topilmadi🥴")
        return
    
    text = ''
    for currency in currencies:
        text += f"{currency[0]} - {currency[1]} so'm\n"
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["usd"])
def usd_handler(message: Message):
    price = int(currencies[0][1])
    args = extract_arguments(message.text)
    
    if args and not args.isdigit():
        bot.send_message(message.chat.id, "Noto'g'ri buyruq!\nMa'lumot uchun /info")
        return
    
    
    count = 1
    if args:
       count = int(args)
    
    bot.send_message(message.chat.id, f"{count} 💲 - {count * price} so'm") 
    
        

@bot.message_handler(commands=["eur"])
def euro(message: Message):
    pass  


if __name__ == "__main__":
    print("Bot ishga tushdi")
    bot.infinity_polling()