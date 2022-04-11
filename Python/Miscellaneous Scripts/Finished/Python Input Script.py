name = input("What is your name? ")
has_been_greeted = False

def greeting_function(person_to_greet = "Jonathan"):
        if person_to_greet == "Jonathan":
                print("Hail great creator Jonathan!")
                has_been_greeted = True
        else:
                print("Hello " + person_to_greet + "!")
                has_been_greeted = True

greeting_function(name)
print("Complete")