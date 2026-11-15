// Create a simple calculator using switch (addition, subtraction, multiplication and division).

import 'dart:io';

void main(){
  print("Enter two value");
  int val1 = int.parse(stdin.readLineSync()!);
  int val2 = int .parse(stdin.readLineSync()!);

  print("Choose operator for calculation (+, -, *, /)");
  String operator = stdin.readLineSync()!;

  switch(operator){
    case "+":
      var res = val1+val2;
      print("Addition of $val1 and $val2 is $res");
      break;

    case "-":
      var res = val1-val2;
      print("Subtraction form $val1 to $val2 is $res");
      break;

    case "*":
      print("Multiplication of $val1 and $val2 is ${val1*val2}");
      break;

    case "/":
      print("Division of $val1 and $val2 is ${val1/val2}");
      break;

    default:
      print("Invalid Operator!");
  }
}
