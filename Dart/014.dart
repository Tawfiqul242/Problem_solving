// Find the factorial of a number.

import 'dart:io';

void main(){
  int n = int.parse(stdin.readLineSync()!);

  int product = 1;

  for (int i = 1; i<= n; i++){
    product = product*i;
  }
  print(product);
}