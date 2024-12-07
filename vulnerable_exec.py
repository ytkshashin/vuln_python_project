import os

def execute_command(command):
    # Vulnerable command execution
    os.system(command)

if __name__ == "__main__":
    user_input = input("Enter a shell command: ")
    execute_command(user_input)
