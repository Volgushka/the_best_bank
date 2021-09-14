class Human:
    default_name = 'no name'
    default_age = 'no age'

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 0

    def info(self):
        print(self.name)
        print(self.age)
        print(self.__money)
        print(self.__house)

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def earn_money(self,money):
        self.__money += money
        return self.__money

Human.default_info()

men = Human(input("Введите имя: "), input("Введите возраст: "))
men.info()
men.earn_money(int(input("Сколько ты зарабатываешь: ")))
men.info()
