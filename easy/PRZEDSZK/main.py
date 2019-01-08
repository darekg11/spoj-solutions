import math

# Uses Euclid's algorithm
def greatest_common_divisor(a, b):
    if a == b:
        return a
    if a > b:
        return greatest_common_divisor(a - b, b)
    if b > a:
        return greatest_common_divisor(a, b - a)

def least_common_multiple(a, b):
    return int((a * b) / greatest_common_divisor(a, b))

def main():
    number_of_inputs = int(input())
    inputs_to_test = []
    for _i in range(number_of_inputs):
        single_input = input().split(' ')
        first_group = int(single_input[0])
        second_group = int(single_input[1])
        inputs_to_test.append([first_group, second_group])
    for i in inputs_to_test:
        first_group = i[0]
        second_group = i[1]
        print(least_common_multiple(first_group, second_group))

main()