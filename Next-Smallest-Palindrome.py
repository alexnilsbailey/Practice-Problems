# Given a number as an input, find the following smallest palindrome number. For simplicity, assume the input value will not exceed 1 million. The next palindrome may be greater than 1 million.

# Constraints
# The input variable 'n' is an integer.
# The input value 'n' will not exceed 1,000,000. The resulting palindrome may be greater than this limit.

# Wanted to do it without using the while loop to see if I could come up with something a little more creative.

def next_palindrome(n):
    str_n = str(n)
    if len(str(n)) == 1 and n != 9:
        palindrome = n + 1
    elif n == 9:
        palindrome = 11
    else:
        if len(str_n) % 2 == 0:
            first_half = str(int(str_n[:len(str_n) // 2]) + 1)
            if len(first_half) > len(str_n[:len(str_n) // 2]):
                second_half = str(first_half[-2::-1])
            else:
                second_half = first_half[::-1]
            palindrome = int(first_half + second_half)
        else:
            first_half = str(int(str_n[:(len(str_n) + 1) // 2]) + 1)
            if len(first_half) > len((str_n[:(len(str_n) + 1) // 2])):
                second_half = str(first_half[-3::-1])
            else:
                second_half = first_half[-2::-1]
            palindrome = int(first_half + second_half)
    return palindrome
        
     