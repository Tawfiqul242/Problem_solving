// Reverse a string without using the built-in reversed method.

void main(){
  String string = "Hello";
  String result = "";

  for(int i = 0; i < string.length; i++){
    result = string[i]+result;
  }

  print(result);
}