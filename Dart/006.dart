// Find the largest among three numbers.


import 'dart:io';

void main(){
  List < int > values = stdin.readLineSync()!.split(' ').map((e) => int.parse(e)).toList();

  if (values[0] > values[1] && values[0] > values[2]){
    print("Largest Value is - ${values[0]}");
  }

  else if(values[1] > values[0] && values[1] > values[2]){
    print("Largest Value is - ${values[1]}");
  }

  else if(values[2] > values[0] && values[2] > values[1]){
    print("Largest Value is - ${values[2]}");
  }

  else{
    print("All values are same!");
  }
}