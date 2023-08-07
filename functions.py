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


# # 2. With Return Type & w/o args

def preet():
    return 90

print(preet())   # 90


def patel():
    a,b,c = 90,33,21
    return a+b-c

print(patel())   # 102


def man():
    return "Preet", [10,20,30], (90,89,89), {10,20}

print(man())   # ('Preet', [10, 20, 30], (90, 89, 89), {10, 20})

x = man()
print(x)


# 3. Without Return Type & with args

def Shah(x=89,y=10,z = 77):
    print(x+y+z)

Shah()   # 176



def kru(man, woman, *preet, shah=90):   # Args
    print(preet)
    print(type(preet))
    for i in preet:
        print(i)
    print(preet[2])

kru(10,90,[30,90],"str1",{'Preet' : "Name"})   # ([30, 90], 'str1', {'Preet': 'Name'})


def royal(rt, *args, **kwargs):   # kwargs
    print(kwargs)
    print(type(kwargs))

    # for i in kwargs.values():
    for i in kwargs.items():
        print(i)


royal(10,20,30,40,name = "Preet", address = "Taiwan")

# ('name', 'Preet')  ('address', 'Taiwan')
# <class 'dict'>

# 4. With Return Type & with args