list1 = [10,10,20,90.89,"str1",'P',True,90+8j,[10,20,90], (2,3,4), {80,34,12}, {"Name" : "Preet", 'School':"bvcdsvb"}]

print(list1)   # [10, 10, 20, 90.89, 'str1', 'P', True, (90+8j), [10, 20, 90], (2, 3, 4), {80, 34, 12}, {'Name': 'Preet', 'School': 'bvcdsvb'}]


print(type(list1))  # <class 'list'>

print(len(list1))  # 12   # Length starts from 1, Index starts from 0

print(id(list1))   # 1671294432448

print(list1.__sizeof__())  # 136

# List Characteristics: Allow's Duplicates, Ordered (Indexed)

# List Indexing and Slicing

list1 = [10,20,30,40,50,70]   # Ordered

# print(list1[6])  # Index out of Range

print(list1[3])  # 40
print(list1[-1])  # 70
print(list1[-4])  # 30
print(list1[-6])  # 10


# set1 = {10,20,30,40,50}
# print(set1)   # {50, 20, 40, 10, 30}   (Onordered)


# Slicing

list1 = [10,20,30,40,50,70] 

# print(list1[start : end (n-1)])
print(list1[0 : 5])   # start - 0, End - 5 (5-1=4)   # [10, 20, 30, 40, 50]
print(list1[3 : 4])   # [40]
print(list1[3])   # 40 --> int
print(type(list1[3 : 4]))   # list
print(list1[4:])   # [50, 70]
print(list1[:3])   # [10,20,30]
print(list1[:])   # [10,20,30,40,50,70]
print(list1[4:1])   # []
print(list1[-3:2])   # []
print(list1[-5:-1])   # [20, 30, 40, 50]
# print(list1[start : end(n-1) : step(n-1)])   # [20, 30, 40, 50]
print(list1[0 : 5])   # [10, 20, 30, 40, 50]
print(list1[0 : 5 : 1])   # [10, 20, 30, 40, 50]
print(list1[0 : 5 : 2])   # [10, 30, 50]

list1 = [10,20,30,40,50,70] 
print(list1[5 : 0 : -2])   # [70, 40, 20]
print(list1[-1 : -5 : -1])   # [70, 50, 40, 30]
print(list1[4 :  : -1])   # [50, 40, 30, 20, 10]
print(list1[  :  : -1])   # [70, 50, 40, 30, 20, 10]
print(list1[  : -4 : ])   # [10, 20]
print(list1[-3:1:1])   # []