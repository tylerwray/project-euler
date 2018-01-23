# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001 st prime number?

# TODO: Speed this up! This algorithm takes about a minute to finish execution.

def main():
    print(find_large_prime())

def is_prime(number, current):
    if number <= 1:
        return False

    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def find_large_prime():
    number = 1
    counter = 0
    while True:
        if is_prime(number):
            counter += 1
        if counter == 10001:
            return number
        number += 1


if __name__ == "__main__":
    main()
