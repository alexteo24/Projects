def validate_number_for_base(number_for_conversion, initial_base):
    """
    This functions checks if a number is written in a given base
    :param number_for_conversion: The number to check (string)
    :param initial_base: The base in which the number is supposed to be written (string)
    :return: - (the function will raise an error)
    """
    # The dictionary below will help in performing the calculation by making the link between digits and string
    # values of those digits
    dictionary_string_to_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16}
    string_digit_values = '0123456789ABCDEF'  # string to check faster if a digit is valid ( cannot be more than F = 15)
    available_bases = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '16']
    if initial_base not in available_bases:  # checking if the initial base is from {2,3,4,5,6,7,8,9,10,16}
        # if not, raise an error
        raise ValueError("The initial base must be between 2 and 10, or 16!")
    while len(number_for_conversion) > 0:  # starting the validation of the number
        if dictionary_string_to_number[number_for_conversion[0]] >= int(initial_base):  # checking if all the digits are
            # from the base (ex A is not from base 10), if not, raise an error
            raise ValueError("Please make sure that both numbers fit into the given base!")
        if number_for_conversion[0] not in string_digit_values:
            raise ValueError("Please make sure your number has digits from 0-9 and A-F if necessary!")
        number_for_conversion = number_for_conversion[1:]  # removing the last digit of the number


def validate_input_for_successive_division_method(number_for_conversion, initial_base, final_base):
    """
    This functions checks if the input is suitable for the successive division conversion method
    :param number_for_conversion: The number we want to convert (string)
    :param initial_base: The initial base(string)
    :param final_base: The second base (string)
    :return: - (the function will raise an error)
    """
    available_bases = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '16']
    validate_number_for_base(number_for_conversion, initial_base)  # checking if the number is from the initial base
    if initial_base not in available_bases or final_base not in available_bases:  # checking if the initial base and the
        # final base are from {2,3,4,5,6,7,8,9,10,16} if not, raise an error
        raise ValueError("Both initial base and final base must be between 2 and 10, or 16!")
    if int(initial_base) < int(final_base):  # programmed such it will work only for the recommendation from the course
        # (initial_base > final_base), if condition not met, raise an error
        raise ValueError("Please make sure that the initial base > final base if you want to use this method of "
                         "conversion!")


def validate_input_for_substitution_method(number_for_conversion, initial_base, final_base):
    """
    This function checks if the input is suitable for the substitution conversion method
    :param number_for_conversion: The number we want to convert (string)
    :param initial_base: The initial base (string)
    :param final_base: The second base (string)
    :return: - (the function will raise an error)
    """
    available_bases = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '16']
    validate_number_for_base(number_for_conversion, initial_base)  # checking if the number is from the initial base
    if initial_base not in available_bases or final_base not in available_bases:  # checking if the initial base and the
        # final base are from {2,3,4,5,6,7,8,9,10,16} if not, raise an error
        raise ValueError("Both initial base and final base must be between 2 and 10, or 16!")
    if int(initial_base) > int(final_base):  # programmed such it will work only for the recommendation from the course
        # (initial_base < final_base), if condition not met, raise an error
        raise ValueError("Please make sure that the initial base < final base!")


def validate_input_for_decimal_intermediary_method(number_for_conversion, initial_base, final_base):
    """
    This function checks if the input is suitable for conversion using decimal base as an intermediary base
    :param number_for_conversion: The number we want to convert (string)
    :param initial_base: The initial base (string)
    :param final_base: The second base (string)
    :return: - (the function will raise an error)
    """
    available_bases = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '16']
    validate_number_for_base(number_for_conversion, initial_base)  # checking if the number is from the initial base
    if initial_base not in available_bases or final_base not in available_bases:  # checking if the initial base and the
        # final base are from {2,3,4,5,6,7,8,9,10,16} if not, raise an error
        raise ValueError("Both initial base and final base must be between 2 and 10, or 16!")


def validate_input_for_rapid_conversion(number_for_conversion, initial_base, final_base):
    """
    This function checks if the input is suitable for rapid conversion method
    :param number_for_conversion: The number we want to convert (string)
    :param initial_base: The initial base (string)
    :param final_base: The second base (string)
    :return: - (the function will raise an error)
    """
    powers_of_two = ['2', '4', '8', '16']
    validate_number_for_base(number_for_conversion, initial_base)  # checking if the number is from the initial base
    if initial_base not in powers_of_two or final_base not in powers_of_two:  # check if the bases are powers of 2
        raise ValueError("Please make sure that both the initial base and the final base are powers of 2 if you want "
                         "to use this method of conversion!")


def validate_inputs_for_operations(first_number, second_number, operation_base):
    """
    This function validates the input for all operations
    :param first_number: The first number of the operation (string)
    :param second_number: The second number of the operation (string)
    :param operation_base: The base in which we want to perform the operation (string)
    :return: - (the function will raise an error)
    """
    if not first_number.isalnum() or not second_number.isalnum():  # checking if the input is composed only from digits
        # and letters
        raise ValueError("Please make sure that both numbers are positive integers!")
    validate_number_for_base(first_number, operation_base)
    validate_number_for_base(second_number, operation_base)


def validate_inputs_for_subtraction(first_number, second_number, operation_base):
    """
    This functions will perform some additional checks for the subtraction operation
    :param first_number: The first number of the operation (string)
    :param second_number: The second number of the operation (string)
    :param operation_base: The base in which we want to perform the operation (string)
    :return: - (the function will raise an error)
    """
    validate_inputs_for_operations(first_number, second_number, operation_base)  # usual validation for an operation
    if first_number[0] == '-' or second_number[0] == '-':  # checking if the numbers are positive (program only works
        # with positive numbers, both results and inputs
        raise ValueError("Please make sure that you entered positive numbers!")
    if len(first_number) < len(second_number):  # checking if the first_number < second_number (program only works with
        # positive numbers, both results and inputs
        raise ValueError("Please make sure that the first number is bigger than the second one!")
    elif len(first_number) == len(second_number):  # continue the check for first_number < second_number
        while first_number[0] == second_number[0]:  # while both numbers have the same first digit
            first_number = first_number[1:]  # remove the firs digit of the first number
            second_number = second_number[1:]  # remove the first digit of the second number
        if len(first_number) != 0:  # if the string is non-empty, this means the numbers are not equal
            if '0' <= first_number[0] <= '9' and 'A' <= second_number[0] <= 'F':  # first digit of first number < first
                # digit of second number
                raise ValueError("Please make sure that the first number is bigger than the second one!")
            if int(first_number[0]) < int(second_number[0]):  # first digit of first number < first digit of
                # second number
                raise ValueError("Please make sure that the first number is bigger than the second one!")


def validate_inputs_for_division(first_number, second_number, operation_base):
    """
    This functions will perform some additional checks for the division operation
    :param first_number: The first number of the operation (string)
    :param second_number: The second number of the operation (string)
    :param operation_base: The base in which we want to perform the operation (string)
    :return: - (the function will raise an error)
    :return:
    """
    validate_inputs_for_operations(first_number, second_number, operation_base)  # usual operation check
    if second_number == '0':  # checking if the divisor is 0, in this case, division is not possible
        raise ValueError("Cannot perform division by 0!")
    if first_number[0] == '-' or second_number[0] == '-':  # checking if the numbers are positive (program only works
        # with positive numbers, both results and inputs
        raise ValueError("Please make sure that you entered positive numbers!")
    if len(second_number) > 1:  # checking if the divisor is a number >= 10 (only single digit divisions)
        raise ValueError("Please stick to single digits positive integers divisions! Thank you!")
