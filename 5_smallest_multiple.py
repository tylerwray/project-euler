# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divisible(number):
  counter = 20
  while counter != 0:
    if number % counter != 0:
      return False
    counter -= 1
  return True


def smallest_multiple():
  counter = 20
  while True:
    if is_divisible(counter):
      return counter
    counter += 20
  return None


print smallest_multiple()
