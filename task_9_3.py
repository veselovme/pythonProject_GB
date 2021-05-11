class Worker:


    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):


    def get_full_name(self):
        return f"{self.name} {self.surname}"


    def get_full_wage(self):
        return f"{sum(self._income.values())}"


manager = Position("Иван", "Петров", "Аналитик", 50000, 5000)
print(manager.position, manager.get_full_name(), "cумма зарплаты", manager.get_full_wage(), "руб.")