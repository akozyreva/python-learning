s = 'hello'
for letter in s:
    print(letter)

# but we can't iterate through next, only through for loop
# but what we can do is
s_iter = iter(s)
# and now iteration works
print(next(s_iter))
# show h
print(next(s_iter))
# show e
