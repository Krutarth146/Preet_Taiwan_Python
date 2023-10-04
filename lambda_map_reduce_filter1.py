def square(num):
    return num * num


ans = square(15)
print(ans)   # 225


# Lambda (Anounomous Function)  (One Liner)

squ_1 = lambda num : num * num

print(squ_1(56))   # 3136


max_num = lambda num1,num2,num3 : (num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3)
print(max_num(90,32,650))  # 650


# --------------------------------  

# Quadratic Function

# a*x**2 + b*x + c


def quadratic_Fun(a1,b1,c1):
    return lambda x : a1*x**2 + b1*x + c1


shah = quadratic_Fun(10,20,30)

print(shah(5))   # 380


print(quadratic_Fun(10,20,30)(5))   # 380

# -------------------------------------------------------

# Nested Lambda

royal = lambda n1,n2 : lambda x1,x2 : n1 + n2 + x1 ** 2

techno = royal(10,20)
print(techno(30,90))   # 930


# Map, Reduce, Filter -------------------------------------------


# Map  (Powerful Functions)

# def square(num):
#     return num * num

# print(square(5))  # 25
   
# list1 = [20,30,40,32,21]

# for i in list1:
#     print(square(i),end=' ')

# ---------------------------------------------

def square(num):
    return num * num

list1 = [20,30,40,32,21]

preet_1 = map(square, list1)  # <map object at 0x0000014F1AF576D0>
preet_1 = list(map(square, list1))  # [400, 900, 1600, 1024, 441]
preet_1 = list(map(lambda num : num ** 2, list1))  # [400, 900, 1600, 1024, 441]


print(preet_1)


# ------------------------------------------------------------

max_30 = list(filter(lambda x : x > 30, list1))

print(max_30)   # [40,32]


max_30 = list(map(lambda x : x > 100, list1))

print(max_30)   # [False, False, True, True, False]


# --------------------------------------------------------------------

# Reduce

from functools import reduce

list1 = [10,90,78,56,32,67]

sum_rem = reduce(lambda a,b : a+b, list1)
print(sum_rem)   # 333



# ---------------------------------------

from itertools import accumulate

sum_iter = list(accumulate(list1, lambda a,b : a+b))
print(sum_iter)   # [10, 100, 178, 234, 266, 333]



# -----------------------

list1 = []

for i in range(1,6):
    list1.append(i)

print(list1)

list2 = [i for i in range(1,6)]  # list COmprehension
print(list2)   # [1, 2, 3, 4, 5]


list9 = [lambda preet = x : preet * 10 for x in range(1,6)]


for item in list9:
    print(item())


ans = [ [90,32,45], [10,90,30,5,90], [90,23,111,22]]

for i in ans:
    ans[-2].sort()

print(ans)
# lsit1 = [10,90,89,34]
# lsit2 = [10,34,89,90]

# for sublist in list1:
#     # print(i)
#     print(max(sublist))

# for i in range(len(list1)):   # 3 ---> 0,1,2
#     for k in range(len(list1[i])): # 4  ---> 0,1,2,3
#         print(list1[i][k],end=' ')   # list1[0][2]
#     print()

# # List ---> append, Extend, Insert, pop(), pop(index), remove(element), copy, sort, reverse, count, index(element) 

# for sublist in list1:
#     sublist.sort()
#     print(sublist[-2])


# list1 = [30,90,45,78,12,12,78,12]


# # Method - 1
# unique = []


# for i in list1:
#     if i not in unique:
#         unique.append(i)
# print(unique)   # [30, 90, 45, 78, 12]

# # Method - 2

# print(list(set(list1)))  # [12, 45, 78, 90, 30]   # Unordered, Don't Allow Duplicates

# # Method - 3
# unique = []


# for ele in list1:
#     if list1.count(ele) == 1:
#         unique.append(ele)

# print(unique)