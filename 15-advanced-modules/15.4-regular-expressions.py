import re

patterns = ['term1', 'term2']
text = "This is a string with term1, but not with the other term"


# show occurencies
for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' %(pattern, text))

    # Check for match
    if re.search(pattern, text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')

match = re.search(patterns[0], text)
# it's match object
print(type(match))

# it shows index of the match
print(match.start(), match.end())

split_term = '@'
phrase = 'What is your email, is it hello@gmail.com?'
# it splits phrase, using @ and creates a list
print(re.split(split_term, phrase))

# find all matches
print(re.findall('test', 'is\'s testing phrase test and one more test'))
