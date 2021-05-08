import re
print("Задание 1")
a=input("Введите строчку: ")
#bdfh fghisf dfsdgk Bsid
b= re.findall(r'([b|B]\w{2,})', a)
print(b)
print("Задание 2")
a=input("Введите строчку: ")
#ivanov@ivan sidorov@mail.ru petrov_kolya.ru
b= re.findall(r'[\w.-]+@[\w.-]+\.?[\w]+?', a)
print(b)
print("Задание 3")
a=input("Введите строчку: ")
#dsgdsg, eere; asfasf
b=re.split('; |, ',a)
print(b)
print("Задание 4")
#sfsdf,dsf,df df,df df,df.sd.fef
a=input("Введите строчку: ")
b=re.sub(r"\W", " ", a)
print(b)

