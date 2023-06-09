import csv
import sys

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    i = 0
    while i < sequence_length:
        current_run = 0

        if sequence[i:i+subsequence_length] == subsequence:
            current_run = 1

            j = i + subsequence_length
            while j < sequence_length and sequence[j:j+subsequence_length] == subsequence:
                current_run += 1
                j += subsequence_length

        if current_run > longest_run:
            longest_run = current_run

        i += 1

    return longest_run

def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return

    csv_filename = sys.argv[1]
    sequence_filename = sys.argv[2]

    # Read CSV file into memory
    data = []
    with open(csv_filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)

    # Extract STRs from the first row of the CSV file
    str_list = data[0][1:]

    # Read DNA sequence into memory
    sequence = ""
    with open(sequence_filename, "r") as sequence_file:
        sequence = sequence_file.read().strip()

    # Calculate the longest match for each STR
    str_counts = {}
    for str_sequence in str_list:
        str_counts[str_sequence] = longest_match(sequence, str_sequence)

    # Search for matching individual in the CSV data
    for i in range(1, len(data)):
        row = data[i]
        name = row[0]
        matches = 0

        # Check if the STR counts match exactly
        for j in range(1, len(row)):
            if int(row[j]) == str_counts[str_list[j-1]]:
                matches += 1

        if matches == len(str_list):
            print(name)
            return

    # If no match found
    print("No match")

if __name__ == "__main__":
    main()
