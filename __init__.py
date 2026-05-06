import os



currentdir= os.getcwd()
print(currentdir)

print("Change the Directory")

directory=(input("Enter your desire directory"))
chdir= os.chdir(directory)
print(os.getcwd())

print(f"Now your directory is:", os.getcwd())
