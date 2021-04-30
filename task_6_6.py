# add_sale.py
import sys

sales = sys.argv[1]
with open("bakery.csv", 'a', encoding='UTF-8') as f:
    print(sales, file=f)

# show_sales.py
from sys import argv

with open('bakery.csv', 'r', encoding='UTF-8') as f:
    param = len(argv)
    if param == 1:
        print(f.read())
    elif param == 2:
        for line in f.readlines()[int(argv[1]) - 1:]:
            print(line, end='')
    elif param == 3:
        i = 0
        for line in f:
            i += 1
            if i >= int(argv[1]):
                if i > int(argv[2]):
                    break
                print(line, end='')