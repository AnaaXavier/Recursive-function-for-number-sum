def calculate_sum_up_to(chosen_number):
    # It calculates numbers up to the target number given by user.
    if chosen_number == 0:
        return 0
    else:
        return chosen_number + calculate_sum_up_to(chosen_number-1)

try:
    user_input = input('Choose a number to sum up to: ')
    # User_input is converted to integer to avoid any unintended inputs.
    user_input_to_int = int(user_input)

except Exception as e:
    print(f"ERROR: Invalid input! Please enter only positive numbers.")
    
else:
    print(f"Result: {calculate_sum_up_to(user_input_to_int)}")