# function takes a string
# and if it's even, then letter is uppercase, otherwise - lowercase
def myfunc(word):
    new_word=''
    for index, letter in enumerate(word.lower()):
        if index%2:
            new_word += letter.upper()
        else:
            new_word += letter.lower()
    return new_word

print(myfunc('Anthropomorphism'))
# Output: 'aNtHrOpOmOrPhIsM'
