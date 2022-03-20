from Operations import multiplication_of_two_numbers, addition_of_two_numbers, division_of_two_numbers


def successive_divisions_conversion(number_for_conversion, initial_base, base_to_convert_to):
    """
    Recommended for initial_base > base_to_convert_to
    This function converts the number_for_conversion from the base = initial_base to the base = base_to_convert_to
    :param number_for_conversion: The number we want to convert (string)
    :param initial_base: The initial base of the number we want to convert (string)
    :param base_to_convert_to: The base we want our number converted to (string)
    :return: The result of the conversion of the number_to_convert_to from the initial_base to the base_to_convert_to (string)
    """
    conversion_result = ''  # string
    while number_for_conversion != '0':  # start of conversion algorithm
        number_for_conversion, remaining = division_of_two_numbers(
            number_for_conversion, base_to_convert_to, initial_base)
        conversion_result = conversion_result + remaining
    conversion_result = conversion_result[::-1]  # inverting the string so that we have the correct result
    return conversion_result
    # done


def substitution_method_conversion(number_for_conversion, initial_base, base_to_convert_to):
    """
    Recommended for initial_base < base_to_convert_to
    This function converts the number_for_conversion from the base = initial_base to the base = base_to_convert_to
    :param number_for_conversion: The number we want to convert (string)
    :param initial_base: The initial base of the number we want to convert (string)
    :param base_to_convert_to: The base we want our number converted to (string)
    :return: The result of the conversion of the number_to_convert_to from the initial_base to the base_to_convert_to (string)
    """
    power_of_initial_base = '1'  # string
    conversion_result = '0'  # string
    add = addition_of_two_numbers  # add <- the function addition_of_two_numbers
    multiplication = multiplication_of_two_numbers  # multiplication <- the function multiplication_of_two_numbers
    while len(number_for_conversion) > 0:  # start of conversion algorithm
        conversion_result = add(conversion_result, multiplication_of_two_numbers(
            power_of_initial_base, number_for_conversion[-1], base_to_convert_to), base_to_convert_to)
        power_of_initial_base = multiplication(power_of_initial_base, initial_base, base_to_convert_to)
        number_for_conversion = number_for_conversion[:-1]  # removing the last digit of the number
    return conversion_result
    # Done


def conversion_using_decimal_base(number_for_conversion, initial_base, base_to_convert_to):
    """
    This function converts the number_for_conversion from the base = initial_base to the base = base_to_convert_to
        using the decimal base as an intermediary base
    :param number_for_conversion: The number we want to convert (string)
    :param initial_base: The initial base of the number we want to convert (string)
    :param base_to_convert_to: The base we want our number converted to (string)
    :return: The result of the conversion of the number_to_convert_to from the initial_base to the base_to_convert_to
    """
    # The dictionaries below will help in performing the calculation by making the link between digits and string
    # values of those digits
    dictionary_string_to_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16}
    number_to_letter = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                        11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    conversion_result = ''  # string
    power_of_base = 1  # int
    decimal_number = 0  # int
    while len(number_for_conversion) > 0:  # converting to binary
        digit_converted_to_binary = power_of_base * dictionary_string_to_number[number_for_conversion[-1]]  # int
        decimal_number = decimal_number + digit_converted_to_binary  # int
        power_of_base *= int(initial_base)  # int
        number_for_conversion = number_for_conversion[:-1]  # removing the last digit of the number
    while decimal_number > 0:  # start of the conversion algorithm
        conversion_result = conversion_result + number_to_letter[(decimal_number % int(base_to_convert_to))]
        decimal_number //= int(base_to_convert_to)
    conversion_result = conversion_result[::-1]  # inverting the string so that we have the correct result
    return conversion_result
    # done


