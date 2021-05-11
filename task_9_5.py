class Stationery:
    def __init__(self, title="Запуск отрисовки"):
        self.title = title

    def draw(self):
        print(f"{self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуем {self.title} ручкой")


class Pencil(Stationery):
    def draw(self):
        print(f"Рисуем {self.title} карандашом")


class Marker(Stationery):
    def draw(self):
        print(f"Рисуем {self.title} маркером")


stat = Stationery()
stat.draw()
pen = Pen("красной")
pen.draw()
pencil = Pencil("цветным")
pencil.draw()
marker = Marker("аквамаркером")
marker.draw()