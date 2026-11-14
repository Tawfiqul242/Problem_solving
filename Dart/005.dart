// Write a program to check whether a number is even or odd.

import 'dart:io';

void main(){
  int value = int.parse(stdin.readLineSync()!);

  // if (value % 2 == 0){
  //   print("The given number is even");
  // }

  // else{
  //   print("The given number is odd");
  // }

  value % 2 == 0? print("The given number is even") : print("The given number is odd");

}
