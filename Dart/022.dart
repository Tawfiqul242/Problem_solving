// Create a map containing student names and their marks. Print each student's name and marks.

void main(){
  Map<String, double> result = {
    "First Student": 80,
    "Second Student": 85,
    "Third Studnet": 90
  };

  result.forEach(((key, value) => print("Key: $key\t $value")));
}