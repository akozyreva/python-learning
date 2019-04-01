my_list = [1, 2, 3]
my_list = ['String', 100, 23.2]

print(len(my_list))
mylist = ['one', 'two', 'three']

# from 1 element to the end
print(mylist[1:])
another_list = ['four', 'five']
new_list = mylist + another_list
print(new_list)
new_list[0] = 'ONE'
print(new_list)
# append a new item to the list
new_list.append('six')
new_list.append('seven')
print(new_list)
# remove last element from the list
new_list.pop()
print(new_list)
# we can save popped item
popped_item = new_list.pop()
print(popped_item)
# you can pass an index of removing item into pop function
print(new_list.pop(1))

# sorts and reverse
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
# sort method doesn't return anyting, it only sorts
# so, it will be an error my_sorted_list = new_list.sort()
# example bellow should work
# new_list.sort()
# my_sorted_list = new_list
new_list.sort()
print(new_list)

# reverse method - from the end to the beginning
num_list.reverse()
print(num_list)
