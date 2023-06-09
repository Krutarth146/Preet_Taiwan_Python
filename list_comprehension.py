l2 = [[10,20,30], 
      [40,50,60], 
      [70,80,90]]


# for i in l2:
#     for j in i:
#         print(j)

# l3 = [j for i in l2 for j in i]
# print(l3)   # [10, 20, 30, 40, 50, 60, 70, 80, 90]


# ------------------------------------

print(i for i in range(1,11))   # <generator object <genexpr> at 0x0000026C44809A10>

# x = tuple(i for i in range(1,11))
# print(x)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# # --------------------------------------

# y = [int(i) for i in input().split()]
# print(y)   # [10, 907, 87, 7, 6, 54, 32, 7, 89, 0]

# -------------------------------------------

# Matrix = []

# for i in range(3):
#     temp = [int(i) for i in input().split()]
#     Matrix.append(temp)

# print(Matrix)   # [[43, 67, 32], [12, 33, 22], [88, 99, 66]]

# -----------------------------------

l2 = [10,90,67,32,44]

# Ans. [(10,10), (10,90), (10,67), (10,32) .....]

for i in l2:   # 10  90
    for j in l2:  # 10 90 67 32 44  10 90 67 32 44
        print((i,j))


lst = [(i,j) for i in l2 for j in l2]
print(lst)   # [(10, 10), (10, 90), (10, 67), (10, 32), (10, 44), (90, 10), (90, 90), (90, 67), (90, 32), (90, 44), (67, 10), (67, 90), (67, 67), (67, 32), (67, 44), (32, 10), (32, 90), (32, 67), (32, 32), (32, 44), (44, 10), (44, 90), (44, 67), (44, 32), (44, 44)]

lst2 = [20, 90, 78, 75, 43 , 21]

list1 = [i for i in lst2 if i % 2 != 0]
print(list1)   # [75, 43, 21]


l2 = [[10,20,30], 
      [40,50,60], 
      [70,80,90]]


for row in range(len(l2)):
    for col in range(len(l2[row])):
        print(l2[row][col],end=' ')
    print()

print()
for row in range(len(l2)):
    for col in range(len(l2[row])):
        print(l2[col][row],end=' ')
    print()


l1 = [10,20,30,40,50,60]
l2 = [50,90,232,45,21,23]

# (10,50), (20,90) .....

# for i,j in zip(l1,l2):
#     print((i,j))

l3 = [i for i in zip(l1,l2)]
l3 = [i for i,j in zip(l1,l2) if j % 2 != 0]
print(l3)


l9 = [10,89,78,32,45,67,54,32,31]

l10 = [i for i,j in enumerate(l9,100) if j % 2!=0 ]
print(l10)  # [101, 104, 105, 108]


exec("a=10\nb = 20\nc=a%b\nprint(c)")
exec("x=int(input())\ny=int(input())\nprint(x+y)")