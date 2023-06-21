# string 

str1 = 'c'
print(type(str1))   # <class 'str'>

str2 = "Preet"
print(type(str2))  # <class 'str'>


# string is Immutable (Unchangeble)

str1 = "Preet"
print(id(str1))  # 2298725317936

str1 += " Shah"
print(str1)   # Preet Shah
print(id(str1))   # 2298725317744


# string is Ordered

str2 = "Royal Techno"


# Indexing
print(str2[0])   # R
print(str2[-1])   # o


# Slicing
str2 = "Royal Techno"

print(str1[0 : 5])  # Preet
print(str1[5 : 0])  # blank
print(str2[2 : ])   # yal Techno
print(str2[-1 : -5])   # blank
print(str2[-5 : -1])   # echn
print(str2[-3 : 2])   # 
print(str2[2 : 8 : 2])   # ylT
print(str2[5 : 10 : 1])   #  Tech
print(str2[-1 : -6 : 1])   # 
print(str2[-2 : 5 : -3])   # ne
print(str2[10 : 1 : 2])   # blank
print(str2[-3 : 4 : 2])   # blank


# String Methods ---------------------


str1 = "ROyal Techno is Best Institute Ever123."

print(str1.replace('Techno', 'Sankul'))   # ROyal Sankul is Best Institute Ever123.
print(str1.replace('e', 'o'))   # ROyal Tochno is Bost Instituto Evor123.
print(str1.replace('e', 'o', 1))   # ROyal Tochno is Best Institute Ever123.

str1 = "ROyal_Techno is Best Institute Ever123."
print(str1.split())   # ['ROyal_Techno', 'is', 'Best', 'Institute', 'Ever123.']
print(str1.split('_'))   # ['ROyal', 'Techno is Best Institute Ever123.']
print(str1.split('I'))   # ['ROyal_Techno is Best ', 'nstitute Ever123.']

print(str1.partition('I'))   # ('ROyal_Techno is Best ', 'I', 'nstitute Ever123.')
print(str1.partition('e'))   # ('ROyal_T', 'e', 'chno is Best Institute Ever123.')
print(str1.rpartition('e'))   # ('ROyal_Techno is Best Institute Ev', 'e', 'r123.')