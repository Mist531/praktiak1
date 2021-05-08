print("Практика 8 вар 6")
import re
print("Задание 1")
a=input("Введите строчку: ")
print(re.findall(r"\b\d+\b",a))
print("Задание 2")
a=input("Введите строчку: ")
#Это курс информатики соответствует ФГОС и ПООП, это подтверждено ФГУ ФНЦ НИИСИ РАН. 
c=list(re.findall(r"(\b[А-Я]{2,})[\s|\S]",a))
for i in range(0,len(c)):
    print(str(c[i]))
print(c)
input()





