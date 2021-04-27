tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen_of_people():
    i = 0
    j = 0
    while i < len(klasses):
        if i >= len(tutors):
            yield (None, klasses[i])
            i += 1
            j += 1
            break
        else:
            yield (tutors[j], klasses[i])
            i += 1
            j += 1


for gen in gen_of_people():
    print(gen)