# PAPER DOLL: Given a string, return a string where for every
# character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    new_str = ''
    for i in text:
        new_str += i * 3
    return new_str

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# BLACKJACK: Given three integers between 1 and 11, if their sum
# is less than or equal to 21, return their sum. If their sum exceeds 21
# and there's an eleven, reduce the total sum by 10. Finally, if
# the sum (even after adjustment) exceeds 21, return 'BUST
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackJack(a, b, c):
    if a + b + c <= 21:
        return a + b + c
    elif a + b + c >= 21:
        if 11 in (a, b, c):
            return a + b + c - 10
        else:
            return "BUST"

print(blackJack(5,6,7))
print(blackJack(9,9,9))
print(blackJack(9,9,11))


# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending
# to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

print("summer_69")
def summer_69(arr):
    sum = 0
    for index, val in enumerate(arr):
        if val != 6:
            sum += val
        else:
            for new_val in arr[index + 1: ]:
                if new_val != 9:
                    arr.remove(new_val)
                else:
                    arr.remove(new_val)
                    break
        print(arr)
    return sum

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


# SPY GAME: Write a function that takes in a list of integers and returns
# True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
print("spy_game")
def spy_game(nums):
    # find pos of 7
    index_7 = nums.index(7)
    # find the smallest poisition of 0
    index_01 = nums.index(0)
    if index_01 > index_7:
        return False
    else:
        for i in nums[index_01 + 1: index_7]:
            if i == 0:
                return True
        return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]) )

# COUNT PRIMES: Write a function that returns the number of prime
# numbers that exist up to and including a given number
# count_primes(100) --> 25
# 2 3 5 7 11 13 etc.
# By convention, 0 and 1 are not prime.
# I use algorithm  - Sieve of Eratosthenes
def count_primes(num):
    num_list = []
    for i in range(2, num + 1): num_list.append(i)
    count = 2
    for i in num_list:
        for j in num_list[count: ]:
            if j % count == 0:
                num_list.remove(j)
        count += 1
    print(len(num_list))
count_primes(100)

#  PRINT BIG: Write a function that takes in
#  a single letter, and returns a 5x5 representation of that letter
# HINT: Consider making a dictionary of possible patterns, and mapping
# the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".
def print_big(letter):
    a = '{:>3} '.format('*') + '\n' + ' {:>1} '.format('*') + ' {:>1} '.format('*') + '\n *****' + '\n *   *'
    print(a)
    pass
print_big('a')

def printBig(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
printBig('B')
