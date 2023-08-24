def base_11_to_base_10(number):
    decimal = 0
    power = 0
    for digit in number[::-1]:
        if digit.isdigit():
            decimal += int(digit) * (11 ** power)
        else:
            decimal += (ord(digit) - 55) * (11 ** power)
        power += 1
    return str(decimal)

# Read space separated input from user
input_str = input("Enter numbers (space separated): ")

# Convert input to list of strings
input_list = input_str.split()

# Convert each number to base 10 and print the result on one line
output_str = ' '.join([base_11_to_base_10(number) for number in input_list])
print(output_str)
