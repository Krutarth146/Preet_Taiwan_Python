d2 = [
    [10,90,89],
    [67,45,21],
    [89,78,55]
]

d1 = []

for sublist in d2:
    # print(i)
    for ele in sublist:
        # print(ele,end=' ')   # 10 90 89 67 45 21 89 78 55 
        d1.append(ele)
print(d1)  # [10, 90, 89, 67, 45, 21, 89, 78, 55]

d1.sort()
print(d1)  # [10, 21, 45, 55, 67, 78, 89, 89, 90]

# Method-1

d4 = []
k = 0

for row in range(len(d2)):  # 3  ---> 0 to 2
    temp = []
    for col in range(len(d2[row])):
        temp.append(d1[k])
        k+=1
    print(temp)
    d4.append(temp)

print(d4)  # [[10, 21, 45], [55, 67, 78], [89, 89, 90]]

choice = "patel"

match choice:
    case 0: print("Hello")

    case 9.8 : pass
    
    case "patel": print("Enter Valid CHoice Patel")

    case other: print("Enter Valid CHoice")
    