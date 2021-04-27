list1 = [10, 13, 5, 15, 8, 4, 9, 29, 19, 3]
more = [list1[num] for num in range(1, len(list1)) if list1[num] > list1[num - 1]]
print(more)