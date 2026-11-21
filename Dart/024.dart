// Find the common elements between two lists.

void main(){
    List<int> num1 = [1,2,3,4,5];
    List<int> num2 = [4,5,6,7,8,];

    List<int> result = num1.toSet().intersection(num2.toSet()).toList();

    print(result);
}