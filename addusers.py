import telebot
from telebot import types

bot_token = '6781433704:AAF9v2GrkBmq6XoBRiTO4zr6ZomGY9Mpitw'
bot = telebot.TeleBot(bot_token)

# Define districts and corresponding cities
districts_cities_map = {
    'Erode': ['Sathyamangalam', 'Gobi', 'City3'],
    'Coimbatore': ['Avinashi', 'Palladam', 'City6'],
    'Ariyalur': ['City7', 'City8', 'City9'],
    'Chennai': ['City10', 'City11', 'City12'],
    'Cuddalore': ['City13', 'City14', 'City15'],
    'Dharmapuri': ['City16', 'City17', 'City18'],
    'Dindigul': ['City19', 'City20', 'City21'],
    'Kanchipuram': ['City22', 'City23', 'City24'],
    'Kanyakumari': ['City25', 'City26', 'City27'],
    'Karur': ['City28', 'City29', 'City30'],
    'Krishnagiri': ['City31', 'City32', 'City33'],
    'Madurai': ['City34', 'City35', 'City36'],
    'Nagapattinam': ['City37', 'City38', 'City39'],
    'Namakkal': ['City40', 'City41', 'City42'],
    'Nilgiris': ['City43', 'City44', 'City45'],
    'Perambalur': ['City46', 'City47', 'City48'],
    'Pudukkottai': ['City49', 'City50', 'City51'],
    'Ramanathapuram': ['City52', 'City53', 'City54'],
    'Salem': ['City55', 'City56', 'City57'],
    'Sivaganga': ['City58', 'City59', 'City60'],
    'Thanjavur': ['City61', 'City6', 'City63'],
    'Theni': ['City64', 'City65', 'City66'],
    'Thoothukudi(Tuticorin)': ['City67', 'City68', 'City69'],
    'Tiruchirappalli': ['City70', 'City71', 'City72'],
    'Tirunelveli': ['City73', 'City74', 'City75'],
    'Tiruppur': ['City76', 'City77', 'City78'],
    'Tiruvallur': ['City79', 'City80', 'City81'],
    'Tiruvannamalai': ['City82', 'City83', 'City84'],
    'Tiruvarur': ['City85', 'City86', 'City87'],
    'Vellore': ['City88', 'City89', 'City90'],
    'Viluppuram': ['City91', 'City92', 'City93'],
    'Virudhunagar': ['City94', 'City95', 'City96'],
    'Chengalpattu': ['City97', 'City98', 'City99'],
    'Ranipet': ['City100', 'City101', 'City102'],
    'Tenkasi': ['City103', 'City104', 'City105'],
    'Kallakurichi': ['City106', 'City107', 'City108'],
    'Mayiladuthurai': ['City109', 'City110', 'City111'],
    'Tirupattur': ['City112', 'City113', 'City114'],
}

# Define blood types
blood_types = ['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-']

