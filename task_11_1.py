class Date:
    def __init__(self, date='01-01-2001'):
        self.date = date

    @classmethod
    def split_date(cls, date):
        try:
            new_date = tuple(map(int, date.split('-'))) if len(tuple(map(int, date.split('-')))) == 3 else 'Ошибка'
            if new_date == 'Ошибка':
                raise ValueError
            return new_date
        except ValueError:
            print(f'Введена некорректная дата')

    @staticmethod
    def valid_date(date):
        valid_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        try:
            day, month, year = Date().split_date(date)
            if year % 400 != 0 and year % 100 == 0:
                if 1 <= day <= valid_days[month]:
                    return True
            elif year % 400 != 0 and year % 4 != 0:
                if 1 <= day <= valid_days[month]:
                    return True
            else:
                if month == 2 and 1 <= day <= 29:
                    return True
                elif 1 <= day <= valid_days[month]:
                    return True
            raise Exception
        except KeyError:
            print(f'Ошибка! Неверно введен месяц!')
            return False
        except TypeError:
            return False
        except Exception:
            print(f'Ошибка! Неверно введен день!')
            return False


def main():
    while True:
        date = input('Введите дату в формате дд-мм-гг, для выхода неберите "exit": ')
        if date == 'exit':
            break
        else:
            date = Date(date)
            print(date.split_date(date.date))
            print(date.valid_date(date.date))


if __name__ == '__main__':
    main()