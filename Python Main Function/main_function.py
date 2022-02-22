# Python program to demonstrate
# main() function


print("hello")

# Defining main function
def main():
	print("hey there")


# Using the special variable __name__
# when run as the main file, i.e. not imported, __name__ is set to "__main__"
# when imported, __name__ is set to the name of the module
if __name__ == "__main__":
    # this part of the code will only run if the script is run as the main file only
	main()
