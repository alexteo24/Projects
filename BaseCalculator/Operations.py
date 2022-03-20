def addition_of_two_numbers(first_number, second_number, operation_base):
    """
    This function performs the addition of two numbers in a given base
    :param first_number: The first number of the sum (string type)
    :param second_number: The second number of the sum (string type)
    :param operation_base: The base in which the addition will be performed (string type)
    :return: The result of the addition (string type)
    """
    # The dictionaries below will help in performing the calculation by making the link between digits and string
    # values of those digits
    dictionary_string_to_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                   '10': 10, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16}
    number_to_letter = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                        11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    operation_base = int(operation_base)  # str -> int
    if len(first_number) < len(second_number):  # inverting the numbers if the first one has less digits than the other
        auxiliary_string = first_number
        first_number = second_number
        second_number = auxiliary_string
    if second_number == '0':  # addition with 0 will have as the result the first number
        addition_result = first_number
        return addition_result
    while len(second_number) != len(first_number):  # matching the length of the second number to the first number's by
        # adding insignificant zeroes in front
        second_number = '0' + second_number
    addition_result = ''  # string
    carry = 0  # int
    while len(first_number) > 0:  # the start of the addition algorithm
        last_digit_of_first_number = dictionary_string_to_number[first_number[-1]]  # int
        last_digit_of_second_number = dictionary_string_to_number[second_number[-1]]  # int
        result_digit = last_digit_of_first_number + last_digit_of_second_number + carry  # can be > operation base (int)
        digit = number_to_letter[result_digit % operation_base]  # the digit that will be added to the end of the result (string type)
        addition_result = addition_result + digit  # string
        carry = result_digit // operation_base  # int
        first_number = first_number[:-1]  # removing the last digit of the first number (string)
        second_number = second_number[:-1]  # removing the last digit of the second number (string)
    if carry != 0:
        addition_result = addition_result + str(carry)  # adding the last carry (string)
    addition_result = addition_result[::-1]  # inverting the string to get the correct result (string)
    return addition_result
    # done


def subtraction_of_two_numbers(first_number, second_number, operation_base):
    """
    This function performs the subtraction of two numbers (first_number > second_number) in a given base
    :param first_number: The first, and bigger, number of the subtraction (string type)
    :param second_number: The second, and smaller, number of the subtraction (string type)
    :param operation_base: The base in which the subtraction will be performed (string type)
    :return: The result of the subraction (string type)
    """
    # The dictionaries below will help in performing the calculation by making the link between digits and string
    # values of those digits
    dictionary_string_to_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16}
    number_to_letter = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                        11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    operation_base = int(operation_base)  # str -> int
    subtraction_result = ''  # string
    if second_number == '0':  # subtracting 0 will have as the result the first number
        subtraction_result = first_number
        return subtraction_result
    while len(second_number) < len(first_number):  # matching the length of the second number to the first number's by
        # adding insignificant zeroes in front
        second_number = '0' + second_number
    borrow = 0  # int
    while len(first_number) > 0:  # the start ot the subtraction algorithm
        last_digit_of_first_number = dictionary_string_to_number[first_number[-1]]  # int
        last_digit_of_second_number = dictionary_string_to_number[second_number[-1]]  # int
        result_digit = last_digit_of_first_number - last_digit_of_second_number - borrow  # int, can be < 0
        borrow = 0
        if result_digit < 0:  # if the subtraction of the last digits < 0, a borrow is needed
            borrow = 1
        digit = number_to_letter[(result_digit + borrow * operation_base) % operation_base]  # the digit that will be added to the end of the result (string)
        subtraction_result = subtraction_result + digit  # string
        first_number = first_number[:-1]  # removing the last digit of the first number (string)
        second_number = second_number[:-1]  # removing the last digit of the second number (string)
    subtraction_result = subtraction_result[::-1]  # inverting the string to get the correct result
    while subtraction_result[0] == '0':  # checking for insignificant zeroes
        subtraction_result = subtraction_result[1:]  # removing the insignificant zeroes
    return subtraction_result
    # done


def multiplication_of_two_numbers(first_number, second_number, operation_base):
    """
    This function will perform the multiplication of two numbers in a given base
    :param first_number: The first number of the multiplication (string type)
    :param second_number: The second number of the multiplication (string type)
    :param operation_base: The base in which the multiplication will be performed (string type)
    :return: The result of the multiplication (string type)
    """
    # The dictionaries below will help in performing the calculation by making the link between digits and string
    # values of those digits
    dictionary_string_to_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                   '10': 10, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16}
    number_to_letter = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                        11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    multiplication_result = ''  # string
    operation_base = int(operation_base)  # str -> int
    if second_number == '1':  # multiplication by 1 will have the same result
        multiplication_result = first_number
        return multiplication_result
    elif second_number == '0':  # multiplication by 0 will be 0
        return second_number
    carry = 0  # int
    while len(first_number) > 0:  # the start of the multiplication algorithm
        last_digit_of_first_number = dictionary_string_to_number[first_number[-1]]  # int
        last_digit_of_second_number = dictionary_string_to_number[second_number]  # int
        result_digit = last_digit_of_first_number * last_digit_of_second_number + carry  # can be > operation base (int)
        digit = number_to_letter[result_digit % operation_base]  # the digit that will be added to the end of the result (string)
        multiplication_result = multiplication_result + digit  # string
        carry = result_digit // operation_base  # int
        first_number = first_number[:-1]  # removing the last digit of the first number
    if carry != 0:  # inserting the carry in front if necessary
        multiplication_result = multiplication_result + str(carry)
    multiplication_result = multiplication_result[::-1]  # inverting the string to get the correct result
    return multiplication_result
    # done


def division_of_two_numbers(first_number, second_number, operation_base):
    """
    This function will perform the division of two numbers in a given base
    :param first_number: The first number of the division (the dividend) (string type)
    :param second_number: The  second number of the division (the divisor) (string type)
    :param operation_base: The base in which the operation will be performed (string type)
    :return: The result of the operation (string type) using 2 parameters, division_result = quotient, and remaining
    """
    # The dictionaries below will help in performing the calculation by making the link between digits and string
    # values of those digits
    dictionary_string_to_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                                   '10': 10, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, '16': 16}
    number_to_letter = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
                        11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    operation_base = int(operation_base)  # str -> int
    division_result = ''  # string
    if second_number == '1':  # division by 1 will have the result: first_number
        division_result = first_number
        return division_result
    number = ''  # value helpful for the division algorithm
    while len(first_number) > 0:  # the start of the division algorithm
        number = str(number) + first_number[0]  # adding the last digit of the first number
        digit_in_decimal = 0  # in here we will store 'number' converted into decimal for the operations
        power_of_base = 1
        while len(number) > 0:
            digit_in_decimal = digit_in_decimal + power_of_base * dictionary_string_to_number[number[-1]]
            number = number[:-1]  # removing the last digit of number
            power_of_base *= operation_base  # multiplying the power of base to continue the conversion to decimal
        digit = number_to_letter[digit_in_decimal // dictionary_string_to_number[second_number]]  # the digit that will be added to the end of the result (string type)
        division_result = division_result + digit  # string
        number = number_to_letter[digit_in_decimal % dictionary_string_to_number[second_number]]
        first_number = first_number[1:]  # removing the last digit of the first number
    while len(division_result) > 0 and division_result[0] == '0':  # removing insignificant zeros
        division_result = division_result[1:]
    if len(division_result) == 0:  # if nothing was added to the result, it means it should be 0
        division_result = '0'
    remaining = number  # string
    return division_result, remaining
    # done
