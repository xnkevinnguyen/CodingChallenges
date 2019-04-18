class Solution {

  public void reverseString(char[] s) {
    for (int i = 0; i < s.length / 2; i++) {
      char temp = s[i];
      s[i] = s[s.length - i - 1];
      s[s.length - i - 1] = temp;
    }
  }

  public static void main(String[] args) {
    char[] sample = { 'h', 'e', 'l', 'o', 'l', 'o' };
    new Solution().reverseString(sample);
    System.out.println(sample);
  }
}
