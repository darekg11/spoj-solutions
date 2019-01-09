import math

# Uses Euclid's algorithm - iteration to not exceed recursion stack limit
def greatest_common_divisor_iterations(a, b):
    new_a = a
    new_b = b
    while new_a != new_b:
        if new_a == 0 or new_b == 0:
            return 0
        if new_a > new_b:
            new_a -= new_b
        else:
            new_b -= new_a
    return new_a

def main():
    number_of_inputs = int(input())
    inputs_to_test = []
    for _i in range(number_of_inputs):
        single_input = input().split(' ')
        first_number = int(single_input[0])
        second_number = int(single_input[1])
        inputs_to_test.append([first_number, second_number])
    for i in inputs_to_test:
        first_number = i[0]
        second_number = i[1]
        print(greatest_common_divisor_iterations(first_number, second_number))

main()