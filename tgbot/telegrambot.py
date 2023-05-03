class Order:
    def __init__(self, name, price):
        self.name = name
        self.price = price

import telebot
from telebot import types
import psycopg2

bot = telebot.TeleBot('5846296226:AAHfoUin9OgitRzZtL2RIC11_2nOB2ot5mY')
ordering = list()
price = 0
b = 0
connection = psycopg2.connect(
        host = "localhost",
        user = "postgres",
        password = "admin",
        database = "pp2"
    )

connection.autocommit = True

# первые кнопки
keyboard = types.InlineKeyboardMarkup() 
burger = types.InlineKeyboardButton(text="Бургеры", callback_data="burgers")
keyboard.add(burger)
drink = types.InlineKeyboardButton(text="Напитки", callback_data="drinks")
keyboard.add(drink)
combo = types.InlineKeyboardButton(text="Комбо", callback_data="combos")
keyboard.add(combo)

# вторые кнопки
burgers = types.InlineKeyboardMarkup()
gamb = types.InlineKeyboardButton(text="Гамбургер", callback_data="gamb")
burgers.add(gamb)
cheese = types.InlineKeyboardButton(text="Чизбургер", callback_data="cheese")
burgers.add(cheese)
chicken = types.InlineKeyboardButton(text="Чикенбургер", callback_data="chicken")
burgers.add(chicken)

#третьи кнопки
drinks = types.InlineKeyboardMarkup()
cola = types.InlineKeyboardButton(text="Кока-кола", callback_data="cola")
drinks.add(cola)
fanta = types.InlineKeyboardButton(text="Фанта", callback_data="fanta")
drinks.add(fanta)
sprite = types.InlineKeyboardButton(text="Спрайт", callback_data="sprite")
drinks.add(sprite)

#четвертые кнопки
combos = types.InlineKeyboardMarkup()
combo1 = types.InlineKeyboardButton(text="Первое комбо(Макчикен)", callback_data="combo1")
combos.add(combo1)
combo2 = types.InlineKeyboardButton(text="Второе комбо(Роял чизбургер)", callback_data="combo2")
combos.add(combo2)
combo3 = types.InlineKeyboardButton(text="Третье комбо(Биг мак)", callback_data="combo3")
combos.add(combo3)

#кнопки возврата
ret = types.InlineKeyboardMarkup()
ykey = types.InlineKeyboardButton(text="Да", callback_data="yes")
ret.add(ykey)
nkey = types.InlineKeyboardButton(text="Нет", callback_data="no")
ret.add(nkey)

#удаление товара
delete = types.InlineKeyboardMarkup()
yes = types.InlineKeyboardButton(text="Да", callback_data='y')
delete.add(yes)
no = types.InlineKeyboardButton(text="Нет", callback_data='n')
delete.add(no)





