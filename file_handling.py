# Tasks:
# File Creation:
# Create a Python script (file_handling_assignment.py) that does the following:
# Creates a new text file named "my_file.txt" in write mode ('w').
# Write at least three lines of text to the file, including a mix of strings and numbers.

# File Reading and Display:
# Enhance your script to read the contents of "my_file.txt" and display them on the console.

# File Appending:
# Modify the script to open "my_file.txt" in append mode ('a').
# Append three additional lines of text to the existing content.

# Error Handling:
# Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).


def main():
    filename = "my_file.txt"

    try:
        with open(filename, 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 4567.\n")
            file.write("Finally, this is the third line!\n")
        print("File created and content written successfully.")

    except (PermissionError, OSError) as e:
        print(f"Error occurred while creating the file: {e}")

    try: 
        with open(filename, "r") as file:
            content = file.read()
            print("\nContents of the file:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except (PermissionError, OSError) as e:
        print(f"Error occurred while reading the file: {e}")

    
    try:
        with open(filename, 'a') as file:
            file.write("This is the appended first line.\n")
            file.write("Here is another appended line with a number: 67890.\n")
            file.write("And this is the last appended line.\n")
        print("Additional content appended successfully.")

    except (PermissionError, OSError) as e:
        print(f"Error occurred while appending to the file: {e}")

    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nUpdated contents of the file after appending:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except (PermissionError, OSError) as e:
        print(f"Error occurred while reading the file: {e}")
    


if __name__=="__main__":
    main()