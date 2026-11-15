// Check whether a year is a leap year.

import 'dart:io';

void main(){
  int year = int.parse(stdin.readLineSync()!);

  if (year%4==0 && year%100 != 0){
    print("Leap Year");
  }

  else if (year%400==0){
    print("Leap Year");
  }

  else{
    print("Not Leap Year");
  }
}