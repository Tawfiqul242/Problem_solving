// Sort a list of numbers in ascending and descending order.

void main(){
    List<int> numbers = [5,3,6,1,2];
    
    numbers.sort();
    print("In ascending order: $numbers");

    print("In descending order: ${numbers.reversed.toList()}");
}