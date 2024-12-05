void main() {
  // Anonymous function assigned to the variable `printName`
  var printName = () {
    // Print message inside the anonymous function
    print("My name is Mariam");
  };

  // Call the anonymous function
  printName();


  // List of fruits
  var fruits = ['Apple', 'Banana', 'Cherry', 'Date'];

  // Using an anonymous function with forEach to print each fruit
  fruits.forEach((fruit) {
    print(fruit);
  });


  // List of items
  var items = ['Laptop', 'Tablet', 'Smartphone', 'Smartwatch'];

  // Using an anonymous function with forEach to print each item
  items.forEach((item) {
    print(item);
  });
}