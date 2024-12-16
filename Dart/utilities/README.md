A sample command-line application with an entrypoint in `bin/`, library code
in `lib/`, and example unit test in `test/`.

Dart Utilities

Objective:

Explore various utility features in Dart for string manipulation, collections, file handling, and date/time operations.
Provide practical examples and use cases for each utility category.

In computers, a utility is a small program that provides an addition to the capabilities provided by the operating system. In some usages, a utility is a special and nonessential part of the operating system.

Date And Time

Dart offers utilities for working with dates and times, including classes for representing dates, times, durations, and intervals. These utilities allow developers to perform various operations like date arithmetic, formatting, parsing, and timezone handling.

import 'package:intl/intl.dart'; // Import the intl package for date formatting

void main() {
  // Current date and time
  DateTime now = DateTime.now();
  print('Current date and time: $now');
  
  // Creating a specific date and time
  DateTime specificDate = DateTime(2024, 9, 10, 14, 30);
  print('Specific date and time: $specificDate');

  // Formatting date and time
  String formattedDate = DateFormat('yyyy-MM-dd – kk:mm').format(now);
  print('Formatted date and time: $formattedDate');

  // Parsing a date string
  String dateString = '2024-09-10 14:30';
  DateTime parsedDate = DateFormat('yyyy-MM-dd HH:mm').parse(dateString);
  print('Parsed date and time: $parsedDate');

  // Date arithmetic
  DateTime tomorrow = now.add(Duration(days: 1));
  print('Tomorrow: $tomorrow');

  DateTime yesterday = now.subtract(Duration(days: 1));
  print('Yesterday: $yesterday');

  // Duration
  Duration duration = Duration(days: 5, hours: 3, minutes: 30);
  print('Duration: $duration');
  
  // Interval between two dates
  DateTime futureDate = DateTime(2024, 12, 31);
  Duration difference = futureDate.difference(now);
  print('Days until future date: ${difference.inDays}');
}

Asynchronous Programming

Asynchronous programming in Dart allows you to execute non-blocking operations, which is crucial for handling tasks such as network requests, file I/O, and other operations that may take time to complete. Dart provides several features and mechanisms for asynchronous programming, including Futures and the async/await syntax


// Simulating a network request or a long-running operation
Future<String> fetchUserData() async {
  // Simulate a delay
  await Future.delayed(Duration(seconds: 2));
  // Return user data after the delay
  return 'User data retrieved successfully';
}

// Main function marked as async to use await inside it
Future<void> main() async {
  print('Fetching user data...');
  
  // Call fetchUserData() and wait for its completion
  String result = await fetchUserData();
  
  // Print the result once fetchUserData() completes
  print(result);
}

Explanation:

main() is marked with async keyword, indicating that it contains asynchronous operations.
Inside main(), we call fetchUserData(), which returns a Future<String>. We use await to asynchronously wait for this future to complete.
While waiting for fetchUserData() to complete, the execution of main() is paused. This allows other code to run in the meantime.
Once fetchUserData() completes, its result is assigned to result, and the execution of main() resumes.
We print the result obtained from fetchUserData().

Enums

Enums, short for enumerations, are a feature in many programming languages, including Dart. In Dart, enums are a special type used to represent a fixed number of constant values, typically related to a specific domain or set of options. Here's an overview of how enums work in Dart:



// Define an enum called Day
enum Day {
  monday,
  tuesday,
  wednesday,
  thursday,
  friday,
  saturday,
  sunday,
}

void main() {
  // Create a variable of type Day
  Day today = Day.monday;

  // Use a switch statement to perform actions based on the enum value
  switch (today) {
    case Day.monday:
      print('Start of the work week!');
      break;
    case Day.friday:
      print('Almost the weekend!');
      break;
    case Day.saturday:
    case Day.sunday:
      print('Weekend!');
      break;
    default:
      print('Midweek days.');
  }

  // Print all possible values of the enum
  print('All days of the week:');
  for (var day in Day.values) {
    print(day);
  }

  // Get the name of an enum value
  print('The name of the enum value is: ${today.name}');
}


Key Points:

enum Day creates a set of constants (e.g., monday, tuesday) that belong to the Day enum.
Usage: Use enum values to represent specific options or states in your code.
Switch Statement: Use switch to execute code based on the enum value.
Iteration: You can iterate over all enum values using Day.values.


String Manipulation in Dart

Importance:

String manipulation is essential for processing and formatting text data in programming, such as generating messages, formatting user input, or performing text-based calculations.

Common Operations:

Concatenation: Concatenation combines two or more strings into one. Dart uses the + operator for this.
void main() {
  String firstName = 'John';
  String lastName = 'Doe';

  // Concatenate two strings
  String fullName = firstName + ' ' + lastName;

  print('Full Name: $fullName'); // Output: Full Name: John Doe
}




Interpolation: String interpolation allows embedding variables directly within a string. Dart uses $ for simple variables and ${} for expressions.

void main() {
  String name = 'Alice';
  int age = 30;

  // String interpolation with a variable
  String greeting = 'Hello, $name!';

  // String interpolation with an expression
  String message = 'In 5 years, you will be ${age + 5} years old.';

  print(greeting); // Output: Hello, Alice!
  print(message);  // Output: In 5 years, you will be 35 years old.
}




Substring: The substring() method extracts a portion of a string by specifying start and end indices.

void main() {
  String text = 'Hello, Dart programming!';

  // Extract a substring from index 7 to 11
  String subText = text.substring(7, 11);

  print('Substring: $subText'); // Output: Substring: Dart
}

