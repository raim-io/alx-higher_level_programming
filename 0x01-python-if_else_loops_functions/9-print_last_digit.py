#!/usr/bin/python3

def print_last_digit(number):
    """prints the last digit of a numbr"""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
