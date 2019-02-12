from itertools import product, permutations
from names_lists import *
import random
import time

space = " "
names = first_names + last_names # from names file -- python file means can import
# if it were a text file, would have to open it and deal with its contents...

random.shuffle(names) # changes the names list in place (shuffles it) - doesn't return anything

start_time = time.perf_counter()
options = permutations(names, 3)
all_options = list(options)
random.shuffle(all_options)
for item in all_options[:10]:
	# print(item)
	print(space.join(item)) # join function - can use on a sequence that's all in memory
print("Itertools permutations", time.perf_counter() - start_time, "seconds")
