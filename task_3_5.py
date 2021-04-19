import random


def get_jokes(count_jokes):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    res = []
    for i in range(count_jokes):
        res.append(f"{nouns[random.randint(start, stop)]} {adverbs[random.randint(start, stop)]} {adjectives[random.randint(start, stop)]}")
    return res


start = 0
stop = 4
count = int(input("Введите количество шуток: "))
print(get_jokes(count))