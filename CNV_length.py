# Import standard library modules :)
import argparse
import csv

# Creating a function to process our file
def process_file (input_file, output_file):
    # Open the input .csv file to read
    with open(input_file, 'r', newline='') as infile:
        # Read the csv file
        reader = csv.DictReader(infile)
        # Define fieldnames for output .csv file, which will be the same as before + 'length'
        fieldnames = reader.fieldnames + ['length']
        # Create a list to store the processed data 
        processed_data = []

        for row in reader:
            # Extract loc.start and loc.end values per row
            loc_start = int(row['loc.start'])
            loc_end = int(row['loc.end'])

            # Calculate length
            length = loc_end - loc_start

            # Add length value per row
            row['length'] = length

            # Add updated row to processed_data list
            processed_data.append(row)

    # Write processed data to an output .csv file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(processed_data)

def main():
    # Use argparse to create command-line arguments for this script
    # Describe what this script does
    parser = argparse.ArgumentParser(description='Take in a .csv file containing CNV loc.start and loc.end, and save a new .csv adding a column including CNV length')
    # Define command line arguments, and provide a brief description of what they do
    parser.add_argument('input_file', help='Path to input CSV file, containing loc.start and loc.end')
    parser.add_argument('output_file', help='Path to output CSV file')
    # Actually parsing the command-line arguments
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    # Call function to process the file 
    process_file(input_file, output_file)

# Make sure this script still works when imported as a module
if __name__ == "__main__":
    main()