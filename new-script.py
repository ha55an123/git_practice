import os

directory = input("Enter directory: ")

try:
    os.chdir(directory)
    # Now that we are "there", let's do something
    print(f"Listing files in {os.getcwd()}:")
    print(os.listdir()) # This runs IN the new directory
except FileNotFoundError:
    print("Invalid path")


print(f"Now your current working directroy is:", os.getcwd())
