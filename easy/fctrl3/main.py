# If you write down the last 2 digits factorial starting at 0:
# 0 - 1
# 1 - 1
# 2 - 2
# 3 - 6
# 4 - 24
# 5 - 120
# 6 - 720
# 7 - 5 040
# 8 - 40 320
# 9 - 362 880
# 10 - 3 628 800
# 11 - 39 916 800
# 12 - 479 001 600
# Every factorial above 10 always ends with 00
PREDICTABLE_ENDINGS = {
    0: '0 1',
    1: '0 1',
    2: '0 2',
    3: '0 6',
    4: '2 4',
    5: '2 0',
    6: '2 0',
    7: '4 0',
    8: '2 0',
    9: '8 0',
    10: '0 0'
}

def main():
    number_of_inputs = int(input())
    inputs_to_test = []
    for _i in range(number_of_inputs):
        input_to_test = int(input())
        inputs_to_test.append(input_to_test)
    
    for i in inputs_to_test:
        if i >= 10:
            print(PREDICTABLE_ENDINGS[10])
        else:
            print(PREDICTABLE_ENDINGS[i])

main()