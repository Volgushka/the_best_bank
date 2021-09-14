# Два метода в классе, один принимает в себя либо строку,  либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или  равно длине слова, выводить все гласные, иначе согласные;  если число то, произведение суммы чётных цифр на длину  числа.
# Длину строки и числа искать во втором методе


class Homework:

    def __init__(self, abc):
        self.abc = abc

    def method1(self, abc):
        if str(abc).isalpha():
            count = sum(1 for x in str(abc) if x in 'аоуеюяэи')
            if count * (self.method2(abc) - count) <= self.method2(abc):
                res = count
            else:
                res = self.method2(abc) - count
        if str(abc).isdigit():
            res = self.method2(abc) * sum([int(i) for i in str(abc) if int(i) % 2 == 0])
        return res

    def method2(self, abc):
        return int(len(str(abc)))


home = Homework(input('Введите название объекта: ').lower())

print(home.abc)
print(home.method1(home.abc))
