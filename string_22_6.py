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