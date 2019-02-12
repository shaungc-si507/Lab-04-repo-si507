# from itertools import product, permutations
from names_lists import *
import random
import time

space = " "
names = first_names + last_names # from names file -- python file means can import
# if it were a text file, would have to open it and deal with its contents...

random.shuffle(names) # changes the names list in place (shuffles it) - doesn't return anything


def permutation(lst, length):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       random.shuffle(lst)
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first
       # element
       for p in permutation(remLst, length):
           perm = ([m] + p)[:length]
           if perm not in l:
               l.append(perm)
    return l


# Driver program to test above function
start_time = time.perf_counter()
for p in permutation(names[:10],3)[:10]:
    print(p)
print("Slow permutations", time.perf_counter() - start_time, "seconds")
