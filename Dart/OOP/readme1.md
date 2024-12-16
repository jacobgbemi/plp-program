🎯 Learning Objectives 🚀

Understand the KEYWORDS in object-oriented programming. 🗝️

Grasp the paradigms of OOP and why it's a game-changer! 🌟

Get introduced to Factory Methods, Singletons, and Mixins—because who doesn’t like extra features? 🛠️

OOP in Dart 🎩💻

Welcome to the magical world of Object-Oriented Programming (OOP)! ✨ It’s all about designing apps using objects—whether it's a person 🧍‍♂️, a car 🚗, or even a bank account 🏦. In OOP, objects have their own attributes (like name, color, or age) and behaviors (like walking, talking, or driving). Cool, right?

OOP isn’t just some fancy concept—it’s one of the most popular programming paradigms out there, used in Dart, Java, Python, and more! 🌎

Why OOP is Awesome! 🤩

🧠 Easy to understand and use—no rocket science here!

🔁 Reusability FTW—code once, use it again and again!

⚙️ Less complex—because no one likes headaches. 😅

📈 Boosts productivity—get more done in less time!

👥 Teamwork-friendly—collaborate like a pro!

🛠️ Easier to maintain—fix bugs without breaking everything. 🐞

Features of OOP 💡

Class 📚: A blueprint for creating objects (like a recipe for cookies 🍪).

Object 🎯: The actual instance created from the class (like a cookie 🍪 made from the recipe).

Encapsulation 🛡️: Wrapping code into neat little packages.

Inheritance 👨‍👧: Reusing properties from another class. (Dogs inherit from Animals 🐶🐾)

Polymorphism 🎭: One method, many forms!

Abstraction 💼: Only showing the essential features.

Key Points ✍️

OOP uses objects and their interactions to build programs. 🛠️

Objects = Data + Methods (actions they can do!).

Think modular, flexible, and scalable. 🔄

OOP is like a superpower for problem-solving! 💥

Classes in OOP 🎓

In OOP, a class is like a recipe that defines what an object will be like. For example, a class called Dog might have properties like breed 🐕 and color 🎨, and methods like bark 🐶🔊 or run 🏃‍♂️. Once you've got the class, you can create as many dog objects as you want! (Infinite puppies, anyone? 🐾)

Let’s go build some awesome objects and make your code smarter, faster, and cleaner! 🧑‍💻



Declaring A class in Dart

In Dart programming, you can declare a class using the class keyword followed by the class name. Here's a simple example:

// Declaring a class in Dart

class Person {

 // Properties of the class

 String name;

 int age;




 // Constructor

 Person(this.name, this.age);




 // Method to display person details

 void displayInfo() {

  print('Name: $name, Age: $age');

 }

}

Class Declaration:

The class keyword is used to declare a class, followed by the class name Person.
Objects

An object is an instance of a class. It represents a real-world entity with attributes (properties) and behaviors (methods). Objects allow you to create multiple instances of a class, each with its own unique data.



// Declaring a simple class in Dart

class Car {

 String brand;

 String model;




 Car(this.brand, this.model);




 void showDetails() {

  print('Brand: $brand, Model: $model');

 }

}




void main() {

 // Creating an object of the Car class

 Car myCar = Car('Toyota', 'Corolla');

  

 // Calling the method using the object

 myCar.showDetails(); // Output: Brand: Toyota, Model: Corolla

}





Class Declaration:

The Car class has two properties: brand and model.
The constructor Car(this.brand, this.model); initializes these properties.

Object Creation:

Car myCar = Car('Toyota', 'Corolla'); creates an object myCar of the Car class with specific values for brand and model.





🎯 Object-Oriented Programming (OOP) 🧩

OOP is like organizing your code into real-world objects 🌍, not just boring functions and logic! It’s all about data (objects) and what they can do. 🚀 Think of objects as containers that hold both data (attributes) and their behavior (methods).

Components of OOP 🛠️

Constructor 🏗️:

A constructor is like a welcome party for your object! 🎉

It’s a special function that runs automatically when an object is created. 💫

Its main job is to set up the object’s properties and make sure everything is in place. 🔧

In Dart, the constructor has the same name as the class (no guessing games here!).

There are two main types of constructors in Dart, and they’re ready to bring your objects to life! 👾



Default constructor: A default constructor is automatically created if no other constructor is specified.

No parameter required.

Initializes instance variables to their default values ​​(null for objects, 0 for integers, etc.).



class MyDetails {
  String name = 'Unknown';
  int age = 0;
}

