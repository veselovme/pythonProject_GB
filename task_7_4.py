import os

result = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0, 10000000: 0, 100000000: 0}
keys = [0, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        if size == 0:
            result[0] += 1
            continue
        for index, key in enumerate(keys):
            if index == len(keys) - 1:
                print(f"Файл не удовлетворяет условиям (слишком большой): {file}")
                break
            if key < size <= keys[index + 1]:
                result[keys[index + 1]] += 1
                break
print(result)