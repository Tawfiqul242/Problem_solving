// Calculate the sum of numbers from 1 to N.

import 'dart:io';

void main(){
  int N = int.parse(stdin.readLineSync()!);

  int sum = 0;
  for(int i=1; i<=N; i++){
    sum = sum + i;
  }

  print(sum);
}