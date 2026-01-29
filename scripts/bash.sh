#!/bin/bash

# Script to move and rename files
# Usage: ./bash.sh <source_path> <target_path>

# Check if exactly 2 parameters were provided
if [ $# -ne 2 ]; then
    echo "Error: You must provide exactly 2 parameters"
    echo "Usage: $0 <source_path> <target_path>"
    exit 1
fi

source_path="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
target_path="$(cd "$(dirname "$2")" 2>/dev/null && pwd)/$(basename "$2")" || "$(pwd)/$(basename "$2")"

# Check if the source file exists
if [ ! -f "$source_path" ]; then
    echo "Error: Source file '$source_path' does not exist"
    exit 1
fi

# Copy the file to the target destination
if cp "$source_path" "$target_path"; then
    echo "✓ File copied successfully"
    echo "  Source: $source_path"
    echo "  Target: $target_path"
else
    echo "✗ Error: Failed to copy the file"
    exit 1
fi
