print("Практика 8 вар 6")
import re
print("Задание 1")
a=input("Введите строчку: ")
print(re.findall(r"\b\d+\b",a))
print("Задание 2")
a=input("Введите строчку: ")
b=list(re.findall(r"(\b[А-Я]{2,}\b)",a))
for i in range(0,len(b)):
    print(str(b[i]))






