# Factorial

# 5! = 5*4*3*2*1 , 1*2*3*4*5

# num  = 5
# mul = 1

# # for i in range(1,num + 1):
# for i in range(num, 0, -1):
#     mul = mul * i  # 120 = 24 * 5

# print(mul)   # 120



# Recursion ---> when function calls itself then it is called Recursion

def factorial(num):   # 5
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)   # 5

print(factorial(5))   # 120

import time

before_time_it = time.time()
def Fibo_iteration(step):
    list1 = [1,1]
    for j in range(step):
        list1.append(list1[-1] + list1[-2])
    return list1[:-2]


print(Fibo_iteration(10))  # [1, 1, 2, 3, 5]
print(time.time() - before_time_it)

# print()
before_time_rec = time.time()
def Fibo_Recursion(n1):
    if n1 == 0 or n1 == 1:
        return n1
    return Fibo_Recursion(n1-1) + Fibo_Recursion(n1 - 2)

print(Fibo_Recursion(10))
print(time.time() - before_time_rec)


list1 = [10,20,30,40]

print(list(map(lambda x : list(j for j in range(1,x+1) if x % j == 0) , list1)))

# [[1, 2, 5, 10], [1, 2, 4, 5, 10, 20], [1, 2, 3, 5, 6, 10, 15, 30], [1, 2, 4, 5, 8, 10, 20, 40]]

# Total 5 Programs

