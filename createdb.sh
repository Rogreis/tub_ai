# Create the AI db for The Urantia book
# Script for windows
# The environment for python should be already created using: python -m venv tub_ai

#!/bin/bash

# Function to check if VIRTUAL_ENV ends with "/tub_ai_env"
check_virtual_env() {
    if [[ "$VIRTUAL_ENV" == *"/tub_ai_env" ]]; then
        return 0  # Return 0 if the condition is true
    else
        return 1  # Return 1 if the condition is false
    fi
}

# Main script
if check_virtual_env; then
    echo "The virtual environment 'tub_ai_env' is active."
else
    echo "The virtual environment 'tub_ai_env' is not active."
    echo "Activate it: source tub_ai_env/bin/activate"
    exit 1
fi
