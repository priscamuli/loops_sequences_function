#sum in a list program

def sum_of_numbers(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Example usage
nums = [1, 2, 3, 4, 5]
result = sum_of_numbers(nums)
print(f"The sum of the numbers in the list is: {result}")
