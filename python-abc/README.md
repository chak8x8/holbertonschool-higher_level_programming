Python - Abstract Classes and Interfaces
========================================

- Amateur
- By: Javier Valenzani
- Weight: 1
- Your score will be updated as you progress.

Description
-----------

**Python OOP - Abstract Class, Interface, Subclassing**

### Introduction

Welcome to this set of exercises aimed at honing your understanding and application of Object-Oriented Programming (OOP) concepts in Python. Through these exercises, you will delve into abstract classes, interfaces, duck typing, and subclassing standard base classes among other crucial OOP concepts. By the end of these exercises, you should be proficient in employing OOP principles to design, implement, and test Python programs.

---

Learning Objectives
-------------------

- **Abstract Classes**: Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
- **Interfaces and Duck Typing**: Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
- **Subclassing Standard Base Classes**: Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
- **Method Overriding**: Employ method overriding to alter or enhance the behavior of base class methods.
- **Multiple Inheritance**: Understand and apply multiple inheritance to form complex relationships between classes.
- **Mixins**: Utilize mixins to compose behavior across unrelated classes.

Resources
---------

- **Python 3 Object-Oriented Programming**
- **ABC — Abstract Base Classes**
- **Real Python - Object-Oriented Programming (OOP) in Python 3**
- **Corey Schafer - OOP Playlist**
- **sentdex - Python OOP Tutorial**

The above resources provide a mix of reading material, interactive exercises, and video tutorials to cater to different learning styles. It’s recommended to go through these resources to build a solid understanding of OOP concepts in Python before attempting the exercises.

---

Tasks
-----

### 0. Abstract Animal Class and its Subclasses

**mandatory**

**Background**:  
In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python’s `abc` package facilitates the creation of abstract base classes.

**Objective**:  
- Create an abstract class named `Animal` using the `ABC` package. This class should have an abstract method called `sound`.
- Create two subclasses of `Animal`: `Dog` and `Cat`. Implement the `sound` method in each subclass to return the strings `"Bark"` and `"Meow"` respectively.

**Resources**:  
- Python ABC documentation: <https://docs.python.org/3/library/abc.html>

**Instructions**:

1. **Setting up the Abstract Class**:
   - Import the necessary components from the `abc` module.
   - Define the `Animal` class, ensuring it inherits from `ABC` to mark it as abstract.
   - Inside the `Animal` class, declare an abstract method named `sound` using the `@abstractmethod` decorator.

2. **Implementing the Subclasses**:
   - Create a subclass named `Dog` that inherits from the `Animal` class.
   - Implement the `sound` method in the `Dog` class to return the string `"Bark"`.
   - Similarly, create a subclass named `Cat` that also inherits from the `Animal` class.
   - Implement the `sound` method in the `Cat` class to return the string `"Meow"`.

**Hints**:
- The abstract method in the base class doesn’t have a body. You need to provide the implementation in the subclasses.
- If you try to instantiate a class that hasn’t implemented all of its abstract methods, Python will raise a `TypeError`.

```
$ cat main_00_abc.py 
#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())

$ ./main_00_abc.py 
Bark
Meow
Traceback (most recent call last):
  File "main_00_abc.py", line 10, in <module>
    animal = Animal()
TypeError: Can't instantiate abstract class Animal with abstract method sound
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_00_abc.py`

---

### 1. Shapes, Interfaces, and Duck Typing

**mandatory**

**Background**:  
Python employs a concept called “duck typing,” which is concerned with the semantics of objects rather than their inheritance hierarchy. If an object behaves like a duck (i.e., has all the methods and properties of a duck), then it’s considered a duck, regardless of its actual class. This concept allows for flexible and dynamic polymorphism.

**Objective**:  
- Create an abstract class named `Shape` with two abstract methods: `area` and `perimeter`.
- Implement two concrete classes: `Circle` and `Rectangle`, both inheriting from `Shape`. Each class should provide implementations for the `area` and `perimeter` methods.
- Write a standalone function named `shape_info` that accepts an object of type `Shape` (by duck typing) and prints its area and perimeter.
- Test the `shape_info` function with instances of both `Circle` and `Rectangle`.

**Resources**:  
- Python ABC documentation: <https://docs.python.org/3/library/abc.html>
- Concept of Duck Typing: <https://realpython.com/lessons/duck-typing/>

