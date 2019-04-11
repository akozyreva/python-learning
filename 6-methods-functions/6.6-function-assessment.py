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
