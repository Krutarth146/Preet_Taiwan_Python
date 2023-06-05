
def insert_dict(key, value, dict):

    # Your code here
    dict[key] = value

def del_dict(key, dict):
    
    if key:
        del dict[key]
        return 1
    else:
        return 0
    
def print_dict(key, dict):
    
    if not(key):
        return 0
    else:
        print("Marks of",key,"is",dict[key])
    


dict = {}
insert_dict("geeks",100,dict)
print(del_dict("geeks", dict))
print(dict)


env_list =[lambda arg = x : arg *5 for x in range(1,6)]
for i in env_list:
    print(i())
    
print()
print()
def evn(arg):
    for x in range(15,20):
        yield x*arg

for g in evn(5):
    print(g)