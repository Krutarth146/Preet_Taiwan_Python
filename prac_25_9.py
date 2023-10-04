# x = [int(j) for j in input().strip().split()]
# print(x)   # 23


# x1 = list(map(int , input().strip().split()))
# print(x1)

x2 = list(map(lambda x : x % 2, [10,20,21,31,41,90,56,78,99]))
print(x2)   # [0, 0, 1, 1, 1, 0, 0, 0, 1]
x2 = list(filter(lambda x : x % 2, [10,20,21,31,41,90,56,78,99]))
print(x2)   # [21,31,41,99]

print(list((50,) * 4))