from cgi import print_exception


name_of_file = input("What should the file be named? ")
file_extension = input("What should the file extension be? ")

if file_extension == "":
    file_extension = ".py"

try:
    open(name_of_file + file_extension, "x")
except:
    print("An error occured")
