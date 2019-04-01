x = 0
while x < 5:
    print(f'The current val of x is {x}')
    x += 1
else:
    print('Loop ended')

#  example with pass
# pass uses for simply passing execution of for loop
x = [1, 2, 3]
for i in x:
    # comment
    pass
print('end of my script')

myString = 'Sammy'
for letter in myString:
    if letter == 'a':
        continue
    print(letter)
for letter in myString:
    if letter == 'a':
        break
    print(letter)
