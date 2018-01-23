# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99

# Find the largest palindrome made from the product of two 3 digit numbers.

def main():
    print(largestThreeDigitPalindrome())

def isPalindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        else:
            end -= 1
            start += 1

    return True

def largestThreeDigitPalindrome():
    first = 999
    second = 999

    largest = 0

    while first != 100:
        while second != 100:
            product = first * second
            if isPalindrome(str(product)) and product > largest:
                largest = product
            second -= 1
        second = 999
        first -= 1
    return largest


if __name__ == "__main__":
    main()
