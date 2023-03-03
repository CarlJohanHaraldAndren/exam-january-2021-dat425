def duplicates(xs):
    duplicates = []
    dict_counts = {}
    for item in xs:
        dict_counts[item] = dict_counts.get(item, 0) + 1

    duplicates = [key for key, value in dict_counts.items() if value >= 2]

    return duplicates






print(duplicates([1,2,3,2,1,1,5]))
print(duplicates([]))

"""

Implement the function:
duplicates(xs)
Which takes a list of elements and returns a new list which only
contains those elements which appear more than once in the
original list. One way to solve the problem is to count how many
times each element appears, and then to preserve only those
for which the count is greater than one.
Here are some examples:

>>> duplicates([1,2,3,2,1,1,5])
[1,2]
>>> duplicates([‘a’,’b’,’b’,’a’])
[‘b’]
>>> duplicates([True,False])
[]
>>> duplicates([])
[]

"""