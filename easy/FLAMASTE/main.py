import math

def dump_characters(string, saved_characters):
    output_string = string
    if (len(saved_characters) > 2):
        output_string += saved_characters[0] + str(len(saved_characters))
    else:
        output_string += saved_characters
    return output_string

def convert_string(string_to_convert):
    current_character = string_to_convert[0]
    saved_characters = current_character
    output_string = ''
    for i in range(0, len(string_to_convert) - 1):
        if string_to_convert[i + 1] != current_character:
            output_string = dump_characters(output_string, saved_characters)
            saved_characters = ''
            current_character = string_to_convert[i + 1]
        saved_characters += string_to_convert[i + 1]
    output_string = dump_characters(output_string, saved_characters)
    return output_string

def main():
    number_of_inputs = int(input())
    inputs_to_test = []
    for _i in range(number_of_inputs):
        inputs_to_test.append(input())
    for i in inputs_to_test:
        print(convert_string(i))

main()