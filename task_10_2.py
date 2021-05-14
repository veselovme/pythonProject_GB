from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def cloth_consumption(self):
        pass

class Clothes(MyAbstractClass):
    def __init__(self, param=100):
        self.param = param

    @property
    def cloth_consumption_coat(self, param):
        pass

    @property
    def cloth_consumption_suit(self, param):
        pass

    @property
    def cloth_consumption(self):
        return self.cloth_consumption_coat + self.cloth_consumption_suit


class Coat(Clothes):
    @property
    def cloth_consumption(self):
        result = round(self.param / 6.5 + 0.5, 2)
        Clothes.cloth_consumption_coat = result
        return f'Расход ткани для пальто {self.param} размера = {round(self.param / 6.5 + 0.5, 2)} м.'

class Suit(Clothes):
    @property
    def cloth_consumption(self):
        result = round(2 * self.param + 0.3, 2)
        Clothes.cloth_consumption_suit = result
        return f'Расход ткани для костюма на рост {self.param} м. = {round(2 * self.param + 0.3, 2)} м.'

cloth = Clothes()
coat = Coat(int(input("Введите размер пальто: ")))
print(coat.cloth_consumption)
suit = Suit(int(input("Введите рост в см.: ")) / 100)
print(suit.cloth_consumption)
print(f'Общий расход ткани на пальто и костюм = {cloth.cloth_consumption} м.')