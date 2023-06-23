str1 = "ROyal Techno is Best Institute Ever123."

print(str1.capitalize())  # Royal techno is best institute ever123.
print(str1.casefold())   # royal techno is best institute ever123.
print(str1.lower())   # royal techno is best institute ever123.
print(str1.upper())   # ROYAL TECHNO IS BEST INSTITUTE EVER123.
print(str1.title())   # Royal Techno Is Best Institute Ever123.
print(str1.swapcase())   # roYAL tECHNO IS bEST iNSTITUTE eVER123.
print(str1.islower())   # False
print(str1.isupper())   # False
print(str1.istitle())   # False


print(len(str1))   # 39 
print(str1.center(50, '*'))   # *****ROyal Techno is Best Institute Ever123.******

print(str1.count('i',0,15))  # 1  # Returns Frequency

# print(str1.index('i',0,8))  # Error
print(str1.find('i',0,8))  # -1   Returns -1 if Element is Not Found

str1 = "ROyal Techno is \t Best Institute Ever123."
# print(str1.rfind('i'))  # 25

# print(str1.endswith("23"))  # False
print(str1.expandtabs(16))  # ROyal Techno is                  Best Institute Ever123.


str1 = "Ståle"

print(str1.encode())  # b'St\xc3\xa5le'

print(str1.encode(encoding="ASCII", errors="namereplace"))  # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str1.encode(encoding="ASCII", errors="replace"))  # b'St?le'
print(str1.encode(encoding="ASCII", errors="ignore"))  # b'Stle'
print(str1.encode(encoding="ASCII", errors="xmlcharrefreplace"))  # b'St&#229;le'
print(str1.encode(encoding="ASCII", errors="backslashreplace"))  # b'St\\xe5le'
print(str1.encode(encoding="latin"))  # b'St\xe5le'


str1 = "LIon is the king the of the JUngle"

str1 = str1.replace("the",'a',1)
print(str1)   # LIon is a king of the JUngle


list1 = str1.split()
 
print(list1)  # ['LIon', 'is', 'a', 'king', 'the', 'of', 'the', 'JUngle']

list1.reverse()
for i in range(len(list1)):
    if list1[i] == 'the':
        list1[i] = 'a'
        break
print(list1)
list1.reverse()
print(list1)

str1 = '_'.join(list1)
print(str1)   # LIon is a king the of a JUngle

str1 = "{} is the {} of Jungle123."
print(str1.format("Lion", 'King'))   # Lion is the King of Jungle123.

str1 = "{1} is the {0} of Jungle123."
print(str1.format('King', 'Lion'))  # Lion is the King of Jungle123.

str1 = "{animal} is the {designation} of Jungle123."
print(str1.format(animal = "Lion", designation = "King"))  # Lion is the King of Jungle123.


# Format_map

dict1 = {'Designation' : "King" , 'Name' : "Tiger" }

str1 = "{Name} is the {Designation} of Jungle123."
print(str1.format_map(dict1))  # Tiger is the King of Jungle123.

str1 = "Tiger"
print(str1.isalnum())  # True
print(str1.isalpha())
print(str1.isascii())
print(str1.isdecimal())
print(str1.isdigit())
print(str1.isnumeric())
print(str1.isidentifier()) 
print(str1.isspace()) 
 

str1 = "Tiger is KIng of Jungle."
print(len(str1))  # 24
print(str1.ljust(40, '#'))
print(str1.rjust(40, '#'))


str1 = "               Tiger is KIng of Jungle.          "
print(str1.lstrip())   # Tiger is KIng of Jungle.
print(str1.rstrip())   #      Tiger is KIng of Jungle.
print(str1.strip())   # Tiger is KIng of Jungle.

str1 = "Tiger is KIng of Jungle."
table = str1.maketrans("KIng", "kiNG", '.')
print(table)  # {75: 107, 73: 105, 110: 78, 103: 71, 46: None}

print(str1.translate(table))   # TiGer is kiNG of JuNGle

print(str1.removeprefix('K'))   # Tiger is KIng of Jungle.
print(str1.removesuffix('le.'))   # Tiger is KIng of Jung

print(str1.startswith('Ti'))  # True
str1 = "Tiger\nis\nKIng of Jungle."
print(str1)

# Tiger
# is
# KIng of Jungle.
print(str1.splitlines())  # ['Tiger', 'is', 'KIng of Jungle.']

print(str1.swapcase())   # kiNG OF jUNGLE.

str2 = '900'
print(str2.zfill(5))  # 00900

print("%c" %'A')  # A
print("%c" %67)  # C
print("%s" %"Preet")  # Preet
print("%d" % 78)   # 78
print("%.2f" % 21.90)  # 21.90


# String Methods End ----------------------------