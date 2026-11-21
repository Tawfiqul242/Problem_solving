// Check whether a string is a palindrome.

void main() {
  String string = "madam";
  String reverse = "";

  for (int i = 0; i < string.length; i++) {
    reverse = string[i] + reverse;
  }

  if (string == reverse) {
    print("This string is a palindrome");
  } else {
    print("This string is not a palindrome");
  }
}
