import math

# https://brilliant.org/wiki/finding-the-last-digit-of-a-power/
NUMBER_SEQUENCES = {
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1]
}

def get_last_digit_of_power(base, power):
    constant_return_values = [0, 1, 5, 6]
    last_digit_of_base = base
    if base >= 10:
        base_as_string = str(base)
        last_digit_of_base = int(base_as_string[-1])
    if last_digit_of_base in constant_return_values:
        return last_digit_of_base
    sequence = NUMBER_SEQUENCES[last_digit_of_base]
    reminder_of_modulo_division_power_by_length_of_sequence = power % len(sequence)
    final_index = (len(sequence) + reminder_of_modulo_division_power_by_length_of_sequence - 1) % len(sequence)
    return sequence[final_index]


def main():
    number_of_inputs = int(input())
    inputs_to_test = []
    for _i in range(number_of_inputs):
        single_input = input().split(' ')
        base = int(single_input[0])
        power = int(single_input[1])
        inputs_to_test.append([base, power])
    for i in inputs_to_test:
        base = i[0]
        power = i[1]
        print(get_last_digit_of_power(base, power))

main()