def conversion_to_binary_from_base_power_of_two(number_for_conversion, initial_base):
    """
    This function converts the number_for_conversion from the base = initial_base to the binary base
    :param number_for_conversion: The number we want to convert (string)
    :param initial_base: The initial base of the number we want to convert(power of 2) (string)
    :return: The result of the conversion of the number_to_convert_to from the initial_base to the binary base
    """
    # The dictionary below will help in performing the calculation by making the link between digits and string
    # values of those digits
    dictionary_string_to_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16}
    conversion_result = ''  # string
    number_powers_of_two = 0  # int
    copy_initial_base = int(initial_base)  # int
    while copy_initial_base != 1:  # computing the power of 2 EX: copy_initial_base = 4; number_powers_of_two = 2
        number_powers_of_two += 1
        copy_initial_base //= 2
    while len(number_for_conversion) > 0:  # conversion to binary
        last_digit_of_the_number = dictionary_string_to_number[number_for_conversion[-1]]  # int
        number_for_conversion = number_for_conversion[:-1]
        if last_digit_of_the_number == 0:
            for i in range(0, number_powers_of_two):
                conversion_result = conversion_result + '0'
        else:
            while last_digit_of_the_number != 0:  # if the digit is not zero
                conversion_result = conversion_result + str(last_digit_of_the_number % 2)
                last_digit_of_the_number //= 2
            while len(conversion_result) % number_powers_of_two != 0:  # add zeros to match the group length to
                # number powers of two. Ex: 6 = 011(0) - it will be inverted in the end
                conversion_result = conversion_result + '0'  # adding 0 320123012
    conversion_result = conversion_result[::-1]  # inverting the string so that the result is the correct one
    return conversion_result
    # done


def conversion_to_base_power_of_two_from_binary(number_for_conversion, base_to_convert_to):
    """
    This function converts the number_for_conversion from the binary base to the base = base_to_convert_to
    :param number_for_conversion: The number we want to convert (string)
    :param base_to_convert_to: The base we want our number converted to (power of 2) (string)
    :return: The result of the conversion of the number_to_convert_to from the binary base to the base_to_convert_to
    """
    # The dictionary below will help in performing the calculation by making the link between digits and string
    # values of those digits
    number_to_letter = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                        11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    conversion_result = ''  # string
    number_powers_of_two = 0  # int
    copy_base_to_convert_to = int(base_to_convert_to)  # int
    while copy_base_to_convert_to != 1:   # computing the power of 2 EX: copy_initial_base = 4; number_powers_of_two = 2
        number_powers_of_two += 1
        copy_base_to_convert_to //= 2
    while len(number_for_conversion) % number_powers_of_two != 0:  # inserting (before the number) insignificant 0 if
        # needed, so that the length of number_for_conversion will be a multiple of number_powers_of_two
        number_for_conversion = '0' + number_for_conversion
    while len(number_for_conversion) > 0:  # start of conversion algorithm
        digit_in_binary = number_for_conversion[:number_powers_of_two]  # taking groups of digits, the length of
        # a group = number_powers_of_two
        digit_in_base_to_convert = 0  # int
        power_of_two = 1  # int
        while len(digit_in_binary) > 0:  # conversion from binary
            group_in_base_to_convert = int(digit_in_binary[-1]) * power_of_two  # int
            digit_in_base_to_convert = digit_in_base_to_convert + group_in_base_to_convert  # int
            power_of_two *= 2  # int
            digit_in_binary = digit_in_binary[:-1]  # removing the last digit of the number
        conversion_result = conversion_result + number_to_letter[digit_in_base_to_convert]  # adding the just converted
        # digit to the result
        number_for_conversion = number_for_conversion[number_powers_of_two:]  # removing a number = number_powers_of_two
        # of digits from the number
    return conversion_result
    # done


def rapid_conversion(number_for_conversion, initial_base, base_to_convert_to):
    """
    This function converts the number_for_conversion from the base = initial_base to the base = base_to_convert_to
    :param number_for_conversion: The number we want to convert
    :param initial_base: The initial base of the number we want to convert (power of 2)
    :param base_to_convert_to: The base we want our number converted to (power of 2)
    :return: The result of the conversion of the number_to_convert_to from the initial_base to the base_to_convert_to
    """
    # converting to binary
    number_in_binary = conversion_to_binary_from_base_power_of_two(number_for_conversion, initial_base)
    # converting from binary
    number_in_base_to_convert_to = conversion_to_base_power_of_two_from_binary(number_in_binary, base_to_convert_to)
    return number_in_base_to_convert_to
    # done