void main() {
  MyDetails myDetails = MyDetails();
  print("Name: ${myDetails.name}, Age: ${myDetails.age}");
}

In this example:

The MyDetails class has a default constructor, which doesn't take any parameters.
Inside the constructor, you can add any initialization code if needed.
In the main() function, an instance of MyDetails named myDetails is created using the default constructor.





Parameterized Constructors: Parameterized constructors allow you to pass a value during object creation, allowing you to initialize instance variables with specific values.

class MyDetails {
  String name;
  int age;

  // Parameterized constructor
  MyDetails(this.name, this.age);
}

void main() {
  // Creating an instance of MyDetails using the parameterized constructor
  MyDetails myDetails = MyDetails('Allan', 25);
  print("Name: ${myDetails.name}, Age: ${myDetails.age}");
}




Object Oriented Programming Paradigm

🔒 Data Encapsulation: Your Code's Secret Vault! 🔒

Data encapsulation keeps your class's implementation details safe from users, using an object's functions to control access. This enhances security and promotes cleaner code! 🌟

🚀 How to Achieve Encapsulation in Dart 🚀

Hide Your Secrets: Declare class properties as private by prefixing with an underscore (_). This locks away your valuable data! 📦🔒

Public Access: Create getter and setter methods to control access to private properties. These methods act as the keys to your vault! 🗝️💼

🏷️ Getter and Setter Methods: Your Access Control Team! 🏷️

Getter Methods: Friendly guides that safely reveal private property values—no risk of meddling! 🎤✨

Setter Methods: Vigilant bouncers that allow authorized changes to private properties—keeping your vault secure! 💃🎉



Code sample

class Circle {
  // Private property with underscore (_)
  double _radius;

  // Constructor to initialize the radius
  Circle(this._radius);

  // Getter method to access the private radius
  double get radius => _radius;

  // Setter method to update the radius with validation
  set radius(double value) {
    if (value > 0) {
      _radius = value;
    } else {
      print('Radius must be greater than 0');
    }
  }

  // Method to calculate area of the circle
  double calculateArea() {
    return 3.1416 * _radius * _radius; // Area = πr²
  }
}

void main() {
  // Creating an instance of Circle
  Circle circle = Circle(5.0);

  // Accessing the radius using getter
  print("Initial radius: ${circle.radius}");

  // Calculating and printing the area
  print("Initial area: ${circle.calculateArea()}");

  // Updating the radius using setter
  circle.radius = 7.0;

  // Accessing updated radius and area
  print("Updated radius: ${circle.radius}");
  print("Updated area: ${circle.calculateArea()}");

  // Trying to set an invalid radius
  circle.radius = -3.0; // This will trigger validation
}


Explanation

The Circle class has a private variable _radius, which is not directly accessible from outside the class.
The constructor initializes the _radius variable.
Getter (get radius) allows external code to access the value of _radius.
Setter (set radius) provides controlled access to update the value of _radius with validation.

The calculateArea method demonstrates how methods can use the encapsulated data.





🌳 Inheritance: The Family Tree of Code! 🌳

Inheritance is like inheriting your favorite traits from family members—only in the world of OOP! 🎉 It’s the magical process that lets one object inherit properties and behaviors from another.

🦸‍♂️ Why Inherit?

Imagine you're a SuperDog 🐕‍🦸‍♂️ with all the cool features of a regular Dog 🐶 but with some superpowers thrown in! Inheritance allows you to:

Reuse Code: Save time and energy by building on existing properties instead of starting from scratch! ⏳💡

Create a Hierarchy: Build a family tree of classes, where child classes can share the awesome traits of parent classes! 📜🌟

Code sample

// Base class (Superclass)
class Vehicle {
  String brand;
  int year;

  // Constructor for Vehicle
  Vehicle(this.brand, this.year);

  // Method to display vehicle info
  void displayInfo() {
    print("Brand: $brand");
    print("Year: $year");
  }
}

// Derived class (Subclass) inheriting from Vehicle
class Car extends Vehicle {
  String model;

  // Constructor for Car which uses super to call the base class constructor
  Car(String brand, int year, this.model) : super(brand, year);

  // Method to display car-specific info
  void displayCarInfo() {
    displayInfo(); // Call the base class method
    print("Model: $model");
  }
}

void main() {
  // Creating an instance of the Car class
  Car car = Car('Toyota', 2021, 'Corolla');

  // Accessing methods from both base and derived classes
  car.displayCarInfo();
}


Explanation

