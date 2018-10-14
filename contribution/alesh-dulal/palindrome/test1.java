class LargestPalindromProduct {

   public static void main(String args[]) {
      LargestPalindromProduct obj = new LargestPalindromProduct();
      System.out.println("The largest palindrome for product of two 3-digit numbers is " + obj.getLargestPalindromeProduct(3));
   }
private int getLargestPalindromeProduct(int digits) {
   int largestPalindromeProduct = -1;
   int startNum = (int)Math.pow(10, digits) - 1;
   int endNum = (int)Math.pow(10, digits-1) - 1;

   for (int i = startNum; i > endNum; i--) {
       for (int j = startNum; j > endNum; j--) {
           if (isPalindrome(i * j)) {
               largestPalindromeProduct =  Math.max(largestPalindromeProduct, i * j);
           }
       }
   }
   return largestPalindromeProduct;
}

private boolean isPalindrome(int number) {
    String s = String.valueOf(number);
    for (int i = 0, j = s.length() -1; i < j;i++, j--) {
        if (s.charAt(i) != s.charAt(j)) {
            return false;
        }
    }
    return true;
}
}
