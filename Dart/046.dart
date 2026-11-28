// Demonstrate encapsulation using private variables and getter/setter methods.

class Student {
  String? _name;
  int? _age;

  //Student(this.name, this.age);

  set name(String? name) {
    _name = name;
  }

  set age(int? age) {
    _age = age;
  }

  
  String get info => "Name is $_name and his age is $_age";

  }


void main() {
  Student stu = Student();

  stu.name = "Hasan";
  stu.age = 15;

  print(stu.info);
}
