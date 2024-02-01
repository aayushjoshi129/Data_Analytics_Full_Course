# 1) WAP to find max of 3 numbers

'''
def maxNum(val1,val2,val3):
    if(val1>val2 and val1>val3):
        print("Max Number is ",val1)
    elif(val2>val3):
        print("Max Number is ",val2)
    else:
        print("Max Number is ",val3)

maxNum(31,21,45)
'''

# 2) WAP to create and print a list where the values are square of numbers between 1 and 30

'''
def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)
    print(l)
create_list()
'''

# 3) WAP that takes number as parameter and check if no. is prime or not

'''
n = int(input("Enter n:"))
def isPrime(n):
    if n==1:
        print(n, 'is neither a prime nor composite number')
    elif n==2:
        print(n, 'is a prime number')
    if n>2:
        for i in range(2,n):
            if n%i==0:
                print(n,'is not a prime number')
                break
        else:
            print(n,'is a prime number')

isPrime(n)
'''

# 4) WAP to sum all the numbers in a list

'''
l=[1,2,3,4,5,6,7,8,9]
# sum=0
def sum_List(l):
    sum = 0
    for i in l:
        sum+=i
    return sum;
print(sum_List(l))
'''

# 5) WAP to solve fibonacci series using Recursion

'''
def fibonacci(n):
    a = 0
    b = 1
    for i in range(1,n+1):
        print(a)
        c=a+b
        a=b
        b=c

fibonacci(15)
'''

'''
def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5))
'''