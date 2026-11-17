// Find the largest and smallest numbers in a list.

import 'dart:math';

void main(){
  List<int> numbers = [8,3,4,5,6,1];
  int largest = numbers.reduce(max);
  int smallest = numbers.reduce(min);

  print("Maximum Value $largest\nSmallest Value $smallest");
}