@bot.message_handler(commands=['start'])
def start_message(message):
    mycursor = connection.cursor()
    sql = "SELECT * FROM translator WHERE id = %s"
    adr = (str(message.from_user.id),)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    print(myresult)
    if myresult is None or myresult == [] or myresult == ():
        mycursor = connection.cursor()
        sql = "INSERT INTO translator (id) VALUES (%s)"
        val = (str(message.from_user.id))
        mycursor.execute(sql, val)
        bot.send_message(message.from_user.id, "Registred")
    else:
        bot.send_message(message.from_user.id, "You have already register in bot")

    bot.send_message(message.from_user.id,
                     "Добрый вечер! Вас приветствует сеть ресторанов быстрого питания: Mcdonalds" + "\n"
                                                                                                    "Что хотите заказать?",
                     reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def mesag(message):
    global b
    if b >= 1:
        ordering.pop(int(message.text) - 1)
        for i in range(len(ordering)):
            bot.send_message(message.from_user.id,
                             str(i + 1) + "." + ordering[i].name + ". Цена:  " + str(ordering[i].price) + 'тг.')
        bot.send_message(message.from_user.id, "Хотите еще удалить?", reply_markup=delete)


@bot.callback_query_handler(func=lambda call: True)
def orders(call):
    global price, b
    if call.data == "burgers":
        bot.send_photo(call.message.chat.id, 'https://mcdonalds.kz/storage/2499/c9c3bab8dc4ffaef7cfe6954306b90f79dddfd72.png')
        bot.send_photo(call.message.chat.id, 'https://mcdonalds.kz/storage/2500/84a1faa6bd4b2721096a9d777b0f575cd490505b.png')
        bot.send_photo(call.message.chat.id, 'https://mcdonalds.kz/storage/2501/1aea60db5a4ae151271e260a4c0c11b083c95cf8.png')
        bot.send_message(call.message.chat.id, "Какой бургер будете?"+'\n'
                                               "1.Гамбургер. Цена: 600тг"+'\n'
                                                "2.Чизбургер. Цена: 650тг"+'\n'
                                                                       "3.Чикенбургер. Цена: 550тг", reply_markup=burgers)
    elif call.data == "gamb":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2499/c9c3bab8dc4ffaef7cfe6954306b90f79dddfd72.png')
        bot.send_message(call.message.chat.id, "Вы выбрали гамбургер. Цена: 600 тг" + "\n" + "Хотите еще что-нибудь заказать?", reply_markup=ret)
        price += 600
        order = Order("Гамбургер", 600)
        ordering.append(order)
    elif call.data == "cheese":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2500/84a1faa6bd4b2721096a9d777b0f575cd490505b.png')
        bot.send_message(call.message.chat.id, "Вы выбрали чизбургер. Цена: 650 тг" + "\n" + "Хотите еще что-нибудь заказать?", reply_markup=ret)
        price += 650
        order = Order("Чизбургер", 650)
        ordering.append(order)
    elif call.data == "chicken":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2501/1aea60db5a4ae151271e260a4c0c11b083c95cf8.png')
        bot.send_message(call.message.chat.id, "Вы выбрали чикенбургер. Цена: 550тг" + "\n" + "Хотите еще что-нибудь заказать?", reply_markup=ret)
        price += 550
        order = Order("Чикенбургер", 550)
        ordering.append(order)
    elif call.data == "drinks":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2310/fb9219ca21fe7bcd05336afbbd7ffb46676572aa.png')
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2311/b0748c744d20976f14db0bc88d796e17de874e39.png')
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2312/36cde0ab73772f81acd95700ae17b957debbaac4.png')
        bot.send_message(call.message.chat.id, "Какой напиток хотите выбрать?"+'\n'
                                               "1.Кока-кола. Цена:300тг"+'\n'
                                                "2.Фанта. Цена: 300тг"+'\n'
                                                                       "3.Спрайт. Цена: 300тг", reply_markup=drinks)
    elif call.data == "cola":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2310/fb9219ca21fe7bcd05336afbbd7ffb46676572aa.png')
        bot.send_message(call.message.chat.id, "Вы выбрали Кока-колу. Цена: 300 тг" + "\n" + "Хотите еще что-нибудь заказать?", reply_markup=ret)
        price += 300
        order = Order("Кола", 300)
        ordering.append(order)
    elif call.data == "fanta":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2311/b0748c744d20976f14db0bc88d796e17de874e39.png')
        bot.send_message(call.message.chat.id, "Вы выбрали Фанту. Цена: 300 тг" + "\n" + "Хотите еще что-нибудь заказать?", reply_markup=ret)
        price += 300
        order = Order("Фанта", 300)
        ordering.append(order)
    elif call.data == "sprite":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2312/36cde0ab73772f81acd95700ae17b957debbaac4.png')
        bot.send_message(call.message.chat.id, "Вы выбрали Спрайт. Цена: 300тг" + "\n" + "Хотите еще что-нибудь заказать?", reply_markup=ret)
        price += 300
        order = Order("Спрайт", 300)
        ordering.append(order)
    elif call.data == "combos":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2516/da141df1378dc814686593419c679a10f4ed1e0e.png')
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2527/8265c89e6311255ac399bd264febafbe3bd9e55a.png')
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2512/817f2be52e9f284e57a8a10a958c4d529861b237.png')
        bot.send_message(call.message.chat.id, "Какое комбо хотите выбрать?"+'\n'
                                               "1.Макчикен. Цена: 1950тг"+'\n'
                                                "2.Рояль Чизбургер. Цена: 1950тг"+'\n'
                                                                       "3.Биг Мак. Цена: 1950тг", reply_markup=combos)
    elif call.data == "combo1":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2516/da141df1378dc814686593419c679a10f4ed1e0e.png')
        bot.send_message(call.message.chat.id, "Вы выбрали Макчикен. Цена: 1950 тг" + "\n" + "Хотите еще что-нибудь заказать?", reply_markup=ret)
        price += 1950
        order = Order("Макчикен", 1950)
        ordering.append(order)
    elif call.data == "combo2":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2527/8265c89e6311255ac399bd264febafbe3bd9e55a.png')
        bot.send_message(call.message.chat.id, "Вы выбрали Роял Чизбургер. Цена: 1950 тг" + "\n" + "Хотите еще что-нибудь заказать?", reply_markup=ret)
        price += 1950
        order = Order("Роял Чизбургер", 1950)
        ordering.append(order)
    elif call.data == "combo3":
        bot.send_photo(call.message.chat.id,
                       'https://mcdonalds.kz/storage/2512/817f2be52e9f284e57a8a10a958c4d529861b237.png')
        bot.send_message(call.message.chat.id, "Вы выбрали Биг Мак. Цена: 1950тг" + "\n" + "Хотите еще что-нибудь заказать?", reply_markup=ret)
        price += 1950
        order = Order("Биг Мак", 1950)
        ordering.append(order)
    elif call.data == "yes":
        bot.send_message(call.message.chat.id, "Что закажете?", reply_markup=keyboard)
    elif call.data == "no":
        for i in range(len(ordering)):
            bot.send_message(call.message.chat.id, str(i + 1)+"."+ordering[i].name+". Цена:  "+str(ordering[i].price)+'тг.')
        bot.send_message(call.message.chat.id, "Стоимость вашего заказа: " + str(price) + 'тг.'+'\n'
                                                                                                'Хотите что-то удалить?', reply_markup=delete)
    elif call.data == 'y':
        bot.send_message(call.message.chat.id, "Напишите номер товара, который вы хотите удалить из заказа")
        b += 1
    elif call.data == 'n':
        for i in range(len(ordering)):
            bot.send_message(call.message.chat.id,
                         str(i + 1) + "." + ordering[i].name + ". Цена:  " + str(ordering[i].price) + 'тг.')
        ordering.clear()
        
        bot.send_message(call.message.chat.id, "Стоимость вашего заказа: " + str(price) + 'тг.')


bot.polling()