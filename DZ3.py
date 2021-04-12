import datetime
try:
    a=int(input("Введите год "))
    b=int(input("Введите месяц (числом) "))
    c=int(input("Введите день "))
    g=datetime.date(a,b,c)
    a=1
except:
    a=0
if (a == 1):
    print("True")
else:
    print("False")
input()
