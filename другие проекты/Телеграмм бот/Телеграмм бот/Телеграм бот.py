import telebot
import wikipedia
from telebot import types

bot = telebot.TeleBot('7084808510:AAHM4DdQ379aeC_N7-oUmU8Bv9yQDVhBiow')

wikipedia.set_lang("ru")

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
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn5, btn6)
        bot.send_photo(message.chat.id, 'https://sun9-4.userapi.com/impg/lxM1kIkiLXu1Xh9-UbBeKoTyiKKycsqm1M4xkw/8F_y5kljbUA.jpg?size=572x997&quality=96&sign=ef0410255ad2d01a9dce9a40be0d518e&type=album')
        bot.send_message(message.from_user.id, 'Работаю с 13, стремлюсь к тому чтоб найти свою нишу и стать в ней успешным "дядькой". \n'
                                               'Самый большой страх: показаться некомпетентным. \n '
                                               'Хочу добиться много, чтоб не разочароваться в себе и не получить кризис среднего возраста.'
                                               '', reply_markup=markup, parse_mode='Markdown')


    elif message.text == '🤯 Как готовился 🤯':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("✅ Вы здесь ✅")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, 'раздел: Как готовился\n \n самообучение програмированию это сложно поэтому путь был тернист:\n поглащал видеокурсы \n📲', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '👨‍💻 Мои проекты 😎':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn5 = types.KeyboardButton("✅ Вы здесь ✅")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn5, btn6)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn7 = types.InlineKeyboardButton(text='МОИ ПРОЕКТЫ', url='https://github.com/Tappyru/-')
        kb.add(btn7)
        bot.send_message(message.from_user.id, 'ВАШЕМУ ВНИМАНИЮ ПРЕЕЕЕДСТАВЛЯЮ: ', reply_markup=kb, parse_mode='Markdown')

    elif message.text == '🤔 Почему я должен вас нанять? 😑':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("✅ Вы здесь ✅")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, 'И так...\n"Почему я должен вас нанять?"\n'
                                               ' \nЕсли кратко:\nБуду работать и учиться на убой, чтоб достичь желаемого уровня, дайте лишь возможность и у кого спросить источник.\n'
                                               ' \nНе кратко:\n Я устал работать на неофициальных работах со сдельной оплатой, но цель:"стать обеспеченным, авторитетным специалистом/начальником", осталась.\n'
                                               'Поэтому,взяв меня, вы получите: благодарный, потенциально дорогой кадр, который останется в компании на долго. \n ', reply_markup=markup, parse_mode='Markdown')


    elif message.text == '🔙 Главное меню 🔙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")

        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('✅ Вы в меню ✅')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, "👀 Выберите интересующий раздел", reply_markup=markup)



bot.polling(none_stop=True, interval=0)
