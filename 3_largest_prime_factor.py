# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def main():
    number = 600851475143
    print(largestPrimeFactor(number))

def largestPrimeFactor(number):
  largest = 0
  i = 2

  while number > 1:
    if number % i == 0:
      largest = i
      number = number / i
    i += 1
  return largest


if __name__ == "__main__":
    main()


""" Comment out this line to run tests
### Tests ###

if largestPrimeFactor(4) != 2:
  raise AssertionError('Largest Prime Factor Failed')

if largestPrimeFactor(6) != 3:
  raise AssertionError('Largest Prime Factor Failed')

if largestPrimeFactor(13195) != 29:
  raise AssertionError('Largest Prime Factor Failed')

print 'Success!'
#"""
