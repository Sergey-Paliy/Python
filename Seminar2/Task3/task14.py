# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

print("Введите число")
n= int (input())
digit =1
while n>digit:
    digit=digit*2
    print(digit)
