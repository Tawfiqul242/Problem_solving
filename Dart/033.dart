// Create a map with name, phone keys and store some values to it. Use where to find all keys that have length 4.

void main(){
  Map<String, dynamic> address ={
    "name": "kari",
    "phone": 0123456789
  };

  var reuslt = address.keys.where((key) => key.length == 4);

  print(reuslt);
}