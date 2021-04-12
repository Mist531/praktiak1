n=[]
n1=[]
d1=0
d=0
s1=0
for i in open('spiski.txt', "r", encoding="utf-8"):
    a=[]
    a.append(i[:-1])
    g=a[0].split()
    n.append(g)
print(n)
for i in range(len(n)):
    if (int(n[i][2])<3):
        print("Оценка ниже 3",n[i][0],n[i][1])
for i in range(len(n)):
    d=d+1
    d1=d1+int(n[i][2])
print("Ср. арифметическое класса=",str(d1/d))
for i in open("num.txt"):
    n1.append(i[:-1])
    print(n1)
f=n1[0].split()
for i in range(len(f)):
    s1=s1+int(f[i])
print("Сумма чисел=",s1)
input()
