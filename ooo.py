class Human:

    default_name = "Oleg"
    default_age = 35

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 1000
        self.__house = None

    def info(self):
        print(f"Имя: {self.name}\nВозраст: {self.age}\nДеньги: {self.__money}\nДом: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Дефолтное имя: {Human.default_name}\nДефолтный возраст: {Human.default_age}")


def __make_deal(self, house, money):
    self.__house = house
    self.__money -= money

def earn_money(self, money):
    self.__money += money

def buy_house(self, house, sale):
    if self.__money < house.final_price(sale):
        print("У объекта недостаточно средств")
    else:
        self.__make_deal(house, house.final_price(sale))


class House:

    default_cost = 3000

    def __init__(self, area, cost=default_cost):
        self._price = cost

def final_price(self, sale):
    return self._price*(1-sale/100)

def __str__(self):
    return "Дом"


class SmallHouse(House):

    def __init__(self):
        super().__init__(40)


s_house = SmallHouse()
human = Human()
human.buy_house(s_house, 20)
human.earn_money(10000)
human.buy_house(s_house, 20)
human.info()