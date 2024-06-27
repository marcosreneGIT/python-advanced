import sys

# generator expression, iterables e iterators em pyhton

iterable = ['a', 'b', 'c', 'd'] 

iterator = iter(iterable) # < __iter__ e __next__

# print(next(iterator)) # a
# print(next(iterator)) # b
# print(next(iterator)) # c

while True:
    try:
        print(next(iterator))

    except StopIteration:
        break