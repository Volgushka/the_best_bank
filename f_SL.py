import csv
import os
import random

#  with open('user.csv', 'a', encoding='utf-8') as f:
# #     f_writer = csv.writer(f, delimiter=";")
# #     if os.stat('user.csv').st_size == 0:
# #         f_writer.writerow(["id", "ФИО", "Почта", "Телефон"])
# #     id = random.randint(1000, 10000)
# #     f_writer.writerow([id, fio, mail, phone])
#
# with open('user.csv', 'r', encoding='utf-8') as f:
#     f_reader = csv.DictReader(f, delimiter=";")
#     for line in f_reader:
#         if "Анжелика" in line["ФИО"]:
#             print(line)
#
# def record(path, header, data, mode='a'):
#     print("Привет")
#     with open(path, mode, encoding='utf-8') as f:
#         f_writer = csv.writer(f, delimiter=";")
#         if os.stat(path).st_size == 0:
#             f_writer.writerow(header)
#         f_writer.writerow(data)

# def look(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         f_reader = csv.reader(f, delimiter=";")
#         for line in f_reader:
#             print(line)

# def look_1(path, i):
#     with open(path, 'r', encoding='utf-8') as f:
#         f_reader = csv.reader(f, delimiter=";")
#         for line in f_reader:
#             if i in line:
#                  return line



        # 1) Сделайте так, чтобы функция чтения данных в файле возвращало вам словарик
        # такого типа:
        # {1234 : {"ФИО" : "Артур", "Почта" : "mail.ru", "Телефон" : "+375"}, ...}
        # 2) Прописать функцию обновления файла, чтобы можно было отредактировать какую - то
        # отдельную запись, не повредив другие

# def csv_reading(path):
#     with open(path, 'r', encoding='utf-8') as m:
#         reader = csv.DictReader(m, delimiter=";")
#         for i in reader:
#             i = {i['ID']:i}
#             print(i)
#
# csv_reading('klients.csv')

def csv_updater(path):
    with open(path,encoding='utf-8') as file :
        readData = [i for i in csv.DictReader(file, delimiter=";")]
#        readData[][]  как то поменять


csv_updater('klients.csv')


print(couples)

def csv_reading(path):
    with open(path, 'r', encoding='utf-8') as m:
        reader = csv.DictReader(m, delimiter=";")
        for i in reader:
            i = {i['ID']:i}
            print(i)

csv_reading('klients.csv')