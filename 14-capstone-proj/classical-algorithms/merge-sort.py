import random
# let's create generator for list sorting


def create_random_list(low, high):
    len = high - low
    for x in range(len):
        yield random.randint(low, high * low)


unsorted_list = list(create_random_list(2, 10))


def merge_sort(array):
    print("array",array)
    if len(array) <= 1:
        return array

    midpoint = int(len(array) / 2)
    print(midpoint)

    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])
    print("left in the nend", left)
    print("right in the nend", right)
    return merge(left, right)


def merge(left, right):

    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:

            result.append(left[left_pointer])
            left_pointer += 1

        else:

            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    print("result",result)
    return result


print(unsorted_list)
result = merge_sort(unsorted_list)
print(result)
