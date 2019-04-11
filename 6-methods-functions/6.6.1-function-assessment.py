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
        if a == 11 or b == 11 or c == 11:
            return a + b + c - 10
        else:
            return "BUST"

print(blackJack(5,6,7))
print(blackJack(9,9,9))
print(blackJack(9,9,11))
