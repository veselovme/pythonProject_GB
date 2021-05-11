class Car:
    """Автомобиль"""


    def __init__(self, name, color, speed, is_police = False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Автомобиль: {self.name} цвет {self.color}, машина полицейская - {self.is_police}')


    def go(self):
        print(f'{self.name}: Поехала.')


    def stop(self):
        print(f'{self.name}: Остановилась.')


    def turn(self, direction):
        print(f'{self.name}: Повернула: {"налево" if direction == 0 else "направо"}.')


    def show_speed(self):
        return f'{self.name}: Текущая скорость: {self.speed}.'


class TownCar(Car):
    """Городская машина"""


    def show_speed(self):
        return f'{self.name}: Текущая скорость: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость: {self.speed}."


class SportCar(Car):
    """Спортивная машина"""


class WorkCar(Car):
    """Грузовик"""

    def show_speed(self):
        return f'{self.name}: Текущая скорость: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость: {self.speed}."


class PoliceCar(Car):
    """Полицейская машина"""


    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


town_car = TownCar('"Городская машина"', 'серый', 80)
town_car.go()
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()
print()

sport_car = SportCar('"Спортивная машина"', 'зеленый', 120)
sport_car.go()
sport_car.turn(1)
print(sport_car.show_speed())
sport_car.stop()
print()

work_car = WorkCar('"Грузовик"', 'синий', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.stop()
print()

police_car = PoliceCar("Полицейская машина", "белый", 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()