print("Практика 10 вар 6")
print("Задание 1")
n=[]
r=0
for i in open("numbers.txt"):
    n.append(i[:-1])
print(n)
for i in range(len(n)):
    r=r+float(n[i])
f=r/len(n)
print("Ср. арифметическое=",f)
print("Задание 2")
n=open("slova.txt").read()
n=n.split()
#Скопировать для ввода:one two three four five
d=input("Введите текст: ").split()
for i in range(len(d)):
        if (d[i] in n):
            a=0
        else:
            print("Данное слово не входит в словарь",str(d[i]))
print("Задание 3")
n=[]
for i in open('spisok.txt', "r", encoding="utf-8"):
    a=[]
    a.append(i[:-1])
    g=a[0].split()
    n.append(g)
print(n)
for i in range(len(n)):
    try:
        a1=n[i][2]
        print(n[i][0],n[i][1])
    except:
        r=0
#Скопировать для ввода:89083333333
s1=input("Введите номер: ")
for i in range(len(n)):
    try:
        if (s1 == n[i][2]):
            print("Подходящая запись:",n[i][0],n[i][1],n[i][2])
    except:
        a1=0
b1=0
for i in range(len(n)):
    if (n[i][1]=="1984"):
        b1=b1+1
print("Количество студентов с датой рождения 1984:",str(b1))
input()

