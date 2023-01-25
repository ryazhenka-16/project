import string
import pyhibp
from time import sleep
from pyhibp import pwnedpasswords as pw

def generator():
    alphabet = string.ascii_lowercase + string.ascii_uppercase + "0123456789" + "~!@#$%^&*?-=_+"
    symbols = "~!@#$%^&*?"
    while True:
        password = ""
        for i in range(8):
            password += alphabet[random.randint(0, len(alphabet) - 1)]
        for symbol in symbols:
            if symbol in password:
                return password
            else:
                continue

def HIBP_checker(password):
    pyhibp.set_user_agent(ua="Awesome application/0.0.1 (An awesome description)")
    resp = pw.is_password_breached(password=password)
    if resp:
        message = "Этот пароль есть в утечке {0} раз(а)".format(resp)
        return message
    else:
        return True


print("Вас приведствует программа по защите Вас от мошенников в интернете")
sleep(1)
print("Чтобы проверить свой пароль, вам нужо вести его в необходимое поле")
sleep(1)
print("дальше программа сделает все за вас, пользуйтесь;)")
sleep(1)
print("        Проверка пароля         ")
PASSWORD = input("Введите Ваш пароль для проверки " + "\n")

if HIBP_checker(PASSWORD) == True:
    print("Все ОК")
else:
    print(HIBP_checker(PASSWORD))
    answer = input("Создать новый пароль? (да/нет) ").lower()
    if answer == "да":
        while True:
            new_password = generator()
            if HIBP_checker(new_password) == True:
                print(new_password)
                break
    else:
        print("Хорошо!")
    writer = input("Желаете записать пароль с почтой в памятку?  (да/нет) ").lower()
    if writer == "да":
        file_name = input("Как Вы хотите назвать свою памятку? ( если памятка ежу есть, запишите ее название ) ")
        with open(file_name + ".txt", 'a') as opened_file:
            service = input("В каком сервесе вы хотите использовать ваш пароль? (VK/Diskord/Ok/Почта/Telegram/Wathsapp/Viber/Twiter) ").lower()
            if service == "VK" or "Diskord" or "Ok" or "Почта" or "Twiter" or "Telegram" or "Wathsapp" or "Viber":
                login_service_1 = input("Введите свою почту или номер телефона от " + service + '\n')
                opened_file.write(service)
                opened_file.write("     ")
                opened_file.write(login_service_1)
                opened_file.write("     ")
                if answer == "да":
                    opened_file.write(new_password + "\n" + "\n")
                else:
                    opened_file.write(PASSWORD + "\n" + "\n")
                print("Все Ваши данные от", service, "введены в", file_name)
                sleep(1)
                print("Cпасибо что воспользовались нашей программой")
                sleep(1)
                print("Приходите еще!")
            else:
                print("!ошибка!" + "\n" + "запустите программу снова")
    else:
        print("Счастливо!")





        # workbook = xlsxwriter.Workbook('sample_data4.xlsx')
# password_sheet = workbook.add_worksheet()
# for i in range(1, 10000):
#     password_sheet.write('A' + str(i), generator())
# workbook.close()

