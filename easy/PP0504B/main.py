def merge_string(a, b):
    character_count = len(a)
    if len(b) < len(a):
        character_count = len(b)
    final_characters = ''
    for i in range(0, character_count):
        final_characters += a[i]
        final_characters += b[i]
    return final_characters

def main():
    number_of_inputs = int(input())
    inputs_to_test = []
    for _i in range(number_of_inputs):
        single_input = input().split(' ')
        inputs_to_test.append(single_input)
    for i in inputs_to_test:
        first_string = i[0]
        second_string = i[1]
        print(merge_string(first_string, second_string))

main()