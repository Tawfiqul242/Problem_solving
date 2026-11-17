// Remove duplicate elements from a list.

void main(){
  List<int> numbers = [1,3,3,2,5,4,4];

  List<int> unique = numbers.toSet().toList();

  print(unique);
}