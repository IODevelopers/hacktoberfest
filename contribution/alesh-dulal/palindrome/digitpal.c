#include <stdio.h>
// Project Euler: Problem 4
// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99.
// Find the largest palindrome made from the product of two 3-digit numbers.

int isPalindrome(unsigned long orig);

int main(void) {
  unsigned int n, m, max = 0;
  
  for (n = 100; n <= 999; n++) {
    for (m = 100; m <= 999; m++) {
      unsigned int p = n*m;
      if(isPalindrome(p) && p > max) {
        max = p;
      }
    }
  }

  printf("Largest palindrome is: %d\n", max);  

  return 0;
}

int isPalindrome(unsigned long orig) {
  unsigned long reversed = 0, n = orig;

  while (n > 0) {
    reversed = reversed * 10 + n % 10;
    n /= 10;
  }

  return orig == reversed;
}
