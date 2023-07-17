# List Characteristics

# List : ordered (Indexed), Allow's Duplicates, Mutable

# Tuple: Ordered (Indexed), Allow's Duplicates, Immutable (Not changeble)

tup1 = ()
print(type(tup1))  # <class 'tuple'>

tup2 = (20)
print(tup2)   # 20
print(type(tup2))   # <class 'int'>

tup2 = (20,)
print(tup2)   # (20,)
print(type(tup2))   # <class 'tuple'>

l1 = [10,20,30]
t1 = (10,20,30)

print(l1.__sizeof__())   # 72
print(t1.__sizeof__())   # 48

tup2 = (10,20,30,40,50,20)

# print(tup2)   # (10, 20, 30, 40, 50)

# print(tup2[-2]) # 40  # int   # Indexing
# print(tup2[-2:2:-1]) # (40,)  # tuple  # Slicing


print(tup2.count(20))  # 2  # Total occurance of any element

print(tup2.index(20))  # 1

l1 = list(tup2)

print(l1)  # [10, 20, 30, 40, 50, 20]
l1.append([10,20,30])
print(tuple(l1))  # (10, 20, 30, 40, 50, 20, [10, 20, 30])


tup2 = (10,89,89,10,10,10,67)

l1= []

for i in tup2:
    if i not in l1:
        l1.append(i)

print(l1)  # [10, 89, 67]

print(set(tup2))  # {89, 10, 67}  # Unordered, Don't Allow Duplicates, Immutable (But we can add or remove elements.)


list1 = [1,2,2,6,2,5,4,4,4,5,6,3,1,1]

# 1 ---> [0...]
# 2 ---> [1,2,4]    


l2 = []
for i in list1:
    if i not in l2:
        l2.append(i)

print(l2)   # [1, 2, 6, 5, 4, 3]
# print(list(set(list1)))  # [1, 2, 3, 4, 5, 6]

for i in l2:
    temp = []
    for j in range(len(list1)):
        if i == list1[j]:
            temp.append(j)
    print(i,' = ',temp)

# List Compre.
# index(list1[j], x)