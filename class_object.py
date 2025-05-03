# This file will help you understand class and object in Python

class House:
    # Constructor
    def __init__(self, apartment, flats, bangaloo):
        self.apartment = apartment
        self.flats = flats
        self.bangaloo = bangaloo

    # Method
    def display_info(self):
        print(f"House apartment: {self.apartment}, {self.flats}, {self.bangaloo}")

# We need to instantiate object from the class
"""Here we are initializing the class using its constructor"""
house1 = House("Fojil", "Kabete", "Jassy`s Home")


"""Referrencing the object through the var above to point to its memory location"""

house1.display_info()
