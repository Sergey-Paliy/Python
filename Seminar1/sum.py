print("Введите число: ")
n=int (input())
a=n
res=0
while n>0:
    res=res+n%10
    n=n//10
print("n = ",a,"->" " res = ", res, "(", a//100%100,"+", a//10%10, "+", a%10, ")")