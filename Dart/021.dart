// Find the second-largest number in a list.

void main(){
  List<int> numbers = [3,2,7,45,8];

  int largest = numbers[0];
  int second_largest= numbers[0];

  for(int number in numbers){
     if (largest < number){
      second_largest = largest;
      largest = number;
     }

     else if(number < largest && number > second_largest){
      second_largest = number;
     }
  }
  print("The second largest value is : $second_largest");
}