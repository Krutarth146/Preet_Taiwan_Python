i = 1

while i<=10:
    if i == 5:
        break
    print(i,end=' ')   # 1 2 3 4 
    i+=1


# ------------------

k = 1
while k <= 10:
    if k == 5:
        k+=1
        continue
    print(k)
    k+=1

# -----------------------
counter = 0
outer = 0

k = 10
while k<=14:
    l = 3
    while l<=6:
        print(l)
        counter += 1
        l+=1
    print(k)
    outer += 1
    k+=1

print(counter,outer)  # 20   5


# ---------------------------

for k in range(1,4):
    for j in range(1,4):
        if k == j:
            break
        print(j,end=' ')
    print(k,end=' ')

# 1 1 2 1 2 3

print()
for h in range(1,5):
    if h % 8 == 0:
        break
    print(h,end=' ')
else:
    print('Else Block is Executed.') 


# 1 2 3 4 Else Block is Executed.


# Homework

i = 10
j = 7 
while i <= 15:
    while j<=15:
        if i % j == 0:
            break
        print(j,end=' ')
        j+=1
    print(i,end=' ')
    i+=1


# for Loop

for i in range(25,30):
    for j in range(25,30):
        if i == j:
            continue
        print(j,end=' ')
    else:
        print("Inner Else Executed.")
    if i == 30:
        break
    print(i,end=' ')
else:
    print("Outer Else Executed.")