The Vehicle class is the base class with instance variables brand and year, and a method displayInfo.
The Car class is the derived class that extends (inherits from) the Vehicle class. It adds an additional property model and a method displayCarInfo.
The Car constructor uses super to call the constructor of the base class (Vehicle).
The main function demonstrates creating an instance of the Car class and accessing methods from both the base and derived classes.





🎭 Polymorphism: The Chameleon of OOP! 🎨

Welcome to the world of Polymorphism, where one method can wear many hats! 🎩✨ Think of it as a party where all your favorite classes gather, and each one brings their own unique twist to the same method name!

🔄 Why Polymorphism Rocks:

One Method, Many Forms: Just like a chameleon changes color, polymorphism allows different classes to redefine a method while keeping the same name! 🦎

Flexibility Galore: This ability gives you the power to call the same method on different objects and get results that match their unique behaviors! It’s like having a universal remote for your code! 📺

Code sample

// Base class
class Animal {
  // Method to be overridden by derived classes
  void makeSound() {
    print("Animal makes a sound");
  }
}

// Derived class Dog that overrides makeSound method
class Dog extends Animal {
  @override
  void makeSound() {
    print("Dog barks");
  }
}

// Derived class Cat that overrides makeSound method
class Cat extends Animal {
  @override
  void makeSound() {
    print("Cat meows");
  }
}

void main() {
  // Creating instances of Animal, Dog, and Cat
  Animal animal = Animal();
  Dog dog = Dog();
  Cat cat = Cat();

  // Calling makeSound method for each instance
  animal.makeSound(); // Calls Animal's version
  dog.makeSound();    // Calls Dog's version
  cat.makeSound();    // Calls Cat's version
}


Explanation

The Animal class is the base class with a method makeSound.
The Dog and Cat classes are derived classes that override the makeSound method with their own implementations.
In the main function, instances of Animal, Dog, and Cat are created.
The makeSound method is called on each object, demonstrating polymorphism as the appropriate version of the method is invoked based on the actual type of the object.





🌟 Abstraction: Simplifying Complexity! 🎉

Abstraction is like a magic lens that lets users interact only with the essential features of an object, while keeping the intricate details hidden away. It’s all about making the complicated simple! 🪄✨

🧐 What is Abstraction?

User-Friendly Interaction: Imagine you're using a remote control. You don’t need to know how the remote works internally; you just press buttons to change channels or adjust the volume. That’s the essence of abstraction! It allows users to access just a subset of an object’s characteristics and operations, simplifying their experience. 📺🔧

Simplicity Reveals Complexity: Abstraction takes complex systems and presents them in a straightforward manner. Think of it as showing only the tip of the iceberg while the vast majority lies beneath the surface!







Code example

// Abstract class Shape
abstract class Shape {
  // Abstract method (no implementation)
  double calculateArea();

  // Concrete method (with implementation)
  void printInfo() {
    print("This is a shape.");
  }
}

// Concrete class Circle extends Shape
class Circle extends Shape {
  double radius;

  // Constructor for Circle
  Circle(this.radius);

  // Override the abstract method to provide specific implementation
  @override
  double calculateArea() {
    return 3.14 * radius * radius;
  }
}

// Concrete class Rectangle extends Shape
class Rectangle extends Shape {
  double width;
  double height;

  // Constructor for Rectangle
  Rectangle(this.width, this.height);

  // Override the abstract method to provide specific implementation
  @override
  double calculateArea() {
    return width * height;
  }
}

void main() {
  // Create instances of Circle and Rectangle
  Circle circle = Circle(5.0);
  Rectangle rectangle = Rectangle(10.0, 20.0);

  // Using the common interface provided by the Shape abstract class
  circle.printInfo();  // Calls the concrete method in the abstract class
  print("Circle Area: ${circle.calculateArea()}");

  rectangle.printInfo();  // Calls the concrete method in the abstract class
  print("Rectangle Area: ${rectangle.calculateArea()}");
}


Explanation

The Shape class is an abstract class with an abstract method calculateArea() and a concrete method printInfo().
The Circle and Rectangle classes are concrete classes that extend the Shape class and provide implementations for the abstract method.
In the main function, instances of Circle and Rectangle are created and used through the common interface provided by the Shape abstract class.



FACTORY METHODS

Welcome to the Factory of Fun in Dart! 🎉 Factory constructors are like wizards for creating class instances, offering alternative ways to conjure objects. Need a specific type or subclass? No problem—just like a secret menu at your favorite eatery! 🍔✨

