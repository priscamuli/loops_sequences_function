def has_pair_with_sum(int_list, target_sum):
    """
    Checks if there are two distinct numbers in the list that add up to the target sum.

    Args:
    int_list (list): The list of integers to check.
    target_sum (int): The target sum to find.

    Returns:
    bool: True if such a pair exists, False otherwise.
    """
    seen = set()  # Set to keep track of the numbers we have seen
    for number in int_list:
        complement = target_sum - number  # The number needed to reach the target sum
        if complement in seen:  # Check if the complement is already in the set
            return True  # A valid pair found
        seen.add(number)  # Add the current number to the set
    return False  # No valid pair found


# Example usage:
example_list = [1, 2, 3, 4, 5]
target = 9
result = has_pair_with_sum(example_list, target)
print(result)

target = 8
result = has_pair_with_sum(example_list, target)
print(result)
