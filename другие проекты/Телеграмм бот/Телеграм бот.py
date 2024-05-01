import telebot
from telebot import  types

bot = telebot.TeleBot('7084808510:AAHM4DdQ379aeC_N7-oUmU8Bv9yQDVhBiow')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
    btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
    btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
    btn4 = types.KeyboardButton("🤖 Дополнительные функции бота 🤖")
    btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
    btn6 = types.KeyboardButton('✅ Вы в меню ✅')
    markup.add(btn1)
    markup.add(btn2, btn3)
    markup.add(btn4)
    markup.add(btn5, btn6)
    bot.send_message(message.from_user.id, "Здравствуйте! Рад,что вы это читаете. Я создал этот бот, чтоб вам было удобней найти всё, что вам понадобится обо мне", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '🤡 Обо мне 🤡':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("✅ Вы здесь ✅")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn4 = types.KeyboardButton("🤖 Дополнительные функции бота 🤖")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, 'раздел: "обо мне":\n \n👍🏻 Хороший выбор\n \n📲', reply_markup=markup, parse_mode='Markdown')


    elif message.text == '🤯 Как готовился 🤯':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("✅ Вы здесь ✅")
        btn4 = types.KeyboardButton("🤖 Дополнительные функции бота 🤖")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, 'раздел: Как готовился\n \n самообучение програмированию это сложно поэтому путь был тернист:\n поглащал видеокурсы \n📲', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '👨‍💻 Мои проекты 😎':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn4 = types.KeyboardButton("🤖 Дополнительные функции бота 🤖")
        btn5 = types.KeyboardButton("✅ Вы здесь ✅")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, 'раздел: Мои проекты\n \n👍🏻 Хороший выбор\n \n📲 ', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🤔 Почему я должен вас нанять? 😑':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("✅ Вы здесь ✅")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn4 = types.KeyboardButton("🤖 Дополнительные функции бота 🤖")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, 'раздел:Почему я должен вас нанять?\n \n👍🏻 Хороший выбор\n \n📲 ', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🤖 Дополнительные функции бота 🤖':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn4 = types.KeyboardButton("✅ Вы здесь ✅")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, 'раздел: Дополнительные функции бота\n \n👍🏻 Хороший выбор\n \n📲 ', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔙 Главное меню 🔙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn4 = types.KeyboardButton("🤖 Дополнительные функции бота 🤖")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('✅ Вы в меню ✅')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, "👀 Выбери интересующий раздел", reply_markup=markup)



bot.polling(none_stop=True, interval=0)
