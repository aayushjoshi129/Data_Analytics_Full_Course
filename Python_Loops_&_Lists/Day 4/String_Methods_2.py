# endswith - Returns True if the string ends with the specified value

'''
a='Harry Potter'

print(a.endswith('r'))
print(a.endswith('P'))
'''

# startswith - Returns True if the string starts with the specified value

'''
a='Harry Potter'

print(a.startswith('P'))
print(a.startswith('H'))
'''

# swapcase - lower case becomes upper case and vice versa

'''
a='Harry Potter'

print(a.swapcase())
'''

# strip - Returns a trimmed version of the string

'''
b='     Harry Potter    '
c='********** Happy World ..............'

print(b.strip())
print(c.strip('*'))
'''

# split - splits the string at the specified seperator, and returns a list

'''
d='#OOFD#BOYCOTT#HONEY#LOVE'

print(d.split('#'))
'''

# ljust - Returns a left justified version of the string

'''
a='Harry Potter'

print(a.ljust(20, '*'))
'''

# rjust - Returns a right justified version of the string

'''
a='Harry Potter'

print(a.rjust(20, '.'))
'''

# replace() - Returns a string where a specified value is replaced with a

'''
a='Harry Potter'

print(a.replace('H', 'G'))
'''

# rindex() - Searches the string for a specified value and returns the last position of where it was found

'''
a='Harry Potter'

print(a.rindex('r'))
'''

# rfind() - Searches the string for a specified value and returns the last position of where it was found

# '''
a='Harry Potter'

print(a.rfind('r'))
# '''