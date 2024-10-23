import telebot

bot_token = '6781433704:AAF9v2GrkBmq6XoBRiTO4zr6ZomGY9Mpitw'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "I am blood donation bot")

@bot.message_handler(commands=['greet'])
def greet_command(message):
    bot.reply_to(message, "Hello, How can i help you")
    
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "I am blood donation bot. Kindly provide me details for further response")

@bot.message_handler(commands=['stop'])
def stop_command(message):
    bot.reply_to(message, "Thankyou for using me!")

@bot.message_handler(commands=['owner'])
def owner_command(message):
    bot.reply_to(message, "I was created by HugsforBugs")

@bot.message_handler(commands=['search_blood'])
def search_blood_command(message):
    bot.reply_to(message, "https://www.redcrossblood.org/")

@bot.message_handler(commands=['search'])
def search_blood_command(message):
    bot.reply_to(message, "#yet to be coded")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message,"You can control me by sending these commands:\n/start-start bot \n/greet-greets you \n/help-helps you \n/owner-owner \n/search_blood-webpage \n/search - search")


# Polling loop to keep the bot running
print("Starting the bot....")
bot.polling()