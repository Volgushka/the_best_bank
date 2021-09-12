import random
import csv

NUMBERS = []
MONEY = []
CVV = []
STATUS = []
HISTORY = []

def hi():
    print('Вас приветствует "The Best Bank". Мобильное приложение версия №2')

def klientRegistration():
while True:
    fio = input("Введите ваше ФИО: ")
    name = input("Как вы предпочитаете, чтобы к вам обращались? ")
    tel = input(f"Введите номер телефона, {name}: " )
    if tel[:4] == "+375" and len(tel) == 13 and tel[1:].isdigit():
        break
    print('Вы ошиблись. Номер телефона начинается с +375 и содержит 13 цифр. Введите корректные значения.')
while True:
    mail = input("Введите электронную почту: ")
    if '@' in mail:
        if '.' in mail[mail.index('@'):]:
            break
    print('Вы ошиблись. Такого почтового адреса не существует. Введите корректные значения.')
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
     
print("Writing complete")
print(f'Спасибо, {name}, регистрация прошла успешно'. )

def cardAdd():
    while True:
        number = input("Введите номер новой карты: ")
        if len(number) == 16 and number.isdigit():
            NUMBERS.append(number)
            MONEY.append(0)
            break
        else:
            print('Вы ошиблись.Введите корректные значения.')
    while True:
        cvv = random.randint(100, 999)
        if cvv not in CVV:
            CVV.append(cvv)
            break
    STATUS.append('Разблокирована')
    print(f'Уважаемый(я) {n}, карта {number} добавлена в ваш кошелек.')

def money_transfer()
     while True:
            if NUMBERS:
                print("Номер\t\t\t Деньги\t CVV\t Статус")
                for number in enumerate(NUMBERS):
                    print(number[0]+1, number[1], str(MONEY[number[0]]) + " $\t", CVV[number[0]], STATUS[number[0]])
                ch = input('Сделайте выбор: перевод между своими (21) или перевод на чужую карточку(22): ')
                if ch == '21':
                    number_send = input("С какой карты вы бы хотели сделать перевод? Ваш выбор: ")
                    if number_send not in NUMBERS:
                        print('Такой карточки не существует')
                    else:
                        number_receiver = input('Введите номер карточки для зачисления средств: ')
                        if number_receiver in NUMBERS:
                            money = input("Введите сумму перевода: ")
                            MONEY[NUMBERS.index(number_receiver)] += int(money)
                            MONEY[NUMBERS.index(number_send)] -= int(money)
                            HISTORY.append([number_receiver, "Получен перевод на " + str(money)])
                            HISTORY.append([number_send, "Получен перевод на " + str(money)])
                        else:
                            print('Такой карточки не существует')
                elif ch == '22':
                    number_send = input("С какой карты вы бы хотели сделать перевод? Ваш выбор: ")
                    if number_send not in NUMBERS :
                        print('Такой карточки не существует')
                    else :
                        number_receiver = input('Введите номер карточки для зачисления средств: ')
                        if number_receiver not in NUMBERS :
                            money = input("Введите сумму перевода: ")
                            MONEY[NUMBERS.index(number_send)] -= int(money)
                            HISTORY.append([number_send, "Получен перевод на " + str(money)])
                        else:
                            print('Это ваша карточка. Выберите другую.')    
def money_reception() 
    if NUMBERS:
       print("Номер\t\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[0]+1, number[1], str(MONEY[number[0]]) + " $\t", CVV[number[0]], STATUS[number[0]])
            print("На какую карту вы бы хотели получить перевод? ")
            number = int(input("Ваш выбор: "))
            money = int(input("Сколько денег вы хотите получить: "))
            HISTORY.append([NUMBERS[number-1], "Получен перевод на "+str(money)])
            MONEY[number-1] += money
        else:
            print("У вас пока нет карточек")

def payments():

def cardBlocking():
    if NUMBERS:
        print("Номер\t\t\t Деньги\t CVV\t Статус")
        for number in enumerate(NUMBERS):
            print(number[1], str(MONEY[number[0]])+" $\t", CVV[number[0]], STATUS[number[0]])
            number_zr = input("Какую карточку вы хотите заблокировать/разблокировать: ")
            if STATUS[STATUS.index(number_zr)] == "Разблокирована":
                STATUS[STATUS.index(number_zr)] = "Заблокирована"
            else:
                STATUS[STATUS.index(number_zr)] = "Разблокирована"
        else:
            print("У вас пока нет карточек")
            
def cardsList():
    print("Номер\t\t\t Деньги\t CVV\t Статус")
        for number in enumerate(NUMBERS):
            print(number[1], str(MONEY[number[0]])+" $\t", CVV[number[0]], STATUS[number[0]])
        else:
            print("В настоящее время в кошельке нет карточек.")
            
def cardStory():
    if NUMBERS:
        print("Номер\t\t\t Деньги\t CVV\t Статус")
        for number in enumerate(NUMBERS):
            print(number[0] + 1, number[1], str(MONEY[number[0]]) + " $\t", CVV[number[0]], STATUS[number[0]])
            number_v = input("Историю какой карты вы бы хотели посмотреть?Ваш выбор: ")
            for story in HISTORY:
                if story == NUMBERS[NUMBERS.index(number_v)]:
                    print(story)
        else:
            print("У вас пока не карточек")
def exit():
    print("До свидания")
        break
def transactions():
while True:
    print(
        "Меню:\n1 - Добавить новую карту\n2 - Перевод на карту\n3 - Принять перевод\n4 - Платежи\n5 - Заблокировать карту")
    print("6 - Вывести все карты\n7 - Посмотреть историю карты\n0 - Выйти ")
    choice = input("Сделайте ваш выбор: ")
    if choice == "1":
        cardAdd()      
    elif choice == "2":
        money_transfer()
    elif choice == "3":
        money_reception()
    elif choice == "4":
        payments()
    elif choice == "5":
        card_blocking()
    elif choice == "6":
       cardsList()
    elif choice == "7":
       cardStory()
    elif choice == "0":
        exit()
    else:
        print("Неправильный ввод")

hi()
klientRegistration()
cardAdd()
transactions()