import telebot
from telebot import types

bot_token = '6781433704:AAF9v2GrkBmq6XoBRiTO4zr6ZomGY9Mpitw'
bot = telebot.TeleBot(bot_token)

# Define districts and corresponding cities
districts_cities_map = {
    'Erode': ['Sathyamangalam', 'Gobichettipalayam', 'City3'],
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
                    {'name': 'Deepak', 'contact': '9566439230'},
                    {'name': 'sivakumar. R', 'contact': '9566313265'},
                    {'name': 'vijayaragavan', 'contact': '9843328581'},
                    {'name': 'DHANABAL MARIRAJ', 'contact': '9886367502'},
                    {'name': 'Gurunathan', 'contact': '9942353277'},
                    {'name': 'p. k. Raajan', 'contact': '9894372248'},
                    {'name': 'Nayeemudeen', 'contact': '9566645616'},
                    {'name': 'Jayaprabu Padmaraj', 'contact': '9900273566'},
                    {'name': 'S.SAKTHIVEL', 'contact': '9994443206'},
                    {'name': 'vikram', 'contact': '9698220189'},
                    {'name': 'POOVARASAN M', 'contact': '9894889862'},
                    {'name': 'Sanoj Kumar.R', 'contact': '9688168273'},
                    {'name': 'periyasamy', 'contact': '9965657549'},
                    {'name': 'SHIVAMURTHY.H', 'contact': '9626211568'},
                    {'name': 'kirubaaa', 'contact': '9791427342'},
                    {'name': 'BATHRINATH R', 'contact': '9865232395'},
                    {'name': 'Kumar Chinnaiyan', 'contact': '9942999111'},
                    {'name': 'manobharathy', 'contact': '9786554842'},
                    {'name': 'Ram', 'contact': '9659664591'},
                    {'name': 'Nayeem A.1', 'contact': '9566645616'},
                    {'name': 'Mahalingam', 'contact': '6382708932'},
                    {'name': 'RameshSubramaniyam', 'contact': '9789688278'},
                    {'name': 'Navaneethakrishnan', 'contact': '8056521141'},
                    {'name': 'C.SENTHILKUMAR', 'contact': '8883417781'},
                    {'name': 'Logesh', 'contact': '9488933666'},
                    {'name': 'Nazeerulla', 'contact': '9600511106'},
                    {'name': 'MURUGESAN R', 'contact': '8903780633'},
                    {'name': 'Manoj kumar', 'contact': '8883985213'},
                    {'name': 'ranjith Kumar', 'contact': '8526467242'},
                    {'name': 'Someshwaran', 'contact': '9791639229'},
                    {'name': 'SRIRAM', 'contact': '9943011211'},
                    {'name': 'YUVARAJ', 'contact': '9500649114'},
                    {'name': 'Mohamed Wasig', 'contact': '9894549111'},
                    {'name': 'Joe Ravi Fernandas A', 'contact': '7904298590'},
                    {'name': 'Vadivel', 'contact': '8667673042'},
                    {'name': 'PRABU ram k', 'contact': '7695812927'},
                    {'name': 'rutrakkumaar A P', 'contact': '9994133941'},
                    {'name': 'Dinesh Dhayalan', 'contact': '9042984844'},
                    {'name': 'KUMAR S.R', 'contact': '9865232395'},
                    {'name': 'Shanmuga sundaram', 'contact': '9677773348'},
                    {'name': 'Anush kumar S', 'contact': '8760251145'},
                    {'name': 'Aneesh ahamed', 'contact': '9944331982'},
                    {'name': 'Aiyf Basheer', 'contact': '9500507256'},
                    {'name': 'Rajesh S', 'contact': '8148429771'},
                    {'name': 'ganapathi', 'contact': '7339621147'},
                    {'name': 'Rameshkumar', 'contact': '9788299777'},
                    {'name': 'Sanjay v', 'contact': '9566350471'},
                    {'name': 'S. GOWTHAM', 'contact': '9025659352'},
                    {'name': 'MAHADEVAN', 'contact': '9943184194'},
                    {'name': 'JAWAHAR', 'contact': '8344353637'}
               ]
               
            elif blood_type == 'A-':
                donors = [
                    {'name': 'Bharathi raja', 'contact': '8667055633'},
                    {'name': 'praveenkumar', 'contact': '7845691662'},
                    {'name': 'Bharathi raja', 'contact': '8667055633'},
                    {'name': 'sri Manikandan', 'contact': '8637650085'}
                ]
               
            elif blood_type == 'O+':
                donors = [
                    {'name': 's.seshadri', 'contact': '9994363731'},
                    {'name': 'Om0rakash', 'contact': '9790618046'},
                    {'name': 'vadivelu', 'contact': '9940294388'},
                    {'name': 'Saran kumar Ramasamy', 'contact': '7868990445'},
                    {'name': 'Sreedharan S', 'contact': '8056786575'},
                    {'name': 'Kandhakumar', 'contact': '8838684528'},
                    {'name': 'Udhayakumar', 'contact': '8526070314'},
                    {'name': 'Aram kathar', 'contact': '8056554053'},
                    {'name': 'ANANTHA KUMAR B', 'contact': '9865207779'},
                    {'name': 'Pravinkumar', 'contact': '9597510979'},
                    {'name': 'dinesh', 'contact': '9095944492'},
                    {'name': 'R.Selvakumat', 'contact': '9025450305'},
                    {'name': 'Prasath Narayanan', 'contact': '9066695777'},
                    {'name': 'thannasiappan', 'contact': '8610549731'},
                    {'name': 'zaffrullah', 'contact': '7373562678'},
                    {'name': 'M.Balaguru', 'contact': '9976612125'},
                    {'name': 'kathirvel', 'contact': '9790013413'},
                    {'name': 'Arun', 'contact': '9025175875'},
                    {'name': 'santhosh', 'contact': '9159819980'},
                    {'name': 'Manoharan', 'contact': '9159381151'},
                    {'name': 'Vijayanand.S', 'contact': '9976634903'},
                    {'name': 'J.lawrance jerome', 'contact': '8344195534'},
                    {'name': 'Saravana Kumar M', 'contact': '9894682660'},
                    {'name': 'HARITHARAN', 'contact': '7904093171'},
                    {'name': 'mouna priya', 'contact': '6379286165'},
                    {'name': 'Mylsamy S', 'contact': '9942293388'},
                    {'name': 'PRABHU R', 'contact': '9578777517'},
                    {'name': 'Vishnukumar', 'contact': '8110080800'},
                    {'name': 'suldhan', 'contact': '9715563924'},
                    {'name': 'Ram mahendar', 'contact': '9677506077'},
                    {'name': 'Devaraj', 'contact': '8883417521'},
                    {'name': 'Daniel', 'contact': '9003467848'},
                    {'name': 'Mahasivanesan', 'contact': '9159076558'},
                    {'name': 'S.ABDUL FARITH', 'contact': '9790522353'},
                    {'name': 'G M Pravin', 'contact': '8056556401'},
                    {'name': 'LAKSHMANAKUMAR P', 'contact': '9994310444'},
                    {'name': 'santhosh kumar.t', 'contact': '9894530033'},
                    {'name': 'Elavarasan', 'contact': '9842916429'},
                    {'name': 'DINESH KANAGARAJ', 'contact': '9715562886'},
                    {'name': 'Nandha kumar', 'contact': '9842668801'},
                    {'name': 'RAMESH.K', 'contact': '9842519794'},
                    {'name': 'BALASUBARAMANI S', 'contact': '8012185773'},
                    {'name': 'JANARTHANAN.M', 'contact': '9500602274'},
                    {'name': 'Abuthahir', 'contact': '9942527193'},
                    {'name': 'B.Karthikeyan', 'contact': '9865657476'},
                    {'name': 'Arunsakdeeban', 'contact': '9842688777'},
                    {'name': 'Govindaraj.m', 'contact': '9677840500'},
                    {'name': 'Aswin', 'contact': '8760765642'},
                    {'name': 'parthasarathi', 'contact': '9894439536'},
                    {'name': 'Parthiban', 'contact': '9600429252'},
                    {'name': 'jagadeesh', 'contact': '9843110905'},
                    {'name': 'R.VENKATESH', 'contact': '9944520159'},
                    {'name': 'Krithika', 'contact': '9003744337'},
                    {'name': 'Naveen', 'contact': '9790796094'},
                    {'name': 'Mohankumar N', 'contact': '9095807143'},
                    {'name': 'Dinesh Kumar.C C', 'contact': '9585945319'},
                    {'name': 'SELVARAJ OTHISAMY', 'contact': '9500959493'},
                    {'name': 'Gowthaman', 'contact': '9894385001'},
                    {'name': 'Mohan', 'contact': '9787880948'},
                    {'name': 'SENGUTTUVAN.S', 'contact': '9629958588'},
                    {'name': 'easwaran', 'contact': '9865234663'},
                    {'name': 'Dhanush', 'contact': '9500533828'},
                    {'name': 'Chithuraj', 'contact': '9626266474'},
                    {'name': 'karthikkannan.E', 'contact': '9655037735'},
                    {'name': 'balaguru', 'contact': '9976612125'},
                    {'name': 'RIJO JOEL J', 'contact': '9488993147'},
                    {'name': 'Mubarak', 'contact': '9944052892'},
                    {'name': 'KARTHIK V', 'contact': '9944766744'},
                    {'name': 'Nithyanantham T', 'contact': '9976055328'},
                    {'name': 'Abuthahir', 'contact': '9942527193'},
                    {'name': 'Naveenkumar', 'contact': '7904365925'},
                    {'name': 'Dhinesh.M', 'contact': '9942959170'},
                    {'name': 'RAMESH', 'contact': '9443945511'},
                    {'name': 'KATHIRVEL', 'contact': '8667220975'},
                    {'name': 'ARAM Kadhar', 'contact': '8056554053'},
                    {'name': 's.mahendran.', 'contact': '9843643048'},
                    {'name': 'Rajanna.s', 'contact': '8110041248'},
                    {'name': 'Balasubramaniam', 'contact': '8610747751'},
                    {'name': 'S.Perumal', 'contact': '9787160903'},
                    {'name': 'Loganathan', 'contact': '9942946138'},
                    {'name': 'VAIRAMUTHU', 'contact': '9944606123'},
                    {'name': 'Prem Kumar', 'contact': '9865799382'},
                    {'name': 'Tamilarasan.T.V', 'contact': '9566336297'},
                    {'name': 'NAVEEN KUMAR N', 'contact': '9626144300'},
                    {'name': 'Shellappandi', 'contact': '9751980506'},
                    {'name': 'ANWAR', 'contact': '8754971114'},
                    {'name': 'Sundaramoorthi Arumugam', 'contact': '9965685701'},
                    {'name': 'vijaikumar', 'contact': '9791622204'},
                    {'name': 'Sureshkumar', 'contact': '9524740305'},
                    {'name': 'Abishek', 'contact': '9942969911'},
                    {'name': 'Dhanya', 'contact': '9003340468'},
                    {'name': 'Kalai Selvan', 'contact': '9384731230'},
                    {'name': 'anandakumar suberamani', 'contact': '9443304545'},
                    {'name': 'Prasath V.', 'contact': '9994236355'},
                    {'name': 'Ranjeth', 'contact': '9677561952'},
                    {'name': 'S.Sridhar', 'contact': '9787893976'},
                    {'name': 'BALAJI', 'contact': '9443545617'},
                    {'name': 'Sanjit Velumani', 'contact': '9677591352'},
                    {'name': 'J.lawrancejerome', 'contact': '8344195534'},
                    {'name': 'Sabari', 'contact': '9688879348'},
                    {'name': 'hariprasanth', 'contact': '9994161169'},
                    {'name': 'S.DHINESH KUMAR', 'contact': '9659221865'},
                    {'name': 'AJITH', 'contact': '6374435455'},
                    {'name': 'N. Balamuthu', 'contact': '9500575005'},
                    {'name': 'Kathiresan Subramaniam', 'contact': '9790261680'},
                    {'name': 'Karthikeyan', 'contact': '9865657476'},
                    {'name': 'Ajithkumar', 'contact': '6383141008'},
                    {'name': 'L.R.PARTHIBAN', 'contact': '9677564745'},
                    {'name': 'S.Shriram', 'contact': '9976446469'},
                    {'name': 'Muthukumar', 'contact': '9123582662'},
                    {'name': 'Abishek.D', 'contact': '8778539737'},
                    {'name': 'Shasanth', 'contact': '9578625027'},
                    {'name': 'k.kadhar bhasha', 'contact': '8056554053'},
                    {'name': 'Palanisamy D', 'contact': '9688661784'},
                    {'name': 'RAJKUMARD', 'contact': '9843375766'},
                    {'name': 'Nithyanantham T', 'contact': '6379438822'}
                ]
                
            elif blood_type=='O-':
                donors=[
                   {'name': 'santhosh k', 'contact': '9025734416'},
                    {'name': 'luies raj', 'contact': '9865740920'},
                    {'name': 'VanithaSundar', 'contact': '9524805019'},
                    {'name': 'Shakthi Siva', 'contact': '9159744625'},
                    {'name': 'senthil kumar', 'contact': '8973414121'},
                    {'name': 'Shibee Shanmugam', 'contact': '9790674812'},
                    {'name': 'manjunathaeswaran', 'contact': '8870207058'},
                    {'name': 'A.K.BALASUNDARAM', 'contact': '9025134567'},
                    {'name': 'Vignesh VP', 'contact': '9843456337'},
                    {'name': 'Syed Mujibur Rahman', 'contact': '9865012495'},
                    {'name': 'mubarak ali', 'contact': '7639753821'},
                    {'name': 'sathish', 'contact': '9688667329'},
                    {'name': 'SARAVANA KUMAR', 'contact': '9994053526'},
                    {'name': 'Dr.T.Nithya', 'contact': '9043475369'}
                ]
               
            elif blood_type=='B+':
                donors = [
                    {'name': 'Thamarai selvi', 'contact': '9025307980'},
                    {'name': 'mohan kumar', 'contact': '9345205441'},
                    {'name': 'vignesh', 'contact': '8883823603'},
                    {'name': 'Ranjitha', 'contact': '8190876969'},
                    {'name': 'M.Poornachandran', 'contact': '9942946683'},
                    {'name': 'SUNDARA', 'contact': '7676767370'},
                    {'name': 'SIVAKUMAR S.S', 'contact': '9842675985'},
                    {'name': 'Zaheed Abdullah s. a', 'contact': '9443065499'},
                    {'name': 'fazil', 'contact': '9659090786'},
                    {'name': 'RANJITHKUMAR', 'contact': '9524069587'},
                    {'name': 'Preethi Natarajan', 'contact': '9345488873'},
                    {'name': 'M Leo Joseph', 'contact': '9894607189'},
                    {'name': 'Siddaraju R', 'contact': '6379749554'},
                    {'name': 'Vignesh', 'contact': '9626840585'},
                    {'name': 'SURENDARNATH. S', 'contact': '8220475643'},
                    {'name': 'DineshkumarV', 'contact': '9566602331'},
                    {'name': 'SIVAKUMAR.V', 'contact': '9865272717'},
                    {'name': 'RAGHU V', 'contact': '9865710150'},
                    {'name': 'Hariprakash', 'contact': '9715562345'},
                    {'name': 'Gokul.A', 'contact': '8489516179'},
                    {'name': 'Chandru', 'contact': '8754507326'},
                    {'name': 'Immanuel.L', 'contact': '9585813850'},
                    {'name': 'surendhar kumar', 'contact': '9585471892'},
                    {'name': 'Thiyagaraj A', 'contact': '9715946760'},
                    {'name': 'shankar', 'contact': '9003477779'},
                    {'name': 'seenu a supramani', 'contact': '9790204988'},
                    {'name': 'Karthik', 'contact': '8883660295'},
                    {'name': 'R.Dinesh', 'contact': '9789729394'},
                    {'name': 'Ashokkumar', 'contact': '9043695569'},
                    {'name': 'SURESH N', 'contact': '8124491233'},
                    {'name': 'Ravichandran. S', 'contact': '9158779662'},
                    {'name': 'Gowtham', 'contact': '9159847531'},
                    {'name': 'PRABHAHARAN', 'contact': '9944053663'},
                    {'name': 'Selvanayagam R', 'contact': '8807534363'},
                    {'name': 'Raghunandha N', 'contact': '9445726683'},
                    {'name': 'Poovarasu. K', 'contact': '8838880893'},
                    {'name': 'Vaideeswaran', 'contact': '9943726442'},
                    {'name': 'PA KRISHNAMURTHY', 'contact': '7904478984'},
                    {'name': 'DinesBaBu', 'contact': '9698090706'},
                    {'name': 'Viswanath V', 'contact': '9791301812'},
                    {'name': 'Lakshmi', 'contact': '9962522312'},
                    {'name': 'vijay', 'contact': '8903413900'},
                    {'name': 'Hari Prakash', 'contact': '9894522901'},
                    {'name': 'Naveengowtham', 'contact': '7598435342'},
                    {'name': 'SARANPRABHU S S', 'contact': '8344823211'},
                    {'name': 'sivagopal', 'contact': '9751901891'},
                    {'name': 'Surendar.v', 'contact': '7502773833'},
                    {'name': 'Dhanasekaran', 'contact': '9739002795'},
                    {'name': 'K NATARAJAN', 'contact': '9942966641'},
                    {'name': 'SUGANTHARAJ.G', 'contact': '9600940018'},
                    {'name': 'Arumugam.d', 'contact': '9843199363'},
                    {'name': 'Senthilkumar', 'contact': '9600954643'},
                    {'name': 'Rajeshwaran P', 'contact': '9597439539'},
                    {'name': 'S Prabhakaran', 'contact': '9566655889'},
                    {'name': 'Samivel p', 'contact': '9629839297'},
                    {'name': 'SanthosH', 'contact': '9003340803'},
                    {'name': 'kirubhakaran', 'contact': '7667609045'},
                    {'name': 'ikram irshu', 'contact': '9500507393'},
                    {'name': 'pradeep', 'contact': '9095061455'},
                    {'name': 'Nataraj', 'contact': '8760075101'},
                    {'name': 'M.Suriya', 'contact': '9597890977'},
                    {'name': 'manikandan', 'contact': '8610825078'},
                    {'name': 'kamal', 'contact': '9787696969'},
                    {'name': 'Karthikeyan', 'contact': '8754070192'},
                    {'name': 'Hassankhan', 'contact': '9442131714'},
                    {'name': 'Kesavan Rajan', 'contact': '9487200311'},
                    {'name': 'Saravana Parthiban', 'contact': '8940138758'},
                    {'name': 'Santhosh Kumar', 'contact': '9003340803'},
                    {'name': 's.bhuvaneswari', 'contact': '9003912541'},
                    {'name': 'MURALIKRISHNAN', 'contact': '9842840476'},
                    {'name': 'Kathirvel', 'contact': '9655829552'},
                    {'name': 'Vijayakumar', 'contact': '9965447223'},
                    {'name': 'Varatharaj', 'contact': '8675303526'},
                    {'name': 'R.mohankumar', 'contact': '9578062817'},
                    {'name': 's.gokul', 'contact': '9843224571'},
                    {'name': 'achuthan', 'contact': '9750777915'},
                    {'name': 'Prahadheshwar', 'contact': '9629852910'},
                    {'name': 'Prabhakaran', 'contact': '9943853436'},
                    {'name': 'Mubarak', 'contact': '9629962112'},
                    {'name': 'Mohamed Farooq', 'contact': '9443521642'},
                    {'name': 'GOBALAKRISHNAN', 'contact': '9629382802'}
                ]

            elif blood_type=='B-':
                donors=[
                    {'name': 'Pravin Riyaz', 'contact': '8807070907'},
                    {'name': 'GAUTHAM C', 'contact': '9659059035'},
                    {'name': 'KALIAPPAN M', 'contact': '9487927678'},
                    {'name': 'Ramachandran', 'contact': '9788736363'},
                    {'name': 'Mathan Nivash', 'contact': '9942542115'},
                    {'name': 'VENKATESAN T', 'contact': '9443185758'},
                    {'name': 'Gokul.P', 'contact': '6379688195'},
                    {'name': 'Bhuvanesh kumar P', 'contact': '9842720430'},
                    {'name': 'ERODE SARAVANAN SAMINATHAN', 'contact': '9677968978'},
                    {'name': 'vignesh', 'contact': '8883823603'},
                ]

            elif blood_type=='AB+':
                donors=[
                    {'name': 'Pradeep Kumar', 'contact': '9952433063'},
                    {'name': 'Sampath', 'contact': '9976111804'},
                    {'name': 'R Suganth', 'contact': '8344750120'},
                    {'name': 'Kathirvel', 'contact': '9790492404'},
                    {'name': 'Venkatraman', 'contact': '9865919242'},
                    {'name': 'Joel Mathew', 'contact': '9952324362'},
                    {'name': 'Vadivel', 'contact': '9488907909'}
                ]

            elif blood_type=='AB-':
                donors=[]
        if city == 'Gobichettipalayam':
            if blood_type == 'A+':
                donors = [
                   {'name': 'Elamathian', 'contact': '9994956956'},
                    {'name': 'Ramesh', 'contact': '6374228009'},
                    {'name': 'Deva', 'contact': '9566843454'},
                    {'name': 'Lakshmanan P', 'contact': '9944498020'},
                    {'name': 'Logesh N', 'contact': '9865376541'},
                    {'name': 'JANAKIRAMAN.S', 'contact': '9629711287'},
                    {'name': 'Manikandan.?', 'contact': '9025898167'},
                    {'name': 'yuvaraja Gm', 'contact': '8778835358'},
                    {'name': 'Sathish sharma', 'contact': '9843910203'},
                    {'name': 'hariharasudhan k.a', 'contact': '9003656867'},
                    {'name': 'shanmugam', 'contact': '9790500711'},
                    {'name': 'Gokulnath', 'contact': '9629310495'},
                    {'name': 'Gayathri devi', 'contact': '9884490806'},
                    {'name': 'Aswin Sankar C', 'contact': '9677640031'},
                    {'name': 'V.karthi kannan', 'contact': '9865411474'},
                    {'name': 'somasundaram', 'contact': '9942037577'},
                    {'name': 'prabhakaran', 'contact': '9865171616'},
                    {'name': 'Prakash', 'contact': '9600878263'},
                    {'name': 'Ajay Sooriya', 'contact': '9087743285'},
                    {'name': 'DineshRaja', 'contact': '6381567302'},
                    {'name': 'தரணீஷ்.S', 'contact': '8072727295'},
                    {'name': 'S Prakash', 'contact': '8973782992'},
                    {'name': 'm. jahier usean', 'contact': '9965155992'},
                    {'name': 'Hariharan V', 'contact': '8610333143'},
                    {'name': 'Kolathasamy', 'contact': '9659065083'},
                    {'name': 'Nijanthan', 'contact': '9003789957'},
                    {'name': 'Mohamed Rafic', 'contact': '6382574740'},
                    {'name': 'KARUPPUSAMY.V', 'contact': '6383998377'},
                    {'name': 'S.Kannan', 'contact': '7708929133'},
                    {'name': 'Muthukumar', 'contact': '9843725934'},
                ]
            elif blood_type == 'A-':
                donors = [
                    {'name': 'Suresh', 'contact': '9500921884'},
                ]
            elif blood_type == 'O+':
                donors = [
                   {'name': 'PRABHAKARAN M V', 'contact': '9443499151'},
                    {'name': 'm.dinesh', 'contact': '9894345920'},
                    {'name': 'KIRUTHIKA. A', 'contact': '7548860497'},
                    {'name': 'Naveen', 'contact': '9360348529'},
                    {'name': 'P Sampath', 'contact': '9942379171'},
                    {'name': 'saravanan', 'contact': '9865881575'},
                    {'name': 'K.S.KOTHANDAN', 'contact': '9524355293'},
                    {'name': 'K.S.KOTHANDAN', 'contact': '9524355293'},
                    {'name': 'Haris kumar', 'contact': '9384170093'},
                    {'name': 'Jeyaprakash.S', 'contact': '9865133278'},
                    {'name': 'Rajbhagavath A.P', 'contact': '9677361983'},
                    {'name': 'R. sureshkumar', 'contact': '9865011742'},
                    {'name': 'Raja', 'contact': '8217633928'},
                    {'name': 'S MADHUSUTHANAN', 'contact': '9043539062'},
                    {'name': 'Ramachandran N', 'contact': '9994499407'},
                    {'name': 'Thangavel', 'contact': '9688960733'},
                    {'name': 'Dhiyanesh', 'contact': '6374454535'},
                    {'name': 'shanmugam', 'contact': '8903118427'},
                    {'name': 'karthikeyan', 'contact': '9003880580'},
                    {'name': 'K. R. PRABHU', 'contact': '9566376629'},
                    {'name': 'Akilesh', 'contact': '6383447819'},
                    {'name': 'S.J.Aadhil bathusha', 'contact': '9500516603'},
                    {'name': 'Balakumar', 'contact': '8526965518'},
                    {'name': 'Gunasekaran', 'contact': '8012433511'},
                    {'name': 'Gnanavel', 'contact': '9943187197'},
                    {'name': 'J.MADESWARAN', 'contact': '9655098738'},
                    {'name': 'venkateshwaran', 'contact': '9789171182'},
                    {'name': 'somasundaram A.M.', 'contact': '9886134723'},
                    {'name': 'P.Mahesh Kumar', 'contact': '9944030637'},
                    {'name': 'P.Karuppusamy', 'contact': '9677744107'},
                    {'name': 'kirankumar', 'contact': '9789572297'},
                    {'name': 'karthik', 'contact': '9965591818'},
                    {'name': 'P.Balachandar', 'contact': '9965704205'},
                    {'name': 'Arivolee V N', 'contact': '9442554819'},
                    {'name': 'gowri shyam', 'contact': '9042680392'},
                    {'name': 'kuppuraj', 'contact': '9976978414'},
                    {'name': 'Gurumoorthy M', 'contact': '9786270437'},
                    {'name': 'rafeekjf', 'contact': '9488972021'},
                    {'name': 'Dharanidharan', 'contact': '7904732181'},
                    {'name': 'Sri Kritika M', 'contact': '9489404084'},
                    {'name': 'S.Arul kumar', 'contact': '9445253944'},
                    {'name': 'Sowndhararajan', 'contact': '9944842532'},
                    {'name': 'thiyagu', 'contact': '7904219209'},
                    {'name': 'Ganesan', 'contact': '9884340075'},
                    {'name': 'Gowtham.G', 'contact': '9629655544'},
                    {'name': 'Deepan', 'contact': '9597995117'},
                    {'name': 'kandasamy sampathkumar', 'contact': '9443090277'},
                    {'name': 'logeshwaran', 'contact': '9943890740'},
                    {'name': 'Mugunthan', 'contact': '7339241241'},
                    {'name': 'Gowtham', 'contact': '9688849734'},
                    {'name': 'Andamuthu', 'contact': '9842881583'},
                    {'name': 'Meganathan', 'contact': '9940756168'},
                    {'name': 'SENTHILNATHAN.R', 'contact': '9566604235'},
                    {'name': 'ARUL MURUGAN R', 'contact': '7667542070'},
                    {'name': 'Thirumalaisamy S', 'contact': '6383111060'},
                    {'name': 'Sureshragul', 'contact': '8015810003'},
                    {'name': 'Gowdhaman Rajakrishnan', 'contact': '9976654824'},
                    {'name': 'DharaniDharan. M', 'contact': '6383944412'},
                    {'name': 'Mohankumar Muthusamy', 'contact': '9940791281'},
                    {'name': 'P.N. Ramesu', 'contact': '9688079880'},
                    {'name': 'Pradeep Kumar T.', 'contact': '9095416226'},
                    {'name': 'TAMIL SELVAN A', 'contact': '8489677227'},
                    {'name': 'Veeramanikandan', 'contact': '0916728060'},
                    {'name': 'G.poomanikandan', 'contact': '9976407288'},
                    {'name': 'mathivanan', 'contact': '9080444343'},
                    {'name': 'Suresh', 'contact': '9894664354'},
                    {'name': 'jagan', 'contact': '9629186778'},
                    {'name': 'Dhayanithi', 'contact': '8072025450'},
                    {'name': 'Mahendran K', 'contact': '9600909211'},
                    {'name': 'Ravikumar.G', 'contact': '9500887215'},
                    {'name': 'Boopathi Raj R', 'contact': '9894655565'},
                    {'name': 'Rajkumar P', 'contact': '9095518805'},
                    {'name': 'thiruvenkadam', 'contact': '9524243784'},
                    {'name': 'J.Balaji', 'contact': '7904313572'},
                    {'name': 'MAGAAN T', 'contact': '9042737968'},
                    {'name': 'R.DHARMALINGAM', 'contact': '8778603993'},
                    {'name': 'kajendran', 'contact': '9786115251'},
                    {'name': 'KATHIRESH.K.N', 'contact': '9361719790'},
                    {'name': 'Logesh kumar', 'contact': '7904747089'},
                    {'name': 'Ganapathy', 'contact': '8526618104'},
                    {'name': 'abitha selva nayagi', 'contact': '8946017153'},
                    {'name': 'P.manikandan', 'contact': '9842547870'},
                    {'name': 'Bharath', 'contact': '9361365115'},
                    {'name': 'G.Balaji', 'contact': '9994048570'},
                    {'name': 'Sivakumar', 'contact': '6383575264'},
                    {'name': 'Kandavel Marusamy', 'contact': '9448852633'},
                    {'name': 'Rajendran', 'contact': '9488926836'},
                    {'name': 'jeeva', 'contact': '7845744557'},
                    {'name': 'PRAVEEN', 'contact': '9677771361'},
                    {'name': 'saieswaran', 'contact': '9003709520'},
                    {'name': 'Muthu Kumar', 'contact': '9791928006'},
                    {'name': 'Prasanth raj', 'contact': '9789159629'},
                    {'name': 'SathishRangasamy', 'contact': '7010996865'},
                    {'name': 'Gobinath GR', 'contact': '9843903202'},
                    {'name': 'JAGANATHAN', 'contact': '8903877088'},
                    {'name': 'Akilesh', 'contact': '6383447819'},
                    {'name': 'Karuppusamy.N', 'contact': '9578696160'},
                    {'name': 'Mohamad imthiyas', 'contact': '9865235413'},
                    {'name': 'Geetha', 'contact': '6382988838'},
                    {'name': 'B.Karthik', 'contact': '8344412805'},
                    {'name': 'P.Yuvaraj', 'contact': '9940878044'},
                    {'name': 'GOWTHAM S', 'contact': '8144279725'},
                    {'name': 'afser', 'contact': '7448494214'},
                    {'name': 'AJAIKARLMARX S', 'contact': '9445712346'},
                    {'name': 'muhammed imran', 'contact': '7708549994'},
                    {'name': 'Karthik', 'contact': '9894836406'},
                    {'name': 'parthipan', 'contact': '7894846338'}
                ]
            elif blood_type=='O-':
                donors=[
                    {'name': 'Manikandan R', 'contact': '9600672108'},
                    {'name': 'shiva kumar s', 'contact': '9791333143'},
                    {'name': 'R.vijayakumar', 'contact': '8438423137'},
                    {'name': 'Dr. Dinesh KK', 'contact': '9894232729'},
                    {'name': 'Rajesh s', 'contact': '9965559546'},
                    {'name': 'V. SIVAKUMAR', 'contact': '9698098021'},
                    {'name': 'GANESH S', 'contact': '9865303676'},
                    {'name': 'Palanisamy.C', 'contact': '6385501992'},
                    {'name': 'banumathi', 'contact': '6383358922'},
                    {'name': 'S.Dineshkumar', 'contact': '9443680336'},
                    {'name': 'venkades', 'contact': '9025733063'},
                    {'name': 'Ganeshamoorthi', 'contact': '9042785906'},
                    {'name': 'P Selvakumar', 'contact': '9843888832'},
                    {'name': 'ganesh', 'contact': '9865280127'},
                ]
            elif blood_type=='B+':
                donors=[
                    {'name': 'sureshkumar.R', 'contact': '9841516246'},
                    {'name': 'DHAMOTHARAN K', 'contact': '8248336121'},
                    {'name': 'P. Jayabal', 'contact': '9944769936'},
                    {'name': 'R.kaviyarasu', 'contact': '7539926799'},
                    {'name': 'Poomukilan S', 'contact': '8526965055'},
                    {'name': 'Siva Nandha perumalsamy', 'contact': '9566604008'},
                    {'name': 'pugalentheran', 'contact': '9500330937'},
                    {'name': 'Murugan Sabitha', 'contact': '7373150780'},
                    {'name': 'Shankar Dass', 'contact': '9865050700'},
                    {'name': 'Vaitheeswaran Thangavel', 'contact': '7904913439'},
                    {'name': 'sridhar', 'contact': '9384282659'},
                    {'name': 'Vishnu Vignesh', 'contact': '9087444999'},
                    {'name': 'M.SATHIYAMOORTHY', 'contact': '7373735365'},
                    {'name': 'Dhanasekar', 'contact': '9597226390'},
                    {'name': 'karthi', 'contact': '9688933975'},
                    {'name': 'MOHAMEDALI', 'contact': '9865263124'},
                    {'name': 'vasanth', 'contact': '9500584084'},
                    {'name': 'Raj devanand', 'contact': '9942250135'},
                    {'name': 'Jasper F', 'contact': '9025010342'},
                    {'name': 'Sathishkumar', 'contact': '6383604232'},
                    {'name': 'MANI L', 'contact': '8122803329'},
                    {'name': 'Gokul v p', 'contact': '9363336666'},
                    {'name': 'BOOPATHY A', 'contact': '9042995805'},
                    {'name': 'prakash', 'contact': '9655862731'},
                    {'name': 'Yoganathan S', 'contact': '9840633221'},
                    {'name': 'JEEVA', 'contact': '7200100888'},
                    {'name': 'Kavin s', 'contact': '9629289647'},
                    {'name': 'G.Sathish', 'contact': '9659476191'},
                    {'name': 'GIRIDHARAN', 'contact': '9965462632'},
                    {'name': 'Jeeva P', 'contact': '9384584152'},
                    {'name': 'Nithyanandhan', 'contact': '9976319976'},
                    {'name': 'Sam kishore', 'contact': '6380738008'},
                    {'name': 'Sivaganeshkumar. G. G', 'contact': '9994277462'},
                    {'name': 'Sasikumar', 'contact': '9629044432'},
                    {'name': 'K.KARUPPUSAMY', 'contact': '9443245754'},
                    {'name': 'J.K.Shathish', 'contact': '9500887917'},
                    {'name': 'THARANITHARAN', 'contact': '9629206625'},
                    {'name': 'Alavudeenbasha', 'contact': '9942154781'},
                    {'name': 'vignesh', 'contact': '8883823603'},
                    {'name': 'Aaron L Immac', 'contact': '9003388992'},
                    {'name': 'Sureshkannan', 'contact': '9585043819'},
                    {'name': 'Somasundharam s', 'contact': '9942406566'},
                    {'name': 'kathirvel.r', 'contact': '9865668055'},
                    {'name': 'M YUVARAJ LIC', 'contact': '9842683283'},
                    {'name': 'ELAVARASAN', 'contact': '8667600344'},
                    {'name': 'gobinath', 'contact': '9443385116'},
                    {'name': 'Dhanasekar k', 'contact': '9047374080'},
                    {'name': 'gopalakrishnan', 'contact': '9894583182'},
                    {'name': 'sathi', 'contact': '7373321589'},
                    {'name': 'Steephan amalraj j', 'contact': '9750592765'},
                    {'name': 'Mohamed musthafa G E', 'contact': '9943378638'},
                    {'name': 'thivyaprakash kurinji ambulance', 'contact': '9788808108'},
                    {'name': 'Nandhakumar', 'contact': '9043932624'},
                    {'name': 'Devarasu Sengottaiyan', 'contact': '9865018901'},
                    {'name': 'Thillainathan', 'contact': '9789475767'},
                    {'name': 'Balamugunthan Perumal', 'contact': '9790429486'},
                    {'name': 'Muthukumar', 'contact': '9791654788'},
                    {'name': 'ANGURAJ', 'contact': '6369272794'},
                    {'name': 'j muthuroopak', 'contact': '9952702323'},
                    {'name': 'ramesh', 'contact': '8754395895'},
                    {'name': 'Sridhar.N', 'contact': '9842924790'},
                    {'name': 'Shahul Hameed', 'contact': '9965012834'},
                    {'name': 'Gokulnath', 'contact': '7358907775'},
                    {'name': 'Prakash', 'contact': '9025732969'},
                    {'name': 'vairavel M', 'contact': '9976024683'},
                    {'name': 'senthilkumar.t', 'contact': '8610766776'},
                    {'name': 'Sekar', 'contact': '7603826700'},
                    {'name': 'iqbal', 'contact': '9080693994'},
                    {'name': 'yuvaraj kumar', 'contact': '9566601241'},
                    {'name': 'Mohankumar', 'contact': '9942587438'},
                    {'name': 'Ushan signaj', 'contact': '7092780908'},
                    {'name': 'sagul', 'contact': '9003690401'},
                    {'name': 'karthik', 'contact': '9095951119'},
                    {'name': 'sathya nishanth', 'contact': '9626576838'},
                    {'name': 'T.V.Arjunan', 'contact': '9894332446'},
                    {'name': 'AK Dinesh Kumar', 'contact': '7708047877'},
                    {'name': 'mohamedsafi', 'contact': '6382601923'},
                    {'name': 'Sivakumar S T', 'contact': '9788007747'},
                    {'name': 'Muthuvel', 'contact': '9345658789'},
                    {'name': 'SATHISH KUMAR.S', 'contact': '9791634456'},
                    {'name': 'Kumar GOBI ARTS', 'contact': '9688503427'},
                    {'name': 'Sumathi', 'contact': '9894723032'},
                    {'name': 'v.gunasekaran', 'contact': '9488029893'},
                    {'name': 'A.KARTHIKEYAN', 'contact': '9442881833'},
                    {'name': 'GKRAMESHKUMAR', 'contact': '9842399339'},
                    {'name': 'G.A.Gowtham', 'contact': '9791802236'},
                    {'name': 'P.Magudeswaran', 'contact': '9698571748'},
                    {'name': 'A.vijay', 'contact': '9488414505'},
                    {'name': 'murugan', 'contact': '7373150780'},
                    {'name': 'dhanasekaran', 'contact': '7708161673'},
                    {'name': 'Suresh', 'contact': '9585966703'},
                    {'name': 'T. Venkatachalapathi', 'contact': '9025111163'},
                    {'name': 'karthik', 'contact': '8883110181'},
                    {'name': 'kathiresan', 'contact': '8892348048'},
                    {'name': 'PRASANTH KUMAR S', 'contact': '8344537053'},
                    {'name': 'Muniappan', 'contact': '9994820184'},
                    {'name': 'sasitharan', 'contact': '9698896946'},
                    {'name': 'PP.GOVINDHARAJ', 'contact': '9444778869'},
                    {'name': 'Perumal samy.g', 'contact': '9994185681'},
                    {'name': 'Deepak M', 'contact': '9677788887'},
                    {'name': 'R.Pranesh babu', 'contact': '8667327391'},
                    {'name': 'Srinivasan', 'contact': '9677757585'},
                    {'name': 'nithyanantham.r', 'contact': '9842557288'},
                    {'name': 'Karthick Nanba KS', 'contact': '7812859662'},
                    {'name': 'Deepak Rahul. M', 'contact': '8903186558'},
                    {'name': 'Sasidharan', 'contact': '7402495345'},
                    {'name': 'Mohamed yaseen', 'contact': '9080522843'},
                    {'name': 'silambarasan', 'contact': '9952298585'},
                    {'name': 'n.s.saravanan', 'contact': '9443305197'},
                    {'name': 'C.Subramaniam', 'contact': '9360684264'},
                    {'name': 'kaviyarasan', 'contact': '7010328928'},
                    {'name': 'R Aishwarya', 'contact': '9597508726'},
                    {'name': 'Meganathan', 'contact': '9360582099'},
                    {'name': 'vijayakumar R', 'contact': '9865568688'},
                    {'name': 'palanisay sv', 'contact': '9715118877'},
                    {'name': 'Velmani', 'contact': '9345795727'},
                    {'name': 'ப. தமிழ்', 'contact': '8144386938'},
                    {'name': 'UDAY KUMAR', 'contact': '9492932306'},
                    {'name': 'ANGURAJ G', 'contact': '7373303800'},
                    {'name': 'velliangiri.R', 'contact': '8698000056'},
                    {'name': 'Prakash', 'contact': '9994969613'},
                    {'name': 'G. Aravintha raj', 'contact': '9944002827'},
                    {'name': 'Narendran', 'contact': '9789503638'},
                    {'name': 'Deepan Kumar S', 'contact': '7502394749'},
                    {'name': 'k senthilkumar', 'contact': '9894714764'},
                    {'name': 'Dhandabani.K', 'contact': '9600969449'},
                    {'name': 'P.Mathivanan', 'contact': '7708603603'},
                    {'name': 'P.VENUGOPAL', 'contact': '9842677695'},
                ]
            elif blood_type=='B-':
                donors=[
                        {'name': 'N.M.Niranjankumar', 'contact': '9843571768'},
                        {'name': 'Ramvignesh Karunakaran', 'contact': '9791335152'},
                        {'name': 'Muthukumar', 'contact': '9865294343'},
                        {'name': 'Uma maheswari. C', 'contact': '9952882392'},
                        {'name': 'Ashok', 'contact': '9384911907'},
                        {'name': 'Deepankumar', 'contact': '9578553699'},
                ]
            elif blood_type=='AB+':
                donors=[
                       {'name': 'gopalpalanisamy', 'contact': '9842704123'},
                        {'name': 'vignesh', 'contact': '9750464872'},
                        {'name': 'kathir vel', 'contact': '9994132496'},
                        {'name': 'GIRI PRASATH.M', 'contact': '9345824969'},
                        {'name': 'Balamurugan', 'contact': '9787475533'},
                        {'name': 'MURUGESH.P', 'contact': '9944941031'},
                        {'name': 'Kathirvel Kumar k', 'contact': '9360501112'},
                        {'name': 'S. R. saravanaraja', 'contact': '9578669463'},
                        {'name': 'gajendrasingh', 'contact': '8870027472'},
                        {'name': 'prabhu', 'contact': '9786262613'},
                        {'name': 'lokanathan.c', 'contact': '9500788208'},
                        {'name': 'GOKULPRASAN K P', 'contact': '9042448596'},
                        {'name': 'vignesh', 'contact': '8667659532'},
                        {'name': 'N S Naveen kumar', 'contact': '8825526262'},
                        {'name': 'lokanathan.c', 'contact': '9500788208'},
                        {'name': 'Navaneeth. T', 'contact': '9344853032'},
                        {'name': 'sekarbana', 'contact': '8838574535'},
                        {'name': 'ArunkumarM', 'contact': '9488561841'},
                        {'name': 'Surendiran', 'contact': '9944172503'},
                        {'name': 'Naveenkumar', 'contact': '9095510949'},
                        {'name': 'santhosh kumar v', 'contact': '8667646381'},
                        
                ]
            elif blood_type=='AB-':
                donors=[
                    {'name': 'Ragupathi C', 'contact': '9659526591'},
                    {'name': 'Suraj', 'contact': '9972524802'},
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
