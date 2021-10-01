calculation_to_hours = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a Zero,kindly enter a positive number")
    else:
        print("Your input is not a valid number. Don't ruin my program!")


user_input = input("Hey User,Kindly enter the days you want converted into hours!\n")
validate_and_execute()
