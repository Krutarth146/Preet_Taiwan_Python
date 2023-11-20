# Dictionary: 

dict1 = {}
print(type(dict1))  # <class 'dict'>

set1 = {10}
print(type(set1))  # <class 'set'>

dict2 = {'Name' : 'Preet', 'Name' : 'ShreySir', 'Roll' : 902, 'isActive' : True, 'address' : {'city' : ['Gnr', 'Ahm']}}

print(dict2)   # {'Name': 'ShreySir', 'Roll': 902, 'isActive': True, 'address': {'city': ['Gnr', 'Ahm']}}

set2 = set()
print(type(set2))   # <class 'set'>


dict2 = {'Name' : 'Preet', 'Name' : 'ShreySir', 'Roll' : 902, 'isActive' : True, 'address' : [{'city' : ['Gnr', 'Ahm']}]}
 
print(dict2)  # {'Name': 'ShreySir', 'Roll': 902, 'isActive': True, 'address': {'city': ['Gnr', 'Ahm']}}

print(dict2['Name'])  # ShreySir
print(dict2['Roll'])  # 902
print(dict2['address'])  # {'city': ['Gnr', 'Ahm']}
# print(dict2['address']['city'])  # ['Gnr', 'Ahm']
# print(dict2['address']['city'][1])  # Ahm
# print(dict2['address']['city'][1][1])  # h
print(dict2['address'][0]['city'][1][1])   # h

# Dict ----> Ordered, Not Indexed, Mutable (Changeble), Don't Allow Duplicates

dict2 = {'Name' : 'Preet', 'Roll' : 90}

print(dict2['Name'])   # Preet
print(dict2.get('Name'))   # Preet
print(dict2.get('address'))   # None


for i in dict2:
    print(i)   # Name, Roll


for k in dict2.keys():
    print(k)

for k in dict2.values():
    print(k)  # Preet  90

for d in dict2.items():
    print(d)  # ('Name', 'Preet')   ('Roll', 90)

for key, value in dict2.items():
    print(key, '------>', value)  # ('Name', 'Preet')   ('Roll', 90)

    if value == 'Preet':
        print(key)  # Name


dict2.update({'Address' : 'Ahm'})

print(dict2)   # {'Name': 'Preet', 'Roll': 90, 'Address': 'Ahm'}



dict2['Name'] = 'Royal'
print(dict2)   # {'Name': 'Royal', 'Roll': 90, 'Address': 'Ahm'}

dict2['marks'] = 900

print(dict2)   # {'Name': 'Royal', 'Roll': 90, 'Address': 'Ahm', 'marks': 900}

# del dict2

del dict2['marks']

print(dict2)   # {'Name': 'Royal', 'Roll': 90, 'Address': 'Ahm'}


removed_val = dict2.pop('Roll')
print(removed_val)   # 90
print(dict2)   # {'Name': 'Royal', 'Address': 'Ahm'}


dict2.popitem()
print(dict2)   # {'Name': 'Royal'}


tup1 = ('Person1', 'p2', 'p3')
preet = dict.fromkeys(tup1, None)

print(preet)   # {'Person1': None, 'p2': None, 'p3': None}



dict4 = {'Name': 'Royal', 'Roll': 90, 'Address': 'Ahm'}

dict4.setdefault('Address', 'Nadiad')
dict4.setdefault('std', 10)

print(dict4)   # {'Name': 'Royal', 'Roll': 90, 'Address': 'Ahm', 'std': 10}


from bidict import bidict

d5 = bidict(dict4)   # bidirectional Dict
print(d5)   # bidict({'Name': 'Royal', 'Roll': 90, 'Address': 'Ahm', 'std': 10})

d6 = d5.inverse

print(d6)   # bidict({'Royal': 'Name', 90: 'Roll', 'Ahm': 'Address', 10: 'std'})

print(d6['Royal'])   # Name


str1 = "MISSISSIPI"

# ans = {'M' : 1, 'I' : 4, 'S' : 4, 'P' : 1}

ans = {}

for c in set(str1):   # {'M', 'I', 'S', 'P'}
    # ans[c] = str1.count(c)
    if c not in ans:
        ans[c] = 1
    else:
        ans[c] += 1

print(ans)   # {'I': 1, 'S': 1, 'P': 1, 'M': 1}

