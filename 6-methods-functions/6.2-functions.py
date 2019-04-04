def name_function():
    '''
    DOCSTRING: Information about name_function
    INPUT: no output...
    OUTPUT: Hello
    '''
    print('Hello')

name_function()
# if we call help(name_function), you see documentation above

# function with predefault value
def say_hello(name='NAME'):
    return 'hello  ' + name

result = say_hello('Anna')
print(result)

def add(n1, n2):
    return n1 + n2
result = add(20, 30)
print(result)

# check, that we have a word dog in a string
def dog_check(s):
    return 'dog' in s.lower()
print(dog_check('Dog ran away'))

def pig_latin(word):
    first_letter = word[0]
    # check if val is vowel
    if first_letter in 'aieouy':
        pig_word = word + 'ay'
    else:
        pig_word = word[1] + first_letter + 'ay'
    return pig_word

# if function returns somth, you can simply print what it returns
print(pig_latin('word'))
print(pig_latin('apple'))
