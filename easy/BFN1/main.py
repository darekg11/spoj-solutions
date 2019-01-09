import math

def is_number_palindrome(a):
    return int(reverse_number(a)) == a

def reverse_number(a):
    number_as_string = str(a)
    return int(number_as_string[::-1])

def main():
    number_of_inputs = int(input())
    numbers = []
    for _i in range(number_of_inputs):
        numbers.append(int(input()))
    for i in numbers:
        attempts = 0
        current_number = i
        while is_number_palindrome(current_number) is False:
            reversed_number = reverse_number(current_number)
            current_number += reversed_number
            attempts += 1
        print(current_number, attempts)

main()