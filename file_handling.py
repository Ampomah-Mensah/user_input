# File Creation
def create_file():
    try:
        # Open "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("Hello, this is line 1\n")
            file.write("12345\n")
            file.write("Python file handling example\n")
        print("File 'my_file.txt' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the file: {e}")
    finally:
        print("File creation process completed.")

# File Reading and Display
def read_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            contents = file.read()
            print("Contents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to access 'my_file.txt'.")
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")
    finally:
        print("File reading process completed.")

# File Appending
def append_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the file
            file.write("Appending line 1\n")
            file.write("98765\n")
            file.write("More text added to file\n")
        print("Content appended to 'my_file.txt' successfully.")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")
    finally:
        print("File appending process completed.")

# Main function to execute file handling tasks
def main():
    create_file()   # Create the file
    print("\n")
    read_file()     # Read and display file contents
    print("\n")
    append_file()   # Append additional content to the file

if __name__ == "__main__":
    main()