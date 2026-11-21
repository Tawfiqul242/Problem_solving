// Count vowels and consonants in a string.

void main() {
  String string = "abcdefu";

  List<String> vowels = ["a", "e", "i", "o", "u"];
  int v_count = 0;

  for (int i = 0; i < string.length; i++) {
    if (vowels.contains(string[i].toLowerCase())) {
      v_count += 1;
    }
  }
  print(
    "Total Vowel Count: $v_count\nTotal Consonant Count: ${string.length - v_count}",
  );
}
