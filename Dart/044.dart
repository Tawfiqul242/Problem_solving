// Demonstrate method overriding using a parent and child class.

abstract class Parent {
  void display() {}
}

class Child extends Parent {
  void display() {
    print("This is child class");
  }
}

void main() {
  Child c1 = Child();

  c1.display();
}
