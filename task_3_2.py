num = input("Введите наименование числа от ноля до дести на английскрм языке: ")


def num_translate():
    for k in nums.keys():
        if k == num:
            return(nums.get(k))
        else:
                for k in nums1.keys():
                    if k == num:
                        return(nums1.get(k))


nums = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
nums1 = {"Zero": "Ноль", "One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}
print(num_translate())