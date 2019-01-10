def main():
    number_of_inputs = int(input())
    reversed_numbers = []
    for _i in range(number_of_inputs):
        current_input = input().split(' ')
        current_input_drop_first = current_input[1:]
        reversed_numbers.append(current_input_drop_first[::-1])
    for i in reversed_numbers:
        print(' '.join(i))

main()