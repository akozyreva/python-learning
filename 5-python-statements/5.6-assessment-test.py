# Use for, .split(), and if to create a Statement that will print
# out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if 's' in word[0]:
        print(word)

# Use range() to print all the even numbers from 0 to 10.
print([x for x in range(0,11,2)])

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if not(len(word) % 2):
        print(word+" even")

# Write a program that prints the integers from 1 to 100. But for multiples of
# three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for x in range(1,50):
    if (not(x % 3)) and (not(x % 5)):
        print ("FizzBuzz",end=' ')
    elif not(x % 5):
        print ("Buzz",end=' ')
    elif not(x % 3):
        print("Fizz",end=' ')
    else:
        print(x,end=' ')

# Use List Comprehension to create a list of
# the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
results = [y for x in st.split() for y in x[0]]
print(results)
