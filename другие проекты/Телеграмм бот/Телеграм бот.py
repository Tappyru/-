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
    bot.send_message(message.from_user.id, "Здравствуйте! Рад,что вы это читаете. Я создал этот бот, чтобы вам было удобней найти всё, что вам понадобится обо мне", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '🤡 Обо мне 🤡':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("✅ Вы здесь ✅")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn4 = types.KeyboardButton("Зачем тебе мы?")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_photo(message.chat.id, 'https://sun9-4.userapi.com/impg/lxM1kIkiLXu1Xh9-UbBeKoTyiKKycsqm1M4xkw/8F_y5kljbUA.jpg?size=572x997&quality=96&sign=ef0410255ad2d01a9dce9a40be0d518e&type=album')
        bot.send_message(message.from_user.id, 'Работаю с 13, стремлюсь к тому чтобы найти свою нишу и стать в ней успешным "дядькой". \n'
                                               'Самый большой страх: показаться некомпетентным. \n '
                                               'Хочу добиться многого, чтобы не разочароваться в себе и не получить кризис среднего возраста.'
                                               '', reply_markup=markup, parse_mode='Markdown')


    elif message.text == '🤯 Как готовился 🤯':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("✅ Вы здесь ✅")
        btn4 = types.KeyboardButton("Зачем тебе мы?")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, 'Самообучение програмированию это сложно поэтому путь был тернист:\n \nбыли пройдены курсы на сайте Stepik и, конечно, Youtube  \n \nГлавная проблема это - осутствие конкретной "дорожной карты", а ведущие, говоря об одном и том же языке програмирования, противоречат друг другу, из за чего так же тратится много времени на сомнения, перечитку одного и того же разными словами. \n' '\n*Именно поэтому я хочу устроиться хоть на позицию стажёра, лишь бы получить доступ к образовательной платформе МТС!*', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '👨‍💻 Мои проекты 😎':
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn4 = types.KeyboardButton("Зачем тебе мы?")
        btn5 = types.KeyboardButton("✅ Вы здесь ✅")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
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
        btn4 = types.KeyboardButton("Зачем тебе мы?")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('🔙 Главное меню 🔙')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, 'И так...\n"Почему я должен вас нанять?"\n'
                                               ' \nЕсли кратко:\nБуду работать и учиться на убой, чтобы достичь желаемого уровня, дайте лишь возможность и у кого спросить источник.\n'
                                               ' \nНе кратко:\n Я устал работать на неофициальных работах со сдельной оплатой, но цель:"стать обеспеченным, авторитетным специалистом/начальником", осталась.\n'
                                               'Поэтому,взяв меня, вы получите: благодарный, потенциально дорогой кадр, который останется в компании на долго. \n ', reply_markup=markup, parse_mode='Markdown')

    elif message.text == "Зачем тебе мы?":
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
        bot.send_message(message.from_user.id, 'Если о работе то:\n Я просто хочу иметь чёткий план того, что и как мне учить. Эта информация различается от компапнии к компании, не говоря уже о курсах на Ютуб.\n'
                                               '\nЕсли нет то: \nОтносительно недавно, я взял ответственность за свою жизнь в свои руки и,попробовав '                                               'разные сферы и должности, в том числе - работу на себя,понял, что хочу просто хорошую работу, с хорошей зарплатой и мед страховкой, чтоб вылечить последствия трудоголизма😅. хочу развиваться,заниматься спортом, возможность продвигаться по карьерной лестнице, чтоб не работая 7/0 обеспечивать семью и своих прекрасных котов. \n \n'                                               'А вот и они:\n \n ', reply_markup=markup, parse_mode='Markdown')
        bot.send_photo(message.chat.id,
                       'https://sun9-78.userapi.com/impg/-vGsX2Jn2T0SqqfxlQcwSuTR9E-o1-wUfhpYAg/ckufONkjMBc.jpg?size=825x825&quality=95&sign=a20fdb4f361b9c576cbd8aa129699230&type=album')
        bot.send_photo(message.chat.id,
                       'https://sun9-55.userapi.com/impg/NvoeH8xfqIIyGMdIad_RRFC3XbkmPZrtA2i8lw/gmLSOiP0XSc.jpg?size=810x1080&quality=95&sign=5fdd9d36555c7c8f7faf690ecc3fbaa7&type=album')
        bot.send_photo(message.chat.id,
                       'https://sun9-73.userapi.com/impg/RlmQ9q9ZOh86GFkgJFAPkIjFUFy3iJuOGuDjnw/zZhWFav6HqA.jpg?size=808x1080&quality=95&sign=d0b0710ddf5fd10813a73bbff0b58203&type=album')
        bot.send_photo(message.chat.id,
                       'https://sun9-1.userapi.com/impg/pUWTk6MRrEIkWYtd9kvgrk2FbA-SitT4PrjuEA/DHvEbH-3abg.jpg?size=810x1080&quality=95&sign=6c1d973d600a93ab04e0278402ca3ed2&type=album')
        bot.send_message(message.from_user.id, "Да! Вы всё верно поняли- это непрекрытое давление на жалость.🙃", reply_markup=markup)


    elif message.text == '🔙 Главное меню 🔙':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤔 Почему я должен вас нанять? 😑")
        btn2 = types.KeyboardButton("🤡 Обо мне 🤡")
        btn3 = types.KeyboardButton("🤯 Как готовился 🤯")
        btn4 = types.KeyboardButton("Зачем тебе мы?")
        btn5 = types.KeyboardButton("👨‍💻 Мои проекты 😎")
        btn6 = types.KeyboardButton('✅ Вы в меню ✅')
        markup.add(btn1)
        markup.add(btn2, btn3)
        markup.add(btn4)
        markup.add(btn5, btn6)
        bot.send_message(message.from_user.id, "👀 Выберите интересующий раздел", reply_markup=markup)



bot.polling(none_stop=True, interval=0)
