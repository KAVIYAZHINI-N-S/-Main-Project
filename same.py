import telebot

bot_token = '6781433704:AAF9v2GrkBmq6XoBRiTO4zr6ZomGY9Mpitw'  # Add your bot token here
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "I am a blood donation bot")

@bot.message_handler(commands=['greet'])
def greet_command(message):
    bot.reply_to(message, "Hello, How can I help you")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "I am a blood donation bot. Kindly provide me details for further response")

@bot.message_handler(commands=['stop'])
def stop_command(message):
    bot.reply_to(message, "Thank you for using me!")

@bot.message_handler(commands=['owner'])
def owner_command(message):
    bot.reply_to(message, "I was created by HugsforBugs")

@bot.message_handler(commands=['search_blood'])
def search_blood_command(message):
    bot.reply_to(message, "https://www.redcrossblood.org/")

@bot.message_handler(commands=['search'])
def search_command(message):
    bot.reply_to(message, "#yet to be coded")

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    text = message.text.lower()

    if '/district' in text:
        bot.reply_to(message, "Please provide your district")
        if 'Erode' in text:
            bot.reply_to(message,"please provide your city")

    elif '/city' in text:
        bot.reply_to(message, "Please provide the blood type")

    elif '/blood_type' in text:
        bot.reply_to(message, "Please provide additional details or perform the search")

    else:
        bot.reply_to(message, "You can control me by sending these commands:\n/start - start bot\n/greet - greets you\n/help - helps you\n/owner - owner\n/search_blood - webpage\n/search - search\n/district - provide district\n/city - provide city\n/blood_type - provide blood type")


# Polling loop to keep the bot running
print("Starting the bot....")
bot.polling()
