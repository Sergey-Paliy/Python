# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

list_1=[]
n = int(input("Введите количество элементов "))
for i in range(n):
   num = int(input("Введите числа "))
   list_1.append(num)
min = int(input("Введите минимальное значение "))
max = int (input("Введите максимальное значение "))

def index(min, max):
    index_2 = []
    for i in range(len(list_1)):
        if min <= list_1[i] <= max:
            index_2.append(i)
    return index_2
    
result = index(min, max)
print(*result)






        




