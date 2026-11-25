// Create a Car class with properties and methods such as start(), stop(), and displayInfo().

class Car {
  String? model = "car007";
  int? year = 123007;

  void start() {
    print("Car is starting.");
  }

  void stop() {
    print("Car is stopping");
  }

  void displayInfo() {
    print("Model: $model");
    print("Year: $year");
  }
}

void main() {
  Car car1 = Car();

  car1.start();
  car1.stop();
  car1.displayInfo();
}
