list1 = [j for j in range(1,201)]

num = 106

# if num in list1:
#     print('Found')

size = 200

min = 0
max = size-1


while min<=max:
    mid = (min + max) // 2

    if list1[mid] == num:
        print('Element is Found')
        break
    elif list1[mid] < num:
        min = mid + 1

    elif list1[mid] > num:
        max = mid - 1

else:
    print("Not Found")