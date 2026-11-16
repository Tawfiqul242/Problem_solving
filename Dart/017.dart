// Check whether a number is prime.

import 'dart:io';

void main(){
  int number = int.parse(stdin.readLineSync()!);
  var isPrime = true;

  if(number < 1){
    isPrime = false;
  }

  else{
    for(int i=2; i<number; i++){
    if (number%i==0){
      isPrime = false;
      break;
      }
    }
  }
  
  print(isPrime
        ? "$number is a prime number"
        : "$number is not a prime number"
    );
  }
