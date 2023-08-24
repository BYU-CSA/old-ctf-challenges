def base_10_to_base_26(number):
    alphabet = '0123456789ABCDEFGHIJKLMNOP'
    result = ''
    while number > 0:
        remainder = number % 26
        result = alphabet[remainder] + result
        number = number // 26
    return result

# Read space separated input from user
input_str = input("Enter numbers (space separated): ")

# Convert input to list of integers
input_list = list(map(int, input_str.split()))

# Convert each number to base 26 and print the result on one line
output_str = ' '.join([base_10_to_base_26(number) for number in input_list])
print(output_str)
