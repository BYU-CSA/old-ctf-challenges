def base_10_to_base_9(number):
    decimal = int(number)
    result = ''
    while decimal > 0:
        remainder = decimal % 9
        result = str(remainder) + result
        decimal = decimal // 9
    return result

# Read space separated input from user
input_str = input("Enter numbers (space separated): ")

# Convert input to list of strings
input_list = input_str.split()

# Convert each number to base 9 and print the result on one line
output_str = ' '.join([base_10_to_base_9(number) for number in input_list])
print(output_str)