user_district_map = {}
user_city_map = {}
user_blood_type_map = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['/search_the_district']
    buttons1 = ['/help', '/stop', '/Creater']
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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # Create buttons for all districts
    district_buttons = [types.KeyboardButton(district) for district in districts_cities_map.keys()]
    markup.add(*district_buttons)

    bot.reply_to(message, 'Select the district:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in districts_cities_map.keys())
def handle_district_selection(message):
    selected_district = message.text
    user_district_map[message.chat.id] = selected_district

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # Create buttons for cities based on the selected district
    city_buttons = [types.KeyboardButton(city) for city in districts_cities_map[selected_district]]
    markup.add(*city_buttons)

    bot.reply_to(message, f'Select the city in {selected_district}:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in [city for cities in districts_cities_map.values() for city in cities])
def handle_city_selection(message):
    selected_city = message.text
    user_city_map[message.chat.id] = selected_city

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # Create buttons for blood types
    blood_type_buttons = [types.KeyboardButton(blood_type) for blood_type in blood_types]
    markup.add(*blood_type_buttons)

    bot.reply_to(message, f'Select your blood type in {selected_city}:', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in blood_types)
def handle_blood_type_selection(message):
    selected_blood_type = message.text
    user_blood_type_map[message.chat.id] = selected_blood_type

    # Now you can retrieve the list of donors based on the selected district, city, and blood type
    selected_district = user_district_map.get(message.chat.id)
    selected_city = user_city_map.get(message.chat.id)

    if selected_district and selected_city:
        # Retrieve donors based on the selected criteria (you can replace this with your actual data)
        donors = get_donors(selected_district, selected_city, selected_blood_type)

        if donors:
            response = f'Donors with blood type {selected_blood_type} in {selected_city}, {selected_district}:\n'
            for donor in donors:
                response += f'{donor["name"]} {donor["contact"]}\n'
        else:
            response = f'No donors found with blood type {selected_blood_type} in {selected_city}, {selected_district}.'

        bot.reply_to(message, response, reply_markup=None)
    else:
        bot.reply_to(message, 'Please select district, city, and blood type first.')

# Function to simulate retrieving donors (replace this with your actual data retrieval logic)
def get_donors(district, city, blood_type):
    # This is a placeholder. You should replace this with your actual data retrieval logic.
    # The structure of donors should be a list of dictionaries with 'name' and 'contact' keys.
    if district == 'Erode':
        if city == 'Sathyamangalam':
            if blood_type == 'A+':
                donors = [
                    {'name': 'Arjun', 'contact': '9345******'},
                    {'name': 'Lakshmi', 'contact': '877861****'},
                    {'name': 'Selvaraj', 'contact': '7708*****'}
                    # Add more donors as needed
                ]
            elif blood_type == 'A-':
                donors = [
                    {'name': 'Lee', 'contact': '9345******'},
                    {'name': 'Loi', 'contact': '877861****'},
                    {'name': 'Leo', 'contact': '7708*****'}
                    # Add more donors as needed
                ]
            elif blood_type == 'O+':
                donors = [
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='O-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='B+':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='B-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='AB+':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='AB-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
        if city == 'Gobi':
            if blood_type == 'A+':
                donors = [
                    {'name': 'Arjun', 'contact': '9345******'},
                    {'name': 'Lakshmi', 'contact': '877861****'},
                    {'name': 'Selvaraj', 'contact': '7708*****'}
                    # Add more donors as needed
                ]
            elif blood_type == 'A-':
                donors = [
                    {'name': 'Lee', 'contact': '9345******'},
                    {'name': 'Loi', 'contact': '877861****'},
                    {'name': 'Leo', 'contact': '7708*****'}
                    # Add more donors as needed
                ]
            elif blood_type == 'O+':
                donors = [
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='O-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='B+':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='B-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='AB+':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='AB-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            else:
                donors = []  # Return an empty list for other blood types
            return donors
    
    elif district == 'Coimbatore':
        if city == 'Avinashi':
            if blood_type == 'A+':
                donors = [
                     {'name': 'Arjun', 'contact': '9345******'},
                     {'name': 'Lakshmi', 'contact': '877861****'},
                     {'name': 'Selvaraj', 'contact': '7708*****'}
                ]
            elif blood_type =='A-':
                donors = [
                     {'name': 'Lee', 'contact': '9345******'},
                     {'name': 'Loi', 'contact': '877861****'},
                     {'name': 'Leo', 'contact': '7708*****'}
                    # Add more donors as needed
                ]
            elif blood_type=='O+':
                donors = [
                       {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
        if city == 'Palladam':
            if blood_type == 'A+':
                donors = [
                    {'name': 'Arjun', 'contact': '9345******'},
                    {'name': 'Lakshmi', 'contact': '877861****'},
                    {'name': 'Selvaraj', 'contact': '7708*****'}
                    # Add more donors as needed
                ]
            elif blood_type == 'A-':
                donors = [
                    {'name': 'Lee', 'contact': '9345******'},
                    {'name': 'Loi', 'contact': '877861****'},
                    {'name': 'Leo', 'contact': '7708*****'}
                    # Add more donors as needed
                ]
            elif blood_type == 'O+':
                donors = [
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='O-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='B+':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='B-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='AB+':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            elif blood_type=='AB-':
                donors=[
                    {'name': 'KKK', 'contact': '6789******'},
                    {'name': 'NHTY', 'contact': '9876******'},
                    {'name': 'REWN', 'contact': '9876543***'}
                    # Add more donors as needed
                ]
            else:
                donors = []  # Return an empty list for other blood types
            return donors
    else:
        donors = []  # Return an empty list for other districts
    return donors

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    bot.reply_to(message, "You can control me by sending these commands:\n/start - start bot\n/help - helps you\n/Creater - owner\n/stop- stop the bot", reply_markup=None)

# Polling loop to keep the bot running
print("Starting the bot....")
bot.polling()
