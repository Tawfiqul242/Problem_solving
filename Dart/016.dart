// Count the digits of a number.

void main(){
  int number = 122345;
  int count = 0;
  while(number > 0){
    number = number~/10;
    count = count + 1;
  }
  print(count);
}