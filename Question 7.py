#duplicate program

def remove_duplicates(input_list):
    # Initialize an empty list to hold unique elements
    unique_list = []

    # Loop through each element in the input list
    for item in input_list:
        # Only add the item to unique_list if it's not already included
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
new_list = remove_duplicates(original_list)
print("List with duplicates removed:", new_list)
