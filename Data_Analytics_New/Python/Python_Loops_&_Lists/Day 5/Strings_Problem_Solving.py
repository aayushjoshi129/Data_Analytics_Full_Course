# 1) WAP to take input from user as a string then, reverse it.

'''
string = input("Enter your string: ")
print("Your string is ", string)
print("Reversed string is ", (string[::-1]) )
'''

# 2) WAP to check if a string contains only digits.

'''
a = input("Enter anything here: ")
if(a.isdigit()==True):
    print(a," It contains only digits")
else:
    print(a," It contains other than digits")
'''

# 3) WAP to check if a string is palindrome.

'''
string = input("Enter your string: ")
rev_string = string[::-1]
if(string==rev_string):
    print(string,"is a palindrome string")
else:
    print(string, "is not a palindrome string")
'''

# 4) WAP to find no. of vowels in a string.

'''
string = input("Enter your string: ")
vowels = 0
for i in string:
    if i.upper() in ('A','E','I','O','U'):
        vowels+=1
print("No of vowels in",string, "is ", vowels)
'''

# 5) WAP to check if every word in a string begins with capital letter.

'''
string = input("Enter your string: ")
if string.istitle() == True:
    print(string, "every word begins with capital letter")
else:
    print(string, "every word does not begins with capital letter")
'''