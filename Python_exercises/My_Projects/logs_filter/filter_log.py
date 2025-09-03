# log_filter.py
# Creating a simple CLI tool to filter server logs

print("Welcome to the Log Filter tool!")

#enter required info
filename = input("Please enter the log filename: ")
keyword = input("Please enter the keyword to search for: ")
print()  # Print a blank line for better output formatting

# Initialize a list to store the matching lines and their numbers
matched_lines = []

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    #ERROR #error
    #for loop to loop each line
    for line_number, line_content in enumerate(lines, start=1):
        # BONUS: Case-Insensitive Search
        if keyword.lower() in line_content.lower(): 
            # If found, store the line number append and store as tuple
            matched_lines.append((line_number, line_content))

#Handle the specific error of a missing file
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please check the filename and try again.")
    # Exit statement
    exit()

#Print the results
if matched_lines:
    print("Matching lines found:")
    #Enumerate through the list of found lines to number the output
    for output_number, (original_line_num, original_line) in enumerate(matched_lines, start=1):
        # .strip() removes any leading/trailing whitespace (like newline characters)
        print(f"{output_number}) (Line {original_line_num}): {original_line.strip()}")
else:
    print("No lines found matching your criteria.")

#Print the final summary
print(f"\nSummary: Found {len(matched_lines)} line(s) containing the keyword '{keyword}'.")