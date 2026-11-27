// Create an abstract class called Shape with an abstract method calculateArea().

abstract class Shape {
  int? wide = 10;
  int? length = 15;

  void calculateArea();
}

class Area1 extends Shape {
  @override
  void calculateArea() {
    print(super.wide! * super.length!);
  }
}

void main() {
  Area1 area = Area1();

  area.calculateArea();
}
