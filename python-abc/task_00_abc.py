#!/usr/bin/python3
"""Defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for all animals."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass  # No implementation in the abstract class

class Dog(Animal):
    """Concrete class representing a Dog."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"

class Cat(Animal):
    """Concrete class representing a Cat."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
