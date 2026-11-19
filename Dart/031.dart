// Add your 7 friend names to the list. Use where to find a name that starts with alphabet K.

void main(){
  List<String> names = ["Rahim", "Karim", "Reheman", "Mir", "Sheikh", "Noor", "Ahmed"];

  var result = names.firstWhere((name) => name.startsWith("K"));

  print(result);
  }