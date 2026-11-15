// Reverse a number. Example: 1234 → 4321.

import 'dart:io';

void main(){
  int number = 1234;
  while(true){
    var result = number % 10;
    number = number ~/ 10;

    stdout.write("$result");
    if (number < 1){
      break;
    }
  }
}
