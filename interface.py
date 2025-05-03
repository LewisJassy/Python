# An interface is a concept in oop that contain methods definition which a class must implement.
# Step 1: Define an interface using ABC modulesince python does not have a built-in one

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # abstract method(no implementation required)

    def stop(self):
        pass

# Step 2: Implemetenting an interface
# We implement an interface by inheriting from a class by providing a concrete implementation of the abstract method

class Car(Vehicle):
    def start(self):
        print("Car starting")
    def stop(self):
        print("car stopping")

# Step 3: Use the implemented class

if __name__ == "__main__":
    car = Car()
    car.start()
    car.stop()
