import time

# Build and return a list
def firstn(n):
  num, nums = 0, []
  while num < n:
    nums.append(num)
    num += 1
  return nums

# For each chunk of code below, choose one (corresponding) version of lines 14 & 30, 15 & 31, 16 & 32 -- NOT all -- and see the differences!

start_time = time.perf_counter()
# sum_of_first_n = sum(firstn(1000000)) # try this first
# sum_of_first_n = sum(firstn(10000000)) # try this second
sum_of_first_n = sum(firstn(100005000)) # try this last - it'll take a minute
print(sum_of_first_n)
print("Original version", time.perf_counter() - start_time, "seconds")



# The same, with a generator that yields items instead of returning a list
def firstn_gen(n):
  num = 0
  while num < n:
    yield num
    num += 1

start_time = time.perf_counter()
# sum_of_first_n_again = sum(firstn_gen(1000000)) # try this first
# sum_of_first_n_again = sum(firstn_gen(10000000)) # try this second
sum_of_first_n_again = sum(firstn_gen(100005000)) # try this last - it'll take a minute (but not as long as the other version!)
print(sum_of_first_n_again)
print("Generator version", time.perf_counter() - start_time, "seconds")


# This stuff adds up!