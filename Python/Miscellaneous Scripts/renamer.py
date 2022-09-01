import os

dir = input("Enter the directory path: ")
fill = len(str(os.listdir(dir))) + 1
counter = 0

# Rename files to numbers
for file in os.listdir(dir):
    counter += 1
    file_extension = file.split(".")[-1]
    new_name = f"{str(counter).zfill(fill)}.{file_extension}"
    os.rename(os.path.join(dir, file), os.path.join(dir, new_name))
