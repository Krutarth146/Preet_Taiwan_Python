# printf(), scanf() -> stdio.h
# getch(), clrscr() -> conio.h
# strcat(), strcpy() -> string.h

# from __future__ import print_function -> py version 2

print('Preet',end='\r')
print("Shah")  # Shaht
print('Preet',end='\b')
print("Shah")  # PreeShah

print('Preet',end=' Taiwan ')
print("Shah")  # Preet Taiwan Shah

str1 = "P"
str2 = "REET"

print(str1,str2,sep=' ')   # P REET

print(str1,str2,sep='')  # PREET

print('''
    Adress: Surbhi Complex,
            Ahmedabad
            380001
''')

# -------------------------------

# Python is Dyanmic Lang.
x = 90
print(x)  # 90
print(type(x))  # <class 'int'>
print(id(x))    # 1632916081680
print(x.__sizeof__())  # 28


y = 89.78
print(y)   # 80.78
print(type(y))  # <class 'float'>

_ = "R"
print(type(_))  # <class 'str'>

l = 'Preet'
print(type(l))  # <class 'str'>

h = 13 + 7j
print(h)  # (13+7j)    # 13 is real Part, 7j is Imaginary Part
print(type(h))   # <class 'complex'>

print(3+2)   # 5
print(78 + 90.56)  # 168.56  # Typecasting

# x = (int)89.90  ->  in C

x = 90.89
print(int(x))    # 90
print(type(x))   # float

k = 23   
print(h + k)   # (36 + 7j)

t = 6+8j
print(h+t)  # (19+15j)

f = True
print(type(f))  # <class 'bool'>

list1 = [10, 90, 89, 78]
print(list1)
print(type(list1))  # <class 'list'>