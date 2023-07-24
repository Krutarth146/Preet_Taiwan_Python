list1 = [(10,90), (32,4), (222,1), (11,90), (55,999)]

n = 2

# [(10,90), (11,90)]

res = []

for subtup in list1:   # subtup = (10, 90)
    flag = False
    for ele in subtup:
        if len(str(ele)) == 2:
            flag = True
        else:
            flag = False
            break

    if flag == True:
        res.append(subtup)
print(res)  # [(10, 90), (11, 90)]




t1 = [(10,90), (78,32), (21,3), (55,34)]

# Sort By Second element

# [(21,3), (78,32), (55,34), (10,90)]

for i in range(len(t1)):
    for j in range(i+1, len(t1)):
        if t1[i][-1] > t1[j][-1]:
            t1[i], t1[j] = t1[j], t1[i]

print(t1)   # [(21, 3), (78, 32), (55, 34), (10, 90)]