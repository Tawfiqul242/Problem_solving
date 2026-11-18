// Create a list of numbers and separate even and odd numbers into two different lists.

void main(){
  List<int> numbers = [1,2,4,3,5,6,7,8,9,10];
  List<int> even = [];
  List<int> odd = [];

  for(int i = 0; i < numbers.length; i++){
    if(numbers[i] % 2 == 0){
      even.add(numbers[i]);
    }
    else{
      odd.add(numbers[i]);
    }
  }
print(even);
print(odd);
}