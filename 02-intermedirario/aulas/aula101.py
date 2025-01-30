# count é um iterador sem fim (itertools)

from itertools import count

for i in count(start=8, step=8): # for i in range(8, 100, 8)
    print(i)
    
    if i >= 100:
        break
    
