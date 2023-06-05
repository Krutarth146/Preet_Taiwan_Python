# # Operators 22/04/23

# # Bitwise O/p   &  |  ^  <<  >> 

# # XOR  (Same -> 0)

# # i/p  i/p  o/p
# #  0    0    0
# #  1    1    0
# #  1    0    1
# #  0    1    1

# # Decimal to Binary ---->   1. 4509   2. 3411   3. 512
# # Binary to Decimal ---->   1. 000011110101    2. 0011010101010101  3. 110110  4. 10010

# print(23 & 56)  # 16
# print(23 | 56)  # 63
# print(23 ^ 56)  # 47
# print(23 << 2)  # 92
# print(23 >> 2)  # 5


# # Loops
# # 1. Entry Control loops   ----> for, while

# # arr1 = [10,20,40,90] 
# list1 = [10,20,89.90, "Preet", 'P', True, 89+9j, [10,20,30,40], {10,20,30}, (30,40,50,60), {"Name" : "Preet", 'age' : 90}]


# # Linear Search

# # for(i=1;i<=5;++i)

# for _ in range(5):   # start - default - 0, End- 5 (n-1) = 4 
#     print(_)

# for u in range(12,19):   # start - 12, End - 18
#     print(u,end=' ')   # 12 13 14 15 16 17 18

# print()
# for q in range(-5,-1):
#     print(q,end=' ')  # -5 -4 -3 -2

# print()
# for q in range(-1,-5):
#     print(q,end=' ')    # blank

# print()
# for q in range(19,12):
#     print(q,end=' ')    # blank

# print()
# for q in range(5,21,1):   # start-5, end-20, step-1
#     print(q,end=' ')    # 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# print()
# for q in range(5,21,3):   # 
#     print(q,end=' ')    # 5 8 11 14 17 20

# print()
# for q in range(21,5,3):   # 
#     print(q,end=' ')    # blank

# print()
# for q in range(21,5,-1):   
#     print(q,end=' ')    # 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6

# print()
# for q in range(21,5,-3):   
#     print(q,end=' ')    # 21 18 15 12 9 6

# print()
# for q in range(-2,2,2):   
#     print(q,end=' ')    # -2 0






# # Linear Search

# list1 = [10,20,89.90, "Preet", 'P', True, 89+9j, [10,20,30,40], {10,20,30}, (30,40,50,60), {"Name" : "Preet", 'age' : 90}]


# for y in list1:
#     print(y,end=' ')  # 10 20 89.9 Preet P True (89+9j) [10, 20, 30, 40] {10, 20, 30} (30, 40, 50, 60) {'Name': 'Preet', 'age': 90}


# user_need = int(input("Enter User Need: "))
# preet = 0
# for i in list1:
#     if i == user_need:
#         preet = 1
#         break
#     else:
#         preet = 0


# if preet == 1:
#     print("Element is Found")
# else:
#     print("Element is Not Found")

# # ---------------------

# # Membership o/p    --->    in, not in

# if user_need in list1:
#     print("Element is Found")
# else:
#     print("Element is Not Found")



# # Relational O/p  // Comparison O/p  == != < > <= >=


# # x = 10
# # x == 10


# # Identity O/p   is, is not

# x = 90
# y = 90


# if x is y:
#     print(x is y)

# if x == y:
#     print(x ,"==", y)

# list1 = [10,20,30]
# list2 = [10,20,30]

# if list1 == list2:
#     print("list1 == list2")  # list1 == list2

# if list1 is list2:
#     print("list1 is list2")
# else:
#     print("Not")   # Not

# print(id(list1))  # 2473835354368
# print(id(list2))  # 2473835511680

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# insert into dictionary
def insert_dict(key, value, dict):
    
    # Your code here
    dict[key] = value
    

# deleting from dictionary
def del_dict(key, dict):
    
    # Your code here
    if key:
        return 0
    del dict[key]
    return 1
    

# print marks of required name
def print_dict(key, dict):
    
    # Your code here
    if key:
        return 0
    print("Marks of",key,"is",dict[key])
    
    
    

#{ 
 # Driver Code Starts.
# Driver code
def main():
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        n = int(input())
        
        i = 0
        dict = {}
        while i < n:
            flag = False
            delete = False
            query = input().split()
            if(query[0] == 'i'):
                insert_dict(query[1], query[2], dict)
                print ("Inserted")
            
            if(query[0] == 'd'):
                if del_dict(query[1], dict) is False:
                    print ("-1")
                else:
                    print ("Deleted")
            
            if(query[0] == 'p'):
                if(print_dict(query[1], dict) is False):
                    print ("-1")
                    
            i+=1
            
        testcase -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends