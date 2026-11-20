// Count how many times each element appears in a list.

void main(){
  List<int> numbers = [1,2,3,3,4,5,5];

  Map<int, int> duplicate = {};

  for(int number in numbers){
    if(!duplicate.containsKey(number)){
      duplicate[number] = 1;
    }

    else{
      duplicate[number] = duplicate[number]!+1;
    }
  }

  duplicate.forEach(((key, value) => print("$key : $value")));

}