**Instructions**:

1. **Shape Abstract Class**:
   - Define an abstract class `Shape` using the `ABC` package.
   - Within `Shape`, declare two abstract methods: `area` and `perimeter`.

2. **Circle and Rectangle Classes**:
   - Create a `Circle` class that inherits from `Shape`. The constructor should accept a `radius`. Implement the `area` and `perimeter` methods.
   - Create a `Rectangle` class, also inheriting from `Shape`. Its constructor should accept the `width` and `height`. Implement the `area` and `perimeter` methods.

3. **shape_info Function**:
   - Define a function named `shape_info` that takes a single argument.
   - Without explicitly checking the type of the argument, call its `area` and `perimeter` methods (relying on duck typing).
   - Print the area and perimeter of the shape passed to the function.

4. **Testing**:
   - Instantiate a `Circle` and a `Rectangle`.
   - Pass each object to the `shape_info` function and observe the output.

**Hints**:
- While Python doesn’t enforce interfaces in the same way as statically-typed languages, abstract base classes provide a mechanism to ensure certain methods are implemented in subclasses.
- Duck typing in the `shape_info` function implies that you **shouldn’t** use `isinstance` checks. Instead, trust that the passed object adheres to the `Shape` interface.

```
$ cat main_01_duck_typing.py 
#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)

$ ./main_01_duck_typing.py 
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_01_duck_typing.py`

---

### 2. Extending the Python List with Notifications

**mandatory**

**Background**:  
In Python, you can extend built-in classes to add or modify behavior. The `list` class provides a collection of methods that handle list operations. By extending the `list` class, you can provide custom behaviors while retaining the original functionalities.

**Objective**:  
Create a class named `VerboseList` that extends the Python `list` class. This custom class should print a notification message every time an item is added (using the `append` or `extend` methods) or removed (using the `remove` or `pop` methods).

**Instructions**:

1. **Setting up the VerboseList Class**:
   - Define a class `VerboseList` that inherits from the built-in `list` class.
   - Within `VerboseList`, override the methods that modify the list: `append`, `extend`, `remove`, and `pop`.

2. **Implementing Notifications**:
   - For `append`: After adding the item, print a message like **"Added [item] to the list."**
   - For `extend`: After extending the list, print a message like **"Extended the list with [x] items."** where `[x]` is the number of items added.
   - For `remove`: Before removing the item from the list, print **"Removed [item] from the list."**
   - For `pop`: Before popping the item from the list, print **"Popped [item] from the list."** If the index is not specified, default behavior is to pop the last item.

3. **Testing**:
   - Instantiate a `VerboseList` object.
   - Test all the overridden methods (`append`, `extend`, `remove`, `pop`) and ensure that the appropriate messages are printed for each operation.

**Hints**:
- Remember to call the original method of the `list` class using `super()` so the original functionality is retained.  
- Watch out for edge cases, such as trying to remove an item that doesn’t exist.

```
$ cat main_02_verboselist.py 
#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)

$ ./main_02_verboselist.py 
Added [4] to the list.
Extended the list with [2] items.
Removed [2] from the list.
Popped [6] from the list.
Popped [1] from the list.
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_02_verboselist.py`

---

### 3. CountedIterator - Keeping Track of Iteration

**mandatory**

**Background**:  
Subclassing allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance behavior. The `iter` function returns an iterator object, which provides the `__next__` method to fetch the next item in the sequence. This exercise focuses on extending the functionality of this iterator object.

**Objective**:  
Create a class named `CountedIterator` that extends the built-in iterator obtained from the `iter` function. The `CountedIterator` should keep track of the number of items that have been iterated over. Specifically, you will need to override the `__next__` method to increment a counter each time an item is fetched.

**Instructions**:

1. **Setting up the CountedIterator Class**:
   - Define a class `CountedIterator`.
   - In the constructor (`__init__`), initialize two attributes: the iterator object (using `iter(some_iterable)`) and a counter to track the number of items iterated.
   - Provide a method `get_count` to return the current value of the counter.

2. **Overriding the next Method**:
   - Within the `CountedIterator` class, override the `__next__` method.
   - In this method, increment the counter each time `__next__` is called.
   - Fetch the next item from the original iterator and return it. If there are no items left, raise `StopIteration`.

