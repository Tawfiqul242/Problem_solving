// Create a  map with name, address, age, country keys and store values to it. Update country name to other country and print all keys and values.

void main(){
  
  Map <String, dynamic> dictionary = {
      'name': "Ramim",
      "address": "Dhaka",
      "age": 100,
      "country": "Bangladesh"
  };

  dictionary["country"] = "Germany";

  dictionary.forEach(((key, value) => print("Key: $key\t Value: $value")));
}