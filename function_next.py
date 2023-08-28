# # 4. With Return Type & with args

# def Girnar(n1 : [int],n2 : [int]) -> [int]:
#     return n1 * n2 + 90 ** 2

# print(Girnar(20,30))   # 8700

# # -----------------------------------------------------

# def series(num):
#     list1 = []
#     for i in range(num):
#         list1.append(i)
#     return list1


# print(series(10))   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def series(num):
    list1 = []
    for i in range(1,num+1):
        yield i

# print(series(10))   # <generator object series at 0x00000239FF219A10>

# for i in series(10):
#     print(i)

print(series(5).__next__())   # 1
print(series(5).__next__())   # 1


x = series(5)

print(x.__next__())  # 1
print(x.__next__())  # 2
print(x.__next__())  # 3
print(x.__next__())  # 4
print(x.__next__())  # 5



# ---------------------------------------------------------

def Royal(fun):
    print("This is Royal Function")
    fun()

def patel():
    print("This is Patel Function")


# x = Royal
# x(patel)

Royal(patel)



# -------------------------------------------

# We can create a FUnction Inside one Function

def Preet(f1):
    def Shah():
        print("This is Shah Function")
        f1()

    return Shah()


@Preet    # Custom Decorators
def Manoj():
    print("This is Manoj Function")


@Preet    # User Defined Decorators
def Shahrukh():
    print("This is Shahrukh Function")
    
# Preet(Manoj)


# OOPs 

@classmethod   # inbuilt Decorators
def Preet():
    pass