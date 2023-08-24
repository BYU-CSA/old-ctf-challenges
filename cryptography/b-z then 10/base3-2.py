def base_3_to_base_2(number):
    decimal = 0
    power = 0
    for digit in number[::-1]:
        decimal += int(digit) * (3 ** power)
        power += 1
    result = ''
    while decimal > 0:
        result = str(decimal % 2) + result
        decimal //= 2
    return result

# Read space separated input from user
input_str = input("Enter numbers (space separated): ")

# Convert input to list of strings
input_list = input_str.split()

# Convert each number to base 2 and print the result on one line
output_str = ' '.join([base_3_to_base_2(number) for number in input_list])
print(output_str)
