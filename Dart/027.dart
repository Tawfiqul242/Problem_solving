// Calculate the sum and average of all elements in a list.

void main(){
  List<int> numbers = [1,2,3,4,5];

  int sum = 0;
  numbers.forEach((number) => sum = sum+number);
  print("Sum of elements: $sum \nAverage of elements: ${sum~/numbers.length}");
}