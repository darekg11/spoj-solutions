import math

def main():
    number_of_inputs = int(input())
    sums = []
    for _i in range(number_of_inputs):
        current_sum = 0
        input()
        single_input = input().split(' ')
        for single_number_str in single_input:
            single_number_int = int(single_number_str)
            current_sum += single_number_int
        sums.append(current_sum)
    for i in sums:
        print(i)

main()