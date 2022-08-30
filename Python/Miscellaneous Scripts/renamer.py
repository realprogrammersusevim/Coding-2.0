import os

dir = input("Enter the directory path: ")
files = os.listdir(dir)
counter = 0

for file in files:
    counter += 1
    file_extension = file.split(".")[-1]
    new_name = f"{counter}.{file_extension}"
    os.rename(f"{dir}/{file}", f"{dir}/{new_name}")
