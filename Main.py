import os
import telebot
from telebot import types

# التوكن الخاص بك
TOKEN = "8358448475:AAGS6RnEyObHNsP84VXYpvVyYfuV9ubqKRA"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🚀 إنشاء حساب جديد", callback_data='register')
    btn2 = types.InlineKeyboardButton("💳 شحن رصيد", callback_data='deposit')
    btn3 = types.InlineKeyboardButton("💸 سحب الأرباح", callback_data='withdraw')
    btn4 = types.InlineKeyboardButton("📞 تواصل مع البروفيسور", callback_data='admin')
    markup.add(btn1, btn2, btn3, btn4)
    
    welcome_text = "🔥 **أهلاً بك في Elprofessor Agents** 🔥\n\nاختر من الخيارات أدناه للبدء:"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

if __name__ == "__main__":
    print("El-professor Bot is LIVE...")
    bot.infinity_polling()
