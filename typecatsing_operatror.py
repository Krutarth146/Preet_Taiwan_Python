# Typecasting -> To convert One Datatype into another datatype

# 1. Implicit Typecasting   2. Explicit TYpecasting


x = True
y = 90

print(x+y)  # 91   # Implicit Typecasting

v = 90.89
w = "89"
print(int(w))   # 89

# e = "Preet"
# print(int(e))  # Generates Error


d = '82.90'

print(int(float(d)))   # 82   # Explicit TYpecasting

x = 90.00001
import math
print(math.ceil(x))   # 91
print(math.floor(x))   # 90

print(-18//4)   # -5



# Operators

# 1. Arithmetic Operator
# 2. Assignment o/p
# 3. Logical o/p
# 4. Relational o/p  (Comparison O/p)
# 5. Membership o/p
# 6. Identity O/p
# 7. Bitwise O/p


# 1 .Arithmetic OPerators   + - * / // % **

print(90 + 89)
print(2**3**2)   # 512   (Right to left)


# 2. Assignment O/p   (Right to Left) (Low Priority)
# = += -= *= /= //= %= <<= >>= &= |= ^=

d = 90
d+=2   # ---> d = d + 2   // 92
d*=5   # 460 = 92 * 5
d//=2  # 230
d%=4   # 2

print(d)   # 2


# 3. Logical O/p   and   or   not


# # And Table  (a*b)
# i/p   i/p    o/p
#  0     0      0
#  1     0      0
#  0     1      0
#  1     1      1


# # or Table  (a+b)

# i/p   i/p    o/p
#  0     0      0
#  1     0      1
#  0     1      1
#  1     1      1


# # xor Table  (Same -> 0)

# i/p   i/p    o/p
#  0     0      0
#  1     0      1
#  0     1      1
#  1     1      0

# # Not 

# i/p   o/p
#  0     1
#  1     0


# If Else

name = input("Enter Name: ")
age = int(input("Enter age: "))

if age > 18:
    print(f"{name} is Eligible for voting.")
else:
    print(f"{name} is Not Eligible for voting. You need {18-age} years.")

# Take 3 subjects as I/p and calculate Total , avg.
    # also find the grade -> 100 to 80 ----> A grade
    #                         60 to 80 ----> B grade
    #                         40 to 60 ----> C Grade


num = 0
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    if type(num) == str:
        print("Negative")
    else:
        pass