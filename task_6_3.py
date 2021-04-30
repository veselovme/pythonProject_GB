import sys
import json


def clean_user(user):
    return user.strip()


def clean_hobbies(hobbies):
    return hobbies.strip()


result_dict = {}
with open('users.csv', 'r', encoding='UTF-8') as f_1, \
        open('hobby.csv', 'r', encoding='UTF-8') as f_2:
    for hobbies, user in zip(f_2, f_1):
        result_dict[clean_user(user)] = clean_hobbies(hobbies)
    for _ in f_2:
        sys.exit(1)
    for user in f_1:
        result_dict[clean_user(user)] = None

with open('result.json', 'w', encoding='UTF-8') as result_file:
    json.dump(result_dict, result_file, ensure_ascii=False)
with open('result.json', 'r', encoding='UTF-8') as f:
    result = json.load(f)
print(result)