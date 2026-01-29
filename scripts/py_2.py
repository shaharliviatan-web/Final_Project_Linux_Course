#!/usr/bin/env python3

import os
from datetime import datetime

# Log file path
log_file = "/app/output.log"

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def log_message(message):
    """Write message to both console and log file with immediate sync"""
    print(message)
    
    # Extract directory path
    log_dir = os.path.dirname(log_file)
    
    # Create directory if it doesn't exist (e.g., if /app is missing)
    if log_dir and not os.path.exists(log_dir):
        try:
            os.makedirs(log_dir, exist_ok=True)
        except PermissionError:
            # Fallback for local testing if /app is restricted
            log_file_local = "output.log"
            with open(log_file_local, "a", encoding="utf-8") as f:
                f.write(f"[FALLBACK] {message}\n")
            return

    # Open file and sync to disk
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")
        f.flush()
        os.fsync(f.fileno())

# Log start of execution
log_message(f"\n--- Execution started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

# Get user input
try:
    user_input = input("Enter temperature in Celsius: ")
    log_message(f"Input: {user_input}")
    
    celsius = float(user_input)
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    result = f"{celsius}°C = {fahrenheit}°F"
    log_message(f"Output: {result}")

except ValueError:
    error_msg = "Error: Please enter a valid number"
    log_message(f"Status: {error_msg}")

finally:
    log_message(f"--- Execution ended at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")