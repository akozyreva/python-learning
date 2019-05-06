s = 'hello world!'

# counts occurencies of letter o
print(s.count('o'))

# find 1 occurency of letter o and return index
print(s.find('o'))

s = 'hello'

# returns true, if there are only numbers and letters
print(s.isalnum())
# returns true, if there are only letters in string
print(s.isalpha())
# retur true, if there are any spaces
print(s.isspace())
print(s.endswith('o'))

s = 'blablbalabla'
# returns before 1 occurency, occurency and the last part as a tuple
print(s.partition('a'))
