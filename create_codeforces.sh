#!/bin/bash

# Check if correct arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <problem_name> <problem_number>"
    exit 1
fi

# Arguments
problem_name=$1
problem_number=$2

# Convert problem name to CamelCase and add '_' after the problem letter
camel_case_name=$(echo "$problem_name" | sed -E 's/[^a-zA-Z0-9]+/ /g' | sed -E 's/(^| )([a-z])/\U\2/g' | sed -E 's/^([A-Z]) /\1_/')

# Create folder path
folder="codeforces/${problem_number}${camel_case_name}"

# Create folder and files
mkdir -p "$folder"
echo -e "\"\"\"\nProblem: $problem_name $problem_number\n\"\"\"\n\ndef main():\n    pass\n\nif __name__ == '__main__':\n    main()" > "$folder/main.py"
touch "$folder/input.txt"

# Confirm success
echo "Folder and files created at: $folder"
