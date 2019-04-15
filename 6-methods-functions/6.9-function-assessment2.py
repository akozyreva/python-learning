import math
import string
# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return rad ** 3 * math.pi * 4 / 3

print(vol(2))

# Write a function that checks whether
# a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    return low < num < high
print(ran_check(5,2,7))

# Write a Python function that accepts a string and calculates the number
# of upper case letters and lower case letters.
#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output :
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
#HINT: Two string methods that might prove useful: .isupper() and .islower()
def up_low():
    upper_counter, lower_counter = 0, 0
    s = str(input('Insert a string, please '))
    if not len(s):
        s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
    for i in s:
        if i.isupper():
            upper_counter += 1
        elif i.islower():
            lower_counter += 1
    return upper_counter, lower_counter
print(up_low())

# Write a Python function that takes a list
# and returns a new list with unique elements of the first list.
# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24
def multiply(numbers):
    mult_num = 1
    for i in numbers: mult_num *= i
    return mult_num
print(multiply([1, 2, 3, -4]))

# Write a Python function that checks whether a passed in string is palindrome or not.
# Note: A palindrome is word, phrase, or sequence that
# reads the same backward as forward, e.g., madam or nurses run.
def palindrome(s):
    return s == s[::-1]
print(palindrome('helleh'))

# Hard:
# Write a Python function to check whether a string is pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
# Hint: Look at the string module
# ispangram("The quick brown fox jumps over the lazy dog") => True

def ispangram(str1, alphabet=string.ascii_lowercase):
    counter = 0
    unique_str = set(str1.lower().replace(" ", ""))
    for i in unique_str:
        if i in alphabet:
            counter += 1
    return counter == len(alphabet)
print(ispangram("The quick brown fox jumps over the lazy dog"))
