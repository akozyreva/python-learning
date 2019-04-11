#  Write a function that returns the lesser of two given numbers if both numbers
#  are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if (a % 2) or (b % 2):
        return a if a < b else b
    else:
        return b if b > a else a

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

# ANIMAL CRACKERS: Write a function takes a two-word string and
# returns True if both words begin with same letter
def animal_crackers(text):
    whitespace_index = text.index(" ")
    return text[whitespace_index + 1] == text[0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))

# MAKES TWENTY: Given two integers, return True if the sum of the integers
# is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1,n2):
    if (n1 == 20) or (n2 == 20) or ((n1 + n2) == 20):
        return True
    return False

print(makes_twenty(20,10))
print(makes_twenty(2,3))

# OLD MACDONALD: Write a function that capitalizes
# the first and fourth letters of a name
def old_macdonald(name):
    str_list = list(name)
    str_list[3] = str_list[3].upper()
    str_list[0] = str_list[0].upper()
    name = "".join(str_list)
    return name
print(old_macdonald('macdonald'))

#  MASTER YODA: Given a sentence, return a
#  sentence with the words reversed
def master_yoda(text):
    text = text.split()[::-1]
    text = " ".join(text)
    return text
print(master_yoda('I am home'))
print(master_yoda('We are ready'))

#  ALMOST THERE: Given an integer n, return
# True if n is within 10 of either 100 or 200
def almost_there(num):
    if (abs(100 - num) <= 10) or (abs(200 - num) <= 10):
        return True
    else:
        return False
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

# Given a list of ints, return True if
# the array contains a 3 next to a 3 somewhere.
print("has_33")
def has_33(nums):
    for index, val in enumerate(nums):
        if index == len(nums) - 1:
            break
        elif val == 3 and nums[index+1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
