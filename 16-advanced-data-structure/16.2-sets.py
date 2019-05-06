s = set()

# adding 1 and 2
s.add(1)
s.add(2)

# remove all elements from set
s.clear()

s = {1, 2, 3}
# make a copy of set
sc = s.copy()

s.add(4)

# see the difference between s and sc
print(s.difference(sc))

s1 = {1, 2, 3}
s2 = {1, 4, 5}
# update s1, removing all elements, which exist in both s1 and s2
s1.difference_update(s2)
print(s1)  # {2, 3}

s = {1, 2, 3, 4}
# if it's in the set, deletes it
s.discard(2)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
# it shows intersection
s1.intersection(s2)  # shows {1, 2}

s1.intersection_update(s2)  # find intersection and update s1


s1 = {1, 2}
s2 = {1, 2, 3}
s3 = {5}

# check, if there is intersection and return False, if yes
s1.isdisjoint(s2)

# and s1 is subset of s2
s1.issubset(s2)  # True
s2.issuperset(s1)  # the same method as above one

# union method
s1.union(s2)  # {1, 2, 4}
