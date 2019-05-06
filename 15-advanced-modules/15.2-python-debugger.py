import pdb

x = [1, 2, 4]
y = 2
z = 3

print(z)

# and putting it here allows you to undertand, which values have variables and so on
pdb.set_trace()
# it's error!
result = y + x
print(result)
