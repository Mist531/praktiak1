print("Задание 1,2 6 вар")
class Game:
    sp=[]
    def __init__(a, x=" ", y=" "):
        a.x=x
        a.y=y
        a.sp.append((a.x,a.y))
    def __str__(a):
        s="Название игры: "+ str(a.x) + ", Год создания: "+ str(a.y)
        return s
    def __repr__(a):
        return f"Игра: {a.x}, Год: {a.y}"
q = Game("CS:GO",2012)
w = Game("Fallout",1997)
e = Game("Minecraft",2011)
print(q)
print(w)
q
w
print(q.sp)
print("Задание 3 6 вар")
class Rectangle:
    sp=[]
    def __init__(a, x=0, y=0):
        a.x=x
        a.y=y
        a.r=a.x*2+a.y*2
        a.sp.append((a.x,a.y,a.r))
    def __str__(a):
        s="a="+ str(a.x) + ", b="+ str(a.y)+", P="+str(a.r)
        return s
    def __repr__(a):
        return f"a={a.x}, b={a.y}, P={a.r}"
q=Rectangle(4,5)
w=Rectangle(5,7)
print(q)
print(w)
q
w
print(q.sp)





