num = 895  # 598


# while num != 0:
while num > 0:
    rem = num % 10    # rem = 8
    print(rem,end='') # 598
    num = num // 10   # num = 0

print()

# Sum of Numbers
num = 895 
sum = 0

while num > 0:
    rem = num % 10    # rem = 8
    sum = sum + rem   # sum = 22
    num = num // 10   # num = 0

print(sum)  # 22


# Total Digits

num = 8951
counter = 0

while num > 0:
    counter += 1
    num = num // 10   # num = 0

print(counter)  # 22

# 

print()

# Sum of Numbers
num = 101   # --> 598
rev = 0

safe = num

while num > 0:
    rem = num % 10    # 
    rev = rev * 10 + rem   # sum = 598
    num = num // 10   # num = 0

print(rev)  # 598

if safe == rev:  # 101 == 101
    print("Palindrome")
else:
    print("fail")

# 1 to 10000 Palindrome Numbers

# Armstrong Number

# 153 ---> (3*3*3) + (5*5*5) + (1*1*1) = 153
# 8208 ---> (8*8*8*8) + (0*0*0*0) + (2*2*2*2) + (8*8*8*8) = 8208


num = 8208
rev = 0

safe = num

while num > 0:
    rem = num % 10    # 
    rev = rev + rem ** len(str(safe))   # sum = 598
    num = num // 10   # num = 0

print(rev)  # 598

if safe == rev:  # 101 == 101
    print("Armstrong")
else:
    print("fail")

# Plaindrome 1 to 10000 & ARmstrong 1 to 10000