Here’s the scoop: factory constructors do use the return keyword to serve up your creations! 🛎️ But remember, you can’t refer to this inside a factory—think of it as a playful twist in the rules! 🤷‍♂️

So dive into the factory methods of Dart, where object creation is an enchanting experience! 🏭✨ Let your coding magic shine! 🎩🚀





import 'dart:math'; // Import math library to use pi

// Circle Class Definition
class Circle {
  double radius; // Instance variable to store the radius of the circle

  // Constructor to initialize the radius
  Circle(this.radius);

  // Factory constructor to control instance creation
  factory Circle.create(double radius) {
    // Ensure the radius is positive before creating the instance
    if (radius > 0) {
      return Circle(radius); // Return a new Circle instance
    } else {
      // Throw an error if the radius is not valid
      throw ArgumentError('Radius must be greater than zero');
    }
  }

  // Method to calculate the area of the circle
  double calculateArea() {
    return pi * radius * radius; // Area formula: pi * radius^2
  }
}

void main() {
  // Using the factory constructor to create circle instances
  Circle circle1 = Circle.create(5.0); // Create a circle with radius 5.0
  Circle circle2 = Circle.create(10.0); // Create a circle with radius 10.0

  // Print the area of the circles by calling the calculateArea method
  print('Circle 1 Area: ${circle1.calculateArea()}'); // Output: Circle 1 Area
  print('Circle 2 Area: ${circle2.calculateArea()}'); // Output: Circle 2 Area

  // Example of error handling for invalid radius
  try {
    Circle circle3 = Circle.create(-3.0); // Invalid radius, will throw an error
  } catch (e) {
    print(e); // Catch and print the error message
  }
}


Explanation:

1.Circle Class:

The Circle class represents a circle with a given radius.
It has an instance variable radius to store the radius of the circle.
The constructor Circle(this.radius) initializes the radius variable when an instance of Circle is created

2.Factory Method:

The Circle class contains a factory method create that takes a radius parameter.
It ensures that the radius is positive and then creates and returns a new instance of Circle with the given radius.
If the provided radius is not positive, it throws an ArgumentError.

3.Calculate Area Method:

The calculateArea() method calculates the area of the circle using the formula pi * radius * radius.

4.Main Function:

In the main() function:We create instances of Circle using the factory method Circle.create() with different radii.
We call the calculateArea() method on each circle instance to calculate and print its area.



SINGLETONS

Welcome to the Singleton Pattern club! 🎉 This pattern ensures your class has only one instance with global access, keeping your app organized and chaos-free! 🌍✨

Why one? Multiple instances can lead to confusion, like having two local storage wizards arguing! 😱 With the Singleton pattern, calling MyClass() gives you the same instance every time. 🎭✨

Thanks to factory constructors in Dart, implementing this pattern is a breeze! Keep your code sleek and consistent—let's rock the singleton way! 🚀🎊

// Singleton class to manage file system operations
class FileSystemManager {
  // Static and final instance variable to hold the single instance of the class
  static final FileSystemManager _instance = FileSystemManager._internal();

  // Private constructor to restrict external instantiation
  FileSystemManager._internal();

  // Factory constructor to control the creation of the singleton instance
  factory FileSystemManager() {
    return _instance; // Always returns the same instance
  }

  // Method to simulate opening a file
  void openFile(String fileName) {
    print('Opening file: $fileName');
  }

  // Method to simulate writing to a file
  void writeFile(String fileName, String content) {
    print('Writing to file: $fileName with content: "$content"');
  }
}

void main() {
  // Create two references to the FileSystemManager singleton instance
  FileSystemManager manager1 = FileSystemManager(); // Uses factory constructor
  FileSystemManager manager2 = FileSystemManager(); // Returns the same instance

  // Verify that both references point to the same singleton instance
  print('Are manager1 and manager2 the same instance? ${identical(manager1, manager2)}');
  print('HashCode of manager1: ${manager1.hashCode}');
  print('HashCode of manager2: ${manager2.hashCode}');

  // Calling methods on both references
  manager1.openFile("data.txt");    // Opens the file using manager1
  manager2.writeFile("data.txt", "Hello, Dart!"); // Writes to the file using manager2
}




1.Singleton Design Pattern:

The FileSystemManager class is implemented using the Singleton design pattern, which ensures that there is only one instance of the class throughout the application's lifecycle.

2.Static Instance Variable:

The _instance variable is declared as static and final, meaning it is associated with the class itself rather than with instances of the class. This variable holds the single instance of the FileSystemManager class.

3.Private Constructor:

