# Два метода в классе, один принимает в себя либо строку,  либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше или  равно длине слова, выводить все гласные, иначе согласные;  если число то, произведение суммы чётных цифр на длину  числа.
# Длину строки и числа искать во втором методе

class homework:

    a = input()

    def __init__(self,a):
        self.a = ''

    def metod1(self,a):
        if a.isalha:
            countS = sum(1 for x in input() if x in 'аоуеюяэи')
            if countS* (metod2 - countS) <= metod2:
                res = countS
            else:
                res = metod2 - countS
        if a.isdigit:
            metod2 *len([1 for i in a if i%2 == 0])
        return res

    def metod2(self,a):
        return len(a)

print(metod1())
