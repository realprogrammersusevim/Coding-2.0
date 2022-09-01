import os

dir = input("Enter the directory path: ")
files = os.listdir(dir)
num_files = len(files)
counter = 0

for file in files:
    counter += 1
    file_extension = file.split(".")[-1]
    # Rename the file to the counter with leading zeros
    new_name = f"{counter:03d}.{file_extension}"
    os.rename(f"{dir}/{file}", f"{dir}/{new_name}")
