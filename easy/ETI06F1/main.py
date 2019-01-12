PI = 3.141592654

def main():
    input_test = input()
    numbers = input_test.split(' ')
    r = float(numbers[0])
    d = float(numbers[1])
    r_of_smaller_circle = pow(r, 2) - pow(d / 2, 2)
    result = PI * r_of_smaller_circle
    print("{:.2f}".format(result))

main()