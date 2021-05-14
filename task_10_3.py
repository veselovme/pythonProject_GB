class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Сложение ячеек:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Вычитание ячеек:")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Ячеек в первой клетке меньше второй, вычитание невозможно!"

    def __mul__(self, other):
        print("Умножение ячеек:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Деление ячеек:")
        return Cell(self.nums // other.nums) if other.nums != 0 else "Делить на 0 нельзя"

cell_1 = Cell(48)
cell_2 = Cell(11)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(8))