# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# list1 = ["Manoj", "Exercises", "Mithil", "AO", "Al_Ma", "Zara", "Exercis"]
# Longest word: Exercises
# Length of the longest word: 9


# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
 
# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2


str1 = 'thequickbrownfoxjumpsoverthelazydog'

s1 = set(str1)  # Removes Duplicates

print(s1)

for ele in s1:
    if str1.count(ele) > 1:
        print(ele,'--->',str1.count(ele))