from collections import Counter

l = [1, 2, 1, 4, 1, 5, 5, 5, 7, 8]

# it counts number of occurences of every el in list
print(Counter(l))

s = 'grhgbdjhgougnkfngkjfd'
# it counts number of occurences of string
print(Counter(s))

words_s = "How many times word of word of word appears many"
# create a list of objects, spliting them by whitespace
words = words_s.split()
# counts the counts of occurences
print(Counter(words))

# and use special methods
c = Counter(words)
# show most common words. arg - number of showing most common- 2 words, 3, etc.
print(c.most_common(2))
# show the total number of words
print(sum(c.values()))
