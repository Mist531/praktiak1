print("Задание 1")
n=int(input("Введите n "))
a=[]
for i in range(n):
    a.append([])
    for y in range(n):
        c=abs(y-i)
        a[i].append(c)
for i in range(n):
    print()
    for t in range(n):
        print(a[i][t]," ",end="")
print()
print("Задание 2")
a=[]
n=int(input("Введите n "))
m=int(input("Введите m "))
k=int(input("Введите k "))
l=int(input("Введите l "))
for i in range(n,m+1):
    a.append(i)
for i in range(len(a)):
    if (a[i]%k==0) or (a[i]%l==0):
        print(str(a[i]), end=" ")
print(" ")
for i in range(len(a)):
    if (a[i]%(k*l)==0):
        print(str(a[i]), end=" ")
input()