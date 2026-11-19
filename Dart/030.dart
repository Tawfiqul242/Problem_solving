// Create an empty list of type string called days. Use the add method to add names of 7 days and print all days.


import 'dart:io';

void main() {
  double total = 0.0;

  List<double> expenses = [];

  print("Enter expenses separated by spaces:");

  expenses.addAll(
    stdin.readLineSync()!
        .split(" ")
        .map((e) => double.parse(e))
  );

  expenses.forEach((expense) => total += expense);

  print("Total Expense: $total");
}
