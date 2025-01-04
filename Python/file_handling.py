def modify_content(content):
    """
    Modify the content of the file.
    Here, we convert the text to uppercase as an example.
    """
    return content.upper()

def main():
    # Ask the user for the filename to read
    input_filename = input("Enter the filename to read: ").strip()
    
    try:
        # Attempt to open and read the file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Create the output filename
        output_filename = f"modified_{input_filename}"
        
        # Write the modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Modified content has been written to '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