3. **Testing**:
   - Instantiate a `CountedIterator` object with a list or other iterable.
   - Iterate over items using a loop or manual calls to the `__next__` method.
   - Use the `get_count` method to retrieve and print the number of items that have been fetched.

**Hints**:
- The `__next__` method should raise `StopIteration` when there are no more items.
- You can store `self.iterator = iter(some_iterable)` in the constructor.

```
$ cat main_03_countediterator.py 
#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")

$ ./main_03_countediterator.py 
Got 1, total 1 items iterated.
Got 2, total 2 items iterated.
Got 3, total 3 items iterated.
Got 4, total 4 items iterated.
No more items.
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_03_countediterator.py`

---

### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance

**mandatory**

**Background**:  
In some object-oriented languages, a class can inherit from more than one parent class—known as multiple inheritance. Python supports multiple inheritance, which can be powerful but also complex. Method resolution order (MRO) determines how Python looks up methods in a multiple-inheritance hierarchy.

**Objective**:  
Construct a `FlyingFish` class that inherits from both a `Fish` class and a `Bird` class. Within `FlyingFish`, override methods from both parents. The goal is to understand multiple inheritance and how Python determines method resolution order.

**Instructions**:

1. **Parent Classes Setup**:
   - Create a `Fish` class with methods `swim` (prints `"The fish is swimming"`) and `habitat` (prints `"The fish lives in water"`).
   - Create a `Bird` class with methods `fly` (prints `"The bird is flying"`) and `habitat` (prints `"The bird lives in the sky"`).

2. **Implementing FlyingFish**:
   - Construct a `FlyingFish` class that inherits from both `Fish` and `Bird`.
   - Override the `fly` method to print `"The flying fish is soaring!"`.
   - Override the `swim` method to print `"The flying fish is swimming!"`.
   - Override the `habitat` method to print `"The flying fish lives both in water and the sky!"`.

3. **Testing and MRO Exploration**:
   - Instantiate a `FlyingFish` object.
   - Call the `fly`, `swim`, and `habitat` methods.
   - Use the `mro()` method (e.g., `print(FlyingFish.mro())`) to investigate method resolution order.

**Hints**:
- The order in which you list parent classes in the `FlyingFish` definition affects method resolution order.
- Use multiple inheritance judiciously to avoid complexities.

```
$ cat main_04_flyingfish.py 
#!/usr/bin/env python3
from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

$ ./main_04_flyingfish.py 
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_04_flyingfish.py`

---

### 5. The Mystical Dragon - Mastering Mixins

**mandatory**

**Background**:  
Mixins are a way to add functionality to classes in a modular fashion. They are not meant to stand alone but to be combined with other classes to add behaviors. By using mixins, you can compose functionality across different classes without deep or rigid inheritance hierarchies.

**Objective**:  
Design two mixin classes, `SwimMixin` and `FlyMixin`, each equipped with methods `swim` and `fly` respectively. Next, construct a class `Dragon` that inherits from both these mixins. Your goal is to show that a `Dragon` instance can both swim and fly.

**Instructions**:

1. **Creating Mixins**:
   - Design a mixin called `SwimMixin` with a method `swim` that prints `"The creature swims!"`.
   - Design another mixin called `FlyMixin` with a method `fly` that prints `"The creature flies!"`.

2. **Implementing Dragon**:
   - Construct a class named `Dragon` that inherits from both `SwimMixin` and `FlyMixin`.
   - Optionally add other methods or attributes, like `roar` which prints `"The dragon roars!"`.

3. **Testing the Dragon’s Abilities**:
   - Instantiate an object named `draco = Dragon()`.
   - Demonstrate `draco`’s abilities by calling `draco.swim()`, `draco.fly()`, and `draco.roar()` (if implemented).

**Hints**:
- Mixins should be focused, providing a single piece of functionality.  
- Mixins allow code reusability and flexible class composition.

```
$ cat main_05_dragon.py 
#!/usr/bin/env python3
from task_05_dragon import Dragon

dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!

$ ./main_05_dragon.py 
The creature swims!
The creature flies!
The dragon roars!
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_05_dragon.py`