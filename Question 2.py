#exiting program

# Ask for user input
def input_until_exit():
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        # Check if the input is "exit"
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break  # Exit the loop
        print(f"You entered: {user_input}")  # Print the entered word

# Call the function
input_until_exit()
