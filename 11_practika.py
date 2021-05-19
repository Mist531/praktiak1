print("Задание 1,2 вар 6")
import os,time
from datetime import datetime
f=0
a=[]
filedirs = os.listdir(".")
for fd in filedirs:
    if os.path.isfile(fd):
        a=time.gmtime(os.stat(fd).st_mtime)
        a1=datetime(a.tm_year,a.tm_mon,a.tm_mday)
        b1=datetime.now()
        w=b1-a1
        if not os.path.exists('TsetPapka'):
            os.mkdir('TsetPapka')
        if w.days>=92:
            print("Файл найден")
            dr=os.getcwd()
            dt="TsetPapka/"
            os.replace(fd, dt + fd)
            f=f+1
if f!=0:
    file=open("work.txt", "w")
    file.write("Программа нашла и перенесла "+str(f)+" файлов")
    file.close()
try:
    file = open("work.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print('Программа не нашла файлы')
except IOError:
    print('Something else')
input()
print("Задание 3 вар 6")
import csv
s=""
myData = [["first_name", "second_name"]]
print("Введите картину и год её написания(через пробел), когда все данные будут введины напишите 0")
while s!="0":
    s=str(input("Введите данные "))
    if s=="0":
        break
    myData.append(s.split())
myFile = open('example2.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
print("Writing complete")
myFile.close()
with open('example2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['second_name'])