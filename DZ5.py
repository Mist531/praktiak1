print("Задание 1")
a=int(input("Введите max число: "))
b=[]
for i in range(1,a+1):
    if ((i%2)==0):
        b.append(i)
print(b)
print("Задание 2")
b=[]
d=0
b.append(1)
for i in range(100):
    b.append(0)
b.append(1)
print(b)
for i in range(len(b)):
    if (b[i]==0):
        d=d+1
print("Всего 0:",str(d))
print("Задание 3")
b=("красный","синий","зелёный")
#Скопируйте для ввода:красный красный синий зелёный синий синий зелёный 
a=input("Введите текст:")
a=a.split()
print(a)
a1=0
g={}
s={}
for d in range(len(b)):
    for i in range(len(a)):
        if (b[d] == a[i]):
            a1=a1+1
    r=dict({b[d]:a1})
    print(r)
    g.update(r)
    a1=0
print(g)
w=2
while (w!=0):
    w=int(input("Хотите поменять словарь? 1-да, 0-нет "))
    if (w==1):
        a1=int(input("Добавить значение-1, убрать-0 "))
        if (a1==1):
            q=input("Введите значение ")
            q1=input("Введите ключ ")
            r=dict({q1:q})
            g.update(r)
            print(g)
        else:
            q1=input("Введите ключ который хотите удалить ")
            g.pop(q1)
            print(g)
    else:
        w=0
else:
    input("Нажмите Enter для выхода")