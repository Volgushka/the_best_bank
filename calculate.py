class Calculate:

    def calculate(self):
        oper = input("Введите операцию:\n плюс - p \n минус - m \n деление - div \n умножение - mul \n факториал - fl \n степень- ex \n модуль - mod \n логарифм - log \n процент - per")
        if oper == 'p':
            print(f'Результат операции сложения {self.plus(int(input("Введите первое число: ")),int(input("Введите второе число: ")))}')
        elif oper == 'm':
            print(f'Результат операции вычитания {self.minus(int(input("Введите первое число: ")),int(input("Введите второе число: ")))}')
        elif oper == 'div':
            print(f'Результат операции деления {self.div(int(input("Введите первое число: ")),int(input("Введите второе число: ")))}')
        elif oper == 'mul':
            print(f'Результат операции умножения {self.multi(int(input("Введите первое число: ")),int(input("Введите второе число: ")))}')
        elif oper == 'fl':
            print(f'Факториал {self.factorial(int(input("Введите число: ")))}')
        elif oper == 'ex':
            print(f'Число в степени составит {self.exponent(int(input("Введите число: ")),int(input("Введите желаемую степень: ")))}')
        elif oper == 'mod':
            print(f'Число по модулю {self.modul(int(input("Введите первое число: ")))}')
        elif oper == 'log':
            print(f'Логарифм {self.logarithm(int(input("Введите аргумент: ")),int(input("Введите основание: ")))}')
        elif oper == 'per':
            print(f'Процент от суммы составит {self.percent(int(input("Введите число: ")),int(input("Введите процент: ")))}')

    def plus(self,a, b):
        return a + b

    def minus(self,a, b):
        return a - b

    def div(a,b):
        return a/ b

    def multi(a,b):
        return a*b

    def factorial(n: int):
        res = 1
        for i in range(2, n+1):
            res = res*i
        return res

    def exponent(a,b):
        return a**b

    def modul(a):
        return a if a>0 else a*-1

    def logarithm(a,b):
        import math
        return math.log(a,b)

    def percent(a,b):
        return a/100*b

