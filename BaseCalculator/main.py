from Validators import *
from ConversionMethods import *
from Operations import *
import time


def print_commands():
    time.sleep(0.3)
    print("Please choose one of the following commands:")
    time.sleep(0.3)
    print("1. Conversion using the successive divisions and multiplications method (initial_base > base_to_convert_to)")
    time.sleep(0.3)
    print("2. Conversion using the substitution method (initial_base < base_to_convert_to)")
    time.sleep(0.3)
    print("3. Conversion using 10 as an intermediate base")
    time.sleep(0.3)
    print("4. Rapid conversion")
    time.sleep(0.3)
    print("5. Addition of two numbers in a given base")
    time.sleep(0.3)
    print("6. Subtraction of two numbers in a given base")
    time.sleep(0.3)
    print("7. Multiplication of a number by a digit in a given base")
    time.sleep(0.3)
    print("8. Division of a number by a digit in a given base")
    time.sleep(0.3)
    print("0. Exit")
    time.sleep(0.3)


def conversion_inputs():
    """
    This function manages the inputs for a conversion ( get the input from the user, remove the spaces, all letters are
        going to be made capitals, returns the data for conversion - initial_base, number_for_conversion, final_base)
    :return: initial_base, number_for_conversion, final_base
    """
    initial_base = input("Please enter the initial base: ")
    number_for_conversion = input("Please enter the number you want to convert: ")
    final_base = input("Please enter the base you want to convert to: ")
    initial_base = initial_base.strip(' ')
    number_for_conversion = number_for_conversion.strip(' ')
    number_for_conversion = number_for_conversion.upper()
    final_base = final_base.strip(' ')
    return initial_base, number_for_conversion, final_base


def operation_inputs():
    """
    This function manages the inputs for an operation ( get the input from the user, remove the spaces, all letters are
        going to be made capitals, returns the data for an operation - first_number, second_number, operation_base)
    :return: first_number, second_number, operation_base
    """
    first_number = input("Please enter the first number: ")
    second_number = input("Please enter the second number: ")
    operation_base = input("Please enter the base in which you want your operation to be performed: ")
    first_number = first_number.strip(' ')
    first_number = first_number.upper()
    second_number = second_number.strip(' ')
    second_number = second_number.upper()
    operation_base = operation_base.strip(' ')
    return first_number, second_number, operation_base


def start_menu():
    print("Code written by Apavaloaei Alexandru-Teodor\n")
    are_we_done_yet = False
    while not are_we_done_yet:
        try:
            time.sleep(0.7)
            print_commands()
            user_command = input("Please enter your command: ")
            if user_command == '1':  # Conversion using the successive divisions and multiplications method (initial_base > base_to_convert_to)
                initial_base, number_for_conversion, final_base = conversion_inputs()
                time.sleep(0.5)
                validate_input_for_successive_division_method(number_for_conversion, initial_base, final_base)
                time.sleep(0.5)
                converted_number = successive_divisions_conversion(number_for_conversion, initial_base, final_base)
                time.sleep(0.5)
                print("The number " + number_for_conversion + " in base " + initial_base + " is equal to "
                      + converted_number + " in base " + final_base)
            elif user_command == '2':  # Conversion using the substitution method ( initial_base < base_to_convert_to)
                initial_base, number_for_conversion, final_base = conversion_inputs()
                time.sleep(0.5)
                validate_input_for_substitution_method(number_for_conversion, initial_base, final_base)
                time.sleep(0.5)
                converted_number = substitution_method_conversion(number_for_conversion, initial_base, final_base)
                time.sleep(0.5)
                print("The number " + number_for_conversion + " in base " + initial_base + " is equal to "
                      + converted_number + " in base " + final_base)
            elif user_command == '3':  # Conversion using 10 as an intermediate base
                initial_base, number_for_conversion, final_base = conversion_inputs()
                time.sleep(0.5)
                validate_input_for_decimal_intermediary_method(number_for_conversion, initial_base, final_base)
                time.sleep(0.5)
                converted_number = conversion_using_decimal_base(number_for_conversion, initial_base, final_base)
                time.sleep(0.5)
                print("The number " + number_for_conversion + " in base " + initial_base + " is equal to "
                      + converted_number + " in base " + final_base)
            elif user_command == '4':  # Rapid conversion
                initial_base, number_for_conversion, final_base = conversion_inputs()
                time.sleep(0.5)
                validate_input_for_rapid_conversion(number_for_conversion, initial_base, final_base)
                time.sleep(0.5)
                converted_number = rapid_conversion(number_for_conversion, initial_base, final_base)
                time.sleep(0.5)
                print("The number " + number_for_conversion + " in base " + initial_base + " is equal to "
                      + converted_number + " in base " + final_base)
            elif user_command == '5':  # Addition of two numbers in a given base
                first_number, second_number, operation_base = operation_inputs()
                time.sleep(0.5)
                validate_inputs_for_operations(first_number, second_number, operation_base)
                time.sleep(0.5)
                addition_result = addition_of_two_numbers(first_number, second_number, operation_base)
                time.sleep(0.5)
                print("The result of the addition of " + first_number + " and " + second_number + " in the base "
                      + operation_base + " is " + addition_result)
            elif user_command == '6':  # Subtraction of two numbers in a given base
                first_number, second_number, operation_base = operation_inputs()
                time.sleep(0.5)
                validate_inputs_for_subtraction(first_number, second_number, operation_base)
                time.sleep(0.5)
                subtraction_result = subtraction_of_two_numbers(first_number, second_number, operation_base)
                time.sleep(0.5)
                print("The result of the subtraction between " + first_number + " and " + second_number + " in the base "
                      + operation_base + " is " + subtraction_result)
            elif user_command == '7':  # Multiplication of a number by a digit in a given base
                first_number, second_number, operation_base = operation_inputs()
                time.sleep(0.5)
                validate_inputs_for_operations(first_number, second_number, operation_base)
                time.sleep(0.5)
                multiplication_result = multiplication_of_two_numbers(first_number, second_number, operation_base)
                time.sleep(0.5)
                print("The result of the multiplication of " + first_number + " with " + second_number + " in the base "
                      + operation_base + " is " + multiplication_result)
            elif user_command == '8':  # Division of a number by a digit in a given base
                first_number, second_number, operation_base = operation_inputs()
                time.sleep(0.5)
                validate_inputs_for_division(first_number, second_number, operation_base)
                time.sleep(0.5)
                quotient, remaining = division_of_two_numbers(first_number, second_number, operation_base)
                time.sleep(0.5)
                print("The result of the division of " + first_number + " with " + second_number + " in the base "
                      + operation_base + " is " + quotient + " remaining " + remaining)

            elif user_command == '0': # Exit
                are_we_done_yet = True
                print("\nCode written by Apavaloaei Alexandru-Teodor\n")
                time.sleep(1)
                print("Bye bye ☺!")
                input("Press Enter to continue...")
            else:
                print("Invalid command!")
        except ValueError as ve:
            print(ve)

start_menu()
