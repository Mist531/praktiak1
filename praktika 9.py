print("Практика 9 вар 6")
import datetime
import time
import calendar
import math as m
print("Задание 1")
now=datetime.datetime.now()
a=0
while a!=1:
    try:
        a=int(input("Введите год "))
        b=int(input("Введите месяц (числом) "))
        c=int(input("Введите день "))
        g=datetime.date(a,b,c)
        time.sleep(2)
        print("Введен",str(g))
        a=1
    except:
        time.sleep(2)
        print("Введена не существующая дата, попробуйте снова")
        a=0
d=now.date()
time.sleep(2)
print("Сейчас",str(d))
time.sleep(2)
print("День недели сейчас "+str(now.weekday()),"День недели метки "+ str(g.weekday()))
r=d-g
time.sleep(2)
print("Разница между датами:",str(r).split()[0],"Недели:",str(int((r.days)/7)),"Месяца:",str((d.year-g.year)*12+(d.month-g.month)))
print("Задание 2")
a=0
while a!=1:
    try:
        a=int(input("Введите год "))
        b=int(input("Введите месяц (числом) "))
        c=int(input("Введите день "))
        g=datetime.date(a,b,c)
        time.sleep(2)
        print("Введен",str(g))
        a=1
    except:
        time.sleep(2)
        print("Введена не существующая дата, попробуйте снова")
        a=0
if (1<=g.month<=9):
    r=datetime.date(g.year, 9, 1)
    print("До 1 сентября осталось: Недель",str(int(((r-g).days)/7)))
else:
    r=datetime.date((g.year)+1, 9, 1)
    print("До 1 сентября осталось: Недель",str(int(m.fabs((g-r).days)/7)))
print("Задание 3")
a=0
while a!=1:
    try:
        a=int(input("Введите год "))
        b=int(input("Введите месяц (числом) "))
        c=int(input("Введите день "))
        g=datetime.date(a,b,c)
        time.sleep(2)
        print("Введен",str(g))
        a=1
    except:
        time.sleep(2)
        print("Введена не существующая дата, попробуйте снова")
        a=0
def grom(g):
    f=calendar.monthrange(g.year, g.month)[1]
    print("До конца месяца осталось:",str(f-(g.day)))
    t=datetime.date(g.year+1, 1, 1)
    y=datetime.date(g.year, 1, 1)
    r=int(m.fabs(int(str(y-t).split()[0]))-(g.day))
    print("До конца месяца осталось:",str(r))
grom(g)
input()
    
    
    
    