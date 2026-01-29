#!/usr/bin/env python3

# Program to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

# Get user input
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"\n{celsius}°C = {fahrenheit}°F")
except ValueError:
    print("Error: Please enter a valid number")
