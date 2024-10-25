#tuple program

def find_largest_number(numbers):
    # Initialize the largest number to the first element of the tuple
    largest = numbers[0]

    # Loop through each number in the tuple
    for number in numbers:
        # Update largest if the current number is greater
        if number > largest:
            largest = number

    return largest


# Example usage
numbers_tuple = (10, 20, 30, 40, 50)
largest_number = find_largest_number(numbers_tuple)
print("The largest number in the tuple is:", largest_number)
