// Count the number of words in a sentence.

void main() {
  String sentence = "Count the number of words in a sentence";

  int count = sentence.split(" ").length;

  print("Total Words: $count");
}