The _internal constructor is private, indicated by the underscore _, meaning it can only be accessed from within the FileSystemManager class. This constructor is used for initialization logic and is called only once to create the singleton instance of the class.

4.Factory Constructor:

The FileSystemManager class provides a factory constructor that ensures only one instance of the class is returned. This factory constructor checks if _instance is null, and if so, it creates a new instance using the private _internal constructor. Otherwise, it returns the existing instance.

5.Usage:

In the main() function, two instances of FileSystemManager named manager1 and manager2 are created.
The hashCode comparison confirms that both manager1 and manager2 reference the same singleton instance, as expected in a Singleton pattern.
The openFile() and writeFile() methods of FileSystemManager are called on manager1 and manager2, respectively, demonstrating that both instances share the same behavior implemented by the singleton instance.



MIXINS

Mixins are the cool kids of the coding playground! 🌟 They let you reuse code across different class hierarchies without making a messy sandwich of inheritance. 🥪✨

Imagine you have an Employee class rocking methods like clockIn. Now, both a Bartender and a Nurse can benefit from this functionality. But wait—what if you have a Doctor who also needs the takeTemperature magic, but you don’t want to bloat the Employee class? 🤔

Enter the Mixins! 🎭💥 By creating a mixin called Medical, you can sprinkle that doctorly functionality wherever it’s needed—without the extra baggage! It’s like having your cake and eating it too! 🍰🎉

So let’s mix it up and keep our classes tidy and fun! 🥳🔧



// Base class Employee
class Employee {
  // Method that simulates an employee clocking in
  void clockIn() {
    print("Employee clocked in");
  }
}

// Mixin for medical-related functionality
mixin Medical {
  // Method that simulates taking a patient's temperature
  int takeTemperature() {
    print("Taking temperature");
    return 98; // Returns a sample temperature value
  }
}

// Class Nurse extends Employee and mixes in Medical
class Nurse extends Employee with Medical {
  // Inherits clockIn from Employee
  // Inherits takeTemperature from Medical
}

// Class Doctor extends Employee and mixes in Medical
class Doctor extends Employee with Medical {
  // Inherits clockIn from Employee
  // Inherits takeTemperature from Medical

  // Method specific to Doctor for performing surgery
  void performSurgery() {
    print("Performing surgery");
  }
}

// Class Bartender extends Employee but does not mix in Medical
class Bartender extends Employee {
  // Inherits clockIn from Employee
  // Does not have access to takeTemperature or performSurgery
}

void main() {
  // Create instances of different employee types
  Nurse nurse = Nurse();
  Doctor doctor = Doctor();
  Bartender bartender = Bartender();

  // Use inherited methods
  nurse.clockIn(); // Calls clockIn method from Employee class
  nurse.takeTemperature(); // Calls takeTemperature from Medical mixin

  doctor.clockIn(); // Calls clockIn method from Employee class
  doctor.takeTemperature(); // Calls takeTemperature from Medical mixin
  doctor.performSurgery(); // Calls Doctor-specific method

  bartender.clockIn(); // Bartender can only clock in, as it doesn't mix in Medical
}

Mixins keep everything neat and functional, ensuring everyone gets just what they need! 🎈✨



EXTENSION METHODS 

What Are Extension Methods?
Imagine having a magic wand that allows you to sprinkle a little extra sparkle on your existing classes in Dart! 🪄✨ That’s exactly what extension methods do! They let you add brand-new methods to classes or interfaces without changing their original design. So, if you’ve ever wished for more powers in a class you didn’t create, extension methods are your new best friends!





// Extending the String class with an extension method

extension StringExtensions on String {

 // Method to capitalize the first letter of a string

 String capitalizeFirstLetter() {

  if (this.isEmpty) {

   return this;

  }

  return this[0].toUpperCase() + this.substring(1);

 }

}




void main() {

 // Create a String object

 String message = "hello, world!";

  

 // Use the extension method to capitalize the first letter

 String capitalizedMessage = message.capitalizeFirstLetter();

  

 // Print the result

 print(capitalizedMessage); // Output: Hello, world!

}



Explanation:
Extension Declaration:
extension StringExtensions on String { ... } defines an extension named StringExtensions that adds functionality to the String class.
Adding a Method:
String capitalizeFirstLetter() { ... } is a method added to the String class. It checks if the string is empty, and if not, it returns the string with the first letter capitalized.
Using the Extension Method:
In the main() function, message.capitalizeFirstLetter() calls the new method on a String object, demonstrating how the extension method can be used just like a regular method of the class.

