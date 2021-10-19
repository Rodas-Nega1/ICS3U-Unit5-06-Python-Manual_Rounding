# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user for a decimal and how many places
#  they want to round it off by, and prints the rounded decimal


import math


def rounding_method(round_number, decimal_place_int):
    # round number

    # process
    round_number[0] = (round_number[0] * pow(10, decimal_place_int)) + 0.5
    round_number[0] = int(round_number[0])
    round_number[0] = float(round_number[0])
    round_number[0] = round_number[0] / pow(10, decimal_place_int)


def main():
    # this function calls the precedent function

    round_number = []

    # input & output
    user_prompt = input("Enter the number to round: ")
    decimal_place = input("Enter how many decimal places you want to round by: ")

    try:
        user_prompt_float = float(user_prompt)
        decimal_place_int = int(decimal_place)

        print("")
        round_number.append(user_prompt_float)
        rounding_method(round_number, decimal_place_int)
        print("Your rounded number is {0}.".format(round_number[0]))

    except Exception:
        print("")
        print("That is an invalid number.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
