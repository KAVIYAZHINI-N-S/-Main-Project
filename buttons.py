import telebot
from telebot import types

bot_token = '6781433704:AAF9v2GrkBmq6XoBRiTO4zr6ZomGY9Mpitw'  
bot = telebot.TeleBot(bot_token)


markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
button1 = types.KeyboardButton('Erode')
button2 = types.KeyboardButton('Coimbatore')
button3 = types.KeyboardButton('Ariyalur')
button4 = types.KeyboardButton('Chengalpattu')
button5 = types.KeyboardButton('Chennai')
button6 = types.KeyboardButton('Cuddalore')
button7 = types.KeyboardButton('Dharmapuri')
button8 = types.KeyboardButton('Dindigul')
button9 = types.KeyboardButton('Kallakurichi')
button10 = types.KeyboardButton('Kancheepuram')
button11 = types.KeyboardButton('Karur')
button12 = types.KeyboardButton('Krishnagiri')
button13 = types.KeyboardButton('Madurai')
button14 = types.KeyboardButton('Mayiladuthurai')
button15 = types.KeyboardButton('Nagapattinam')
button16= types.KeyboardButton('Nagercoil')
button17=types.KeyboardButton('Namakkal')
button18=types.KeyboardButton('Perambalur')
button19=types.KeyboardButton('Pudukkottai')
button20=types.KeyboardButton('Ramanathapuram')
button21=types.KeyboardButton('Ranipet')
button22=types.KeyboardButton('Salem')
button23=types.KeyboardButton('Sivagangai')
button24=types.KeyboardButton('Tenkasi')
button25=types.KeyboardButton('Thanjavur')
button26=types.KeyboardButton('Theni')
button27=types.KeyboardButton('Thiruvallur')
button28=types.KeyboardButton('Thiruvarur')
button29=types.KeyboardButton('Thoothukudi')
button30=types.KeyboardButton('Tiruchirappalli')
button31=types.KeyboardButton('Tirunelveli')
button32=types.KeyboardButton('Tirupathur')
button33=types.KeyboardButton('Tiruppur')
button34=types.KeyboardButton('Tiruvannamalai')
button35=types.KeyboardButton('Udagamandalam')
button36=types.KeyboardButton('Vellore')
button37=types.KeyboardButton('Viluppuram')
button38=types.KeyboardButton('Virudhunagar')

markup.row(button1,button2,button3)
markup.row(button4,button5,button6)
markup.row(button7,button8,button9)
markup.row(button10,button11,button12)
markup.row(button13,button14,button15)
markup.row(button16,button17,button18)
markup.row(button19,button20,button21)
markup.row(button22,button23,button24)
markup.row(button25,button26,button27)
markup.row(button28,button29,button30)
markup.row(button31,button32,button33)
markup.row(button34,button35,button36)
markup.row(button37,button38)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['/search_the_district']
    buttons1=['/help', '/stop', '/Creater']
    markup.add(*[types.KeyboardButton(button) for button in buttons])
    markup.add(*[types.KeyboardButton(button) for button in buttons1])

    bot.reply_to(message, "I am a blood donation bot. How can I help you?", reply_markup=markup)

@bot.message_handler(commands=['stop'])
def stop_command(message):
    bot.reply_to(message, "Thank you for using me!")

@bot.message_handler(commands=['owner'])
def owner_command(message):
    bot.reply_to(message, "I was created by HugsforBugs")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "I am a blood donation bot. Kindly provide me details for further response")


@bot.message_handler(commands=['search_the_district'])
def district_command(message):
    bot.reply_to(message, 'Select the district:', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    bot.reply_to(message, "You can control me by sending these commands:\n/start - start bot\n/help - helps you\n/Creater - owner\n/stop- stop the bot", reply_markup=None)

# Polling loop to keep the bot running
print("Starting the bot....")
bot.polling()
