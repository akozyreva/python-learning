l = [1, 2, 3, 4]

# return position of el in the list
l.count(4)  # 3

x = [1, 2, 3]
x.append([4, 5])
# it appended only 1 element, so 4 el is the list
print(x)  # [1, 2, 3, [4, 5]]

# extend method allows to add new list as a part of previous one
x = [1, 2, 3]
x.extend([4, 5])
print(x)  # [1, 2, 3, 4, 5]
