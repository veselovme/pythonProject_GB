num = input("Введите наименование числа от ноля до дести на английскрм языке: ")


def num_translate():
    for k in nums.keys():
        if k == num:
            return(nums.get(k))


nums = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
print(num_translate())