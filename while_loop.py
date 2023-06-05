# Loop ----> 1. Entry control loops --->  1. while  2. for

# while ----> 1. Intialization   2. Condition (End Condition)  3. Flow

preet = 25  # start position

while preet <= 50:
    print(preet,end=' ')   # 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 
    preet += 1   # preet = preet + 1

print()


counter = 0
preet = 50

while preet >= 25:
    print(preet,end=' ')
    counter+=1
    preet -= 1

print(counter)  # 26
print(preet)  # 24

jk = 5

while jk <= 15:
    if jk == 10:
        break
    print(jk)
    jk+=1

jk = 5

while -3:
    if jk == 10:
        break
    print(jk)  # 5 6 7 8 9
    jk+=1

print()

g = 1
while g <= 30:
    print(g,end=' ')  # 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29
    g+=2
print()

# 5 & 7 Divisible b/w 1 to 100

