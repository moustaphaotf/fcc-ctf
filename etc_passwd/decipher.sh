#!/bin/bash

# Output file to store John the Ripper results
output_file="john_results.txt"

# Function to run John the Ripper with a specific mask
run_john() {
    mask=$1
    john --format=crypt --mask="$mask" copy >> "$output_file"
}

# Function to repeat a string n times
repeat_string() {
    local string="$1"
    local n="$2"

    # Utilisez une boucle for pour répéter la chaîne
    for ((i=0; i<n; i++)); do
        echo -n $string
    done

    # Pour ajouter une nouvelle ligne à la fin
    echo
}


# Initialize mask with "PuMa"
DEFAULT_MASK="PuMa"

# Sleep duration between attempts (adjust as needed)
sleep_duration=2

# Number of placeholders
N=0
# Loop to run John the Ripper with variations of the mask
while true; do

    # Generate prefix and suffix
    suffix=""
    prefix=""

    echo "N=$N"

    for ((i=0,j=N; i<=N; i++,j--))
    do
        mask="$DEFAULT_MASK"

        # Update the mask
        tmp_p=$(repeat_string "?a" "$i")
        tmp_s=$(repeat_string "?a" "$((N-i))")

        suffix=$tmp_s
        prefix=$tmp_p

        mask=$prefix$mask$suffix

        
        echo "Trying: $mask"

        run_john "$mask"

        # Check if the password was found
        if grep -q "1g" "$output_file"; then
            echo "Password found: $mask"
            exit
        fi
    done
    # Sleep between attempts
    ((N++))
done