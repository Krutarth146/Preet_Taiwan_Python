# Functions

# 1. Inbuilt Func.   ---> print(), input(), len(), sum()
# 2. User Defined Functions

# def Preet():
#     sdvsdvsd
#     varsdv
#     sd
#     vs
#     dv
#     sdv
#     s

# 1. Func. Defination
# 2. Func. Calling


def preet():   # Func. Defination
    print("Hello I am Preet Function")

preet()   # Func. Calling


# Func. Types

# 1. Without Return Type & w/o args
# 2. With Return Type & w/o args
# 3. Without Return Type & with args
# 4. With Return Type & with args

# 1. Without Return Type & w/o args

def shah():
    a,b,c = 10,20,30
    print(a+b+c)

shah()   # 60


# 2. With Return Type & w/o args

x = 90   # Global Variable

# def Manoj():
#     x = 40    # Local Variable
#     x+=10     # 50
#     print(x)  # 50

# Manoj()
# print(x+10)   # 100


def dev():
    global x   # 90
    x+=10   # 100
    print(x)  # 100

dev()
print(x+20)  # 120