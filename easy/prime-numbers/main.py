import math

def is_prime(number):
    if number < 2:
        return False
    if number % 2 == 0 and number > 2: 
        return False
    for i in range(3, math.floor(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def main():
    number_of_inputs = int(input())
    inputs_to_test = []
    for _i in range(number_of_inputs):
        input_to_test = int(input())
        inputs_to_test.append(input_to_test)
    for i in inputs_to_test:
        is_prime_test = is_prime(i)
        if is_prime_test:
            print('TAK')
        else:
            print('NIE')


main()