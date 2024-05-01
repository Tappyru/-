'''
Как тут всё работает:
1)Вы вводите пароль
2)происходит перебор паролей до момента пока не найдётся нужный
'''


#вводится пароль который нужно угадать:
password_real = input('Введите пароль:')

#если нужена кирилица:
#cyrillic_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#cyrillic_letters = cyrillic_lower_letters + cyrillic_lower_letters.upper()

#  или characters = string.printable чтоб добавить всё это:
guess_password_set = string.digits + string.ascii_letters + string.punctuation #добавляем цифры, англ. буквы и знаки:
guess_password_length = len(password_real) #узнаём длину пароля


def string_iter(string, length): #создаём функцию с генератором
    yield from itertools.product(*([string] * length))


while True:
    for password_set in string_iter(guess_password_set, guess_password_length):
        password_string = ''.join(password_set) #"перебираем энное число значений из "списка" и объединяем их в одну строку
        print(password_string)
        if password_string == password_real: #сравниваем полученную строку и нужный пароль
            print('Ваш пароль: ', password_string)
            exit()