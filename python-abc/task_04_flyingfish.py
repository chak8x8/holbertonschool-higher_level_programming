#!/usr/bin/python3
"""Defines a FlyingFish class demonstrating multiple inheritance."""


class Fish:
    """Represents a fish with swimming behavior."""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Represents a bird with flying behavior."""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish inheriting from both Fish and Bird."""
    def __init__(self):
        """FlyingFish constructor"""
        print("A FlyingFish is created!")

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# ✅ Testing
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()    # "The flying fish is swimming!"
    flying_fish.fly()     # "The flying fish is soaring!"
    flying_fish.habitat() # "The flying fish lives both in water and the sky!"

    # ✅ Checking Method Resolution Order (MRO)
    print(FlyingFish.mro())  # MRO order
