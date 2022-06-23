# Declare the Person class and define what it contains
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creates an introducing function using the Person class to form an introduction


def introducing_func(self):
    print("Hello! My name is " + self.name +
          ", and I am " + str(self.age) + " years old.")

    if self.name == "Jonathan":
        if self.age == 15:
            last_name = input("Wait a minute, what's your last name?")

            if self.last_name == "Milligan":
                print("This is either some freak coincidence or you are THE Jonathan Milligan who created me. It is an honor to meet you, sir.")


# Gets the input to fulfill the information
input_name = input("What's your name? ")
input_age = input("What's your age? ")

# This variable uses the input information to create an object in the Person class
person = Person(input_name, input_age)

# Finally, this calls the introducing function and gives it the person var above as information
introducing_func(person)
