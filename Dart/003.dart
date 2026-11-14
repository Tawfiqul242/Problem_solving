// Swap two numbers without using a third variable.

import 'dart:io';

void main(){
  var value1 = int.parse(stdin.readLineSync()!);
  var value2 = int.parse(stdin.readLineSync()!);

  (value1, value2) = (value2, value1);

  print("Value 1: $value1 \nValue 2: $value2");
}
