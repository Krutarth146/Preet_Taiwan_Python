# 1 to 1000

for i in range(10):  # start = 0, End = 10 (n-1)
    print(i,end=' ')   # 0 1 2 3 4 5 6 7 8 9

print()
for j in range(3,11):
    print(j,end=' ')   # 3 4 5 6 7 8 9 10

print()
for k in range(20,9):
    print(k)  # Blank

print()

for h in range(20,9,-1):
    print(h,end=' ')   # 20 19 18 17 16 15 14 13 12 11 10

print()

for g in range(2,11,1):
    print(g,end=' ')  # 2 3 4 5 6 7 8 9 10
print()

for g in range(2,11,2):  # start , end (n-1), step (n-1)
    print(g,end=' ')  # 2 4 6 8 10

print()
for e in range(1,101,2):
    print(e,end=' ')

print()

for u in range(65,41,3):
    print(u)
print()

for u in range(-9,5,3):
    print(u,end=' ')   # -9 -6 -3 0 3

print()

# for h in range(0.5, 2.0, 0.5):
#     print(h)  # Gives Error

for t in range(3, -2, 1):
    print(t)  # Blank

print()

for g in range(-3,-9,-1):
    print(g,end=' ')  # -3 -4 -5 -6 -7 -8

l1 = [10,20,30,40,50]

for i in l1:
    print(i)

for j in range(len(l1)):
    print(j)   # 0 1 2 3 4

for j in range(len(l1)):
    print(l1[j])  # 10 20 30 40 50