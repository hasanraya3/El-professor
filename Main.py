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

# برمجة الأفعال عند الضغط على الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "register":
        bot.send_message(call.message.chat.id, "📝 للبدء، يرجى إرسال اسمك الكامل ورقم هاتفك.")
    
    elif call.data == "deposit":
        bot.send_message(call.message.chat.id, "💰 للشحن، يرجى تحويل المبلغ إلى المحفظة رقم: `123456789` ثم أرسل صورة التحويل هنا.")
    
    elif call.data == "withdraw":
        bot.send_message(call.message.chat.id, "💸 يرجى كتابة المبلغ الذي تود سحبه ورقم حسابك.")
    
    elif call.data == "admin":
        # هنا التعديل لإظهار رقم هاتفك
        phone_number = "+96176376296" # استبدل الـ X برقمك الحقيقي
        bot.send_contact(call.message.chat.id, phone_number, "البروفيسور")
        bot.send_message(call.message.chat.id, f"📞 يمكنك أيضاً مراسلتي مباشرة عبر واتساب أو اتصال على: {phone_number}")

if __name__ == "__main__":
    print("El-professor Bot is Updated with Phone Support...")
    bot.infinity_polling()
