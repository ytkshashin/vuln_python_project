def read_file(filepath):
    # Vulnerable: Allows arbitrary file access
    with open(filepath, "r") as f:
        print(f.read())

if __name__ == "__main__":
    user_input = input("Enter file path to read: ")
    read_file(user_input)
