# 1) WAP to get Fibonacci Series upto 10 numbers

'''
nterms = int(input("Upto How many terms? "))
count=0
if nterms==0:
    print("Enter a Valid number")
elif nterms==1:
    print("Fibonacci Series upto ",nterms, "is ", nterms)
else:
    num1=0
    num2=1
    # print(num1)
    # print(num2)
    # for i in range(1, nterms+1):
    while count < nterms:
        print(num1, end=" ")
        num3 = num1 + num2
        num1=num2
        num2=num3
        count+=1
'''

# 2) WAP to check if a number is prime or not

'''
n = int(input("Enter no. to check prime or not? "))
flag = 0
if n == 1:
    print(n, "is neither prime nor composite")
else:
    for i in range(2,n):
        if n%i == 0:
            flag = 0
            break
        else:
            flag = 1
if flag == 1:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
'''

# 3) WAp to find a palindrome of a strings

'''
n = int(input("Enter a number to check it is a palindrome or not: "))
tmp = n
rev = 0
while tmp > 0:
    d = tmp % 10    # tmp=983 || digit=3
    rev = rev*10 + d
    tmp //= 10
if n == rev:
    print(n,rev, "is a palindrome number")
else:
    print(n,rev, 'is not a palindrome number')
'''

