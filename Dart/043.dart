// Demonstrate inheritance using a Person and Student class.

class Person {
  String? name = "name 1";
  int? age = 15;
  int? id = 007;

  void displayInfo() {
    print("Name: $name");
    print("Age: $age");
    print("ID: $id");
  }
}

class Student extends Person {
  int? contact = 01223465;

  void display() {
    print("Contact: $contact");
  }
}

void main() {
  Student student1 = Student();

  student1.displayInfo();
  student1.display();
}
