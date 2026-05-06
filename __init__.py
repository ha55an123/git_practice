import os



currentdir= os.getcwd()
print(currentdir)

print("Change the Directory")

directory=(input("Enter your desire directory"))
chdir= os.chdir(directory)
print(os.getcwd())
