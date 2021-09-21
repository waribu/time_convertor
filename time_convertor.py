calculation_to_hours = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"
    elif num_of_days == 0:
        return "You entered a Zer,kindly enter a positive number"
    else:
         return "You enetered a negative value,so no conversion for you!"


user_input = input ( "Hey User,Kindly enter the days you want converted into hours!\n" )
user_input_number = int(user_input)

calculated_value  = days_to_units(user_input_number)
print(calculated_value)