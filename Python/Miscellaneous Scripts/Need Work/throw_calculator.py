# Python Throw Calculator
# TODO Need to add units to the calculator so that the user can understand the number that they're getting. Also need to go through and make sure that all the math was coded correctly.

import math

gravity = 9.805

thrower_length = int(input("What is the length of the thrower? "))
thrower_throw_power = int(input("What is the throw power of the thrower? "))
thrower_mass = int(input("What is the mass of the thrower? "))
object_mass = int(input("What is the mass of the object beeing thrown? "))
object_diameter = int(
    input("What is the diameter of the object being thrown? "))
object_drag = int(input("What is the drag of the object being thrown? "))

first = ((3 * thrower_length * thrower_throw_power * thrower_mass) /
         (object_mass + (thrower_mass/1000))) ** (1/3)

second = math.sqrt((2 * object_mass * gravity) / (math.pi *
                   ((object_diameter / 2) ** 2) * 1.2041 * object_drag))

final_distance = ((first ** 2) * math.sqrt(2)) / (gravity * math.sqrt(
    (first ** 4) / (second ** 4)) * 0.8 + ((first ** 2) / (second ** 2)) * 3 + 2)

print("After all of that, your final throw distance was " + str(final_distance))
