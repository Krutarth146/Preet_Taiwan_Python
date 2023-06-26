l1 = [10,20,30,40]

print(l1)

l2 = [[10,20,30], 
      [40,50,60], 
      [70,80,90]]

print(l2[2][1])  # 80

for preet in l2: 
    print(preet)   # [10, 20, 30]    [40,50,60]   [70,80,90]


for d in l2:
    for j in d:
        print(j,end=' ')
    print()


# 10 20 30
# 40 50 60
# 70 80 90
internal_count = 0
External_count = 0

for i in range(len(l2)):   # for rows--> 3    ---> 0 to 2   # 0
    for j in range(len(l2[i])): # for columns  # 0 1 2
        print(j,end=' ')
        internal_count +=1 
    External_count+=1

print()
print(internal_count)  # 9
print(External_count)  # 3


l2 = [[10,20,30], 
      [40,50,60], 
      [70,80,90]]

sum = 0
for i in range(len(l2)):
    for j in range(len(l2[i])):
        if i==j:
            sum += l2[i][j]
print(sum)  # 150

# H.w 
# 1. 
# 30 + 50 + 70 ----> 150


# 2. 
# 10 20 30 60 50 40 70 80 90  -- (Snake Type)


# 3.
# Sorting in 2d Array



dict1 = {'Address' : "Ahm"}  # dictionary

print(dict1['Address'])

l3 = [[(20,40), (10,90)], {"Address" : [10, 'Preet', 90, [30,50,80]], 'Manoj' : 900} ]

print(l3[1])  # {'Address': [10, 'Preet', 90, [30, 50, 80]], 'Manoj': 900}
print(l3[-1])  # {'Address': [10, 'Preet', 90, [30, 50, 80]], 'Manoj': 900}


print(l3[-1]["Address"])  # [10, 'Preet', 90, [30, 50, 80]]
print(l3[-1]["Address"][-1])  # [30, 50, 80]
print(l3[-1]["Address"][-1][1])  # 50
print(l3[-1]["Address"][-1][-2])  # 50
print(type(l3[-1]["Address"][-1][-2]))  # <class 'int'>

