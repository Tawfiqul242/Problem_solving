// Check whether a person is eligible to vote (age 18 or above).

import 'dart:io';

void main(){
  int age = int.parse(stdin.readLineSync()!);

  if (age >= 18){
    print("The person is eligible to vote.");
  }

  else{
    print("The person is not eligible to vote.");
  }
}



