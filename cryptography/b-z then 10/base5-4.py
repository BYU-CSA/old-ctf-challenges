def base_5_to_base_4(number):
    decimal = 0
    power = 0
    for digit in number[::-1]:
        decimal += int(digit) * (5 ** power)
        power += 1
    result = ''
    while decimal > 0:
        remainder = decimal % 4
        result = str(remainder) + result
        decimal = decimal // 4
    return result

# Read space separated input from user
input_str = input("Enter numbers (space separated): ")

# Convert input to list of strings
input_list = input_str.split()

# Convert each number to base 4 and print the result on one line
output_str = ' '.join([base_5_to_base_4(number) for number in input_list])
print(output_str)
