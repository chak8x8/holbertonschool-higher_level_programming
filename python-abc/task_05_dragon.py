#!/usr/bin/python3
"""Defines a Dragon class with flying and swimming abilities using mixins."""

class SwimMixin:
    """Mixin class to add swimming ability."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin class to add flying ability."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim and fly, inheriting from SwimMixin and FlyMixin."""
    def roar(self):
        print("The dragon roars!")

# Test case
if __name__ == "__main__":
    dragon = Dragon()  # ✅ Instantiating the Dragon correctly
    dragon.swim()  # Outputs: The creature swims!
    dragon.fly()   # Outputs: The creature flies!
    dragon.roar()  # Outputs: The dragon roars!
