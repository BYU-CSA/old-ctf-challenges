def base_25_to_base_24(number):
    decimal = 0
    power = 0
    for digit in number[::-1]:
        if digit.isdigit():
            decimal += int(digit) * (25 ** power)
        else:
            decimal += (ord(digit) - 55) * (25 ** power)
        power += 1
    result = ''
    while decimal > 0:
        remainder = decimal % 24
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(55 + remainder) + result
        decimal = decimal // 24
    return result

# Read space separated input from user
input_str = input("Enter numbers (space separated): ")

# Convert input to list of strings
input_list = input_str.split()

# Convert each number to base 24 and print the result on one line
output_str = ' '.join([base_25_to_base_24(number) for number in input_list])
print(output_str)
