class DivisionByZero(Exception):
    def __init__(self, message):
        self.message = message


def main():
    while True:
        devisible = input('Введите делимое или "exit" для выхода: ')
        if devisible == 'exit': break
        divisor = input('Введите делитель или "exit" для выхода: ')
        if divisor == 'exit': break
        try:
            if float(divisor) == 0:
                raise DivisionByZero('На ноль делить нельзя!!!')
            else:
                print(f'Частное: {float(devisible) / float(divisor):.2f}')
        except DivisionByZero as ex:
            print(ex)
        except ValueError as ex:
            print(ex)


if __name__ == '__main__':
    main()