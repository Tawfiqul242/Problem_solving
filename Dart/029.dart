// Create a program thats reads list of expenses amount using user input and print total.

import 'dart:io';

void main(){
  
  var total = 0.0;

  List<double> expenses = [];
  expenses.addAll(stdin.readLineSync()!
                        .split(" ")
                        .map((e) => double.parse(e))
                        );
  
  expenses.forEach((expense) => total += expense);

  print("Total Expense: $total");
}