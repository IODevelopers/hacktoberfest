 // An algorithm known as the Sieve of Erastosthenes can generate prime numbers. The  
// algorithm for this procedure is presented here. Write a program that implements  
// this algorithm. Have the program find all prime numbers up to n = 150. What can  
// you say about this algorithm as compared to the ones used in the text for   
// calculating prime numbers?  
//     Step 1: Define an array of integers P. Set all elements P(subscript i) to 0, 2 <= i <= n.   
//     Step 2: Set i to 2.  
//     Step 3: If i > n, the algorithm terminates.  
//     Step 4: If P(superscript i) is 0, i is prime.  
//     Step 5: For all positive integer values of j, such that i*j<=n, set P(subscript i*j) to 1.   
//     Step 6: Add 1 to i and go to step 3.  
  
//  main.m  
  
#import <Foundation/Foundation.h>  
  
int main (int argc, const char * argv[])
{  
    int i, j, n = 150, P[151] = { 0, 1 }, prime = 1;  
      
    for ( i = 2; i <= n; ++i ) {  
        P[i] = prime;  
        for ( j = 2; j < i ; ++j ) {  
            if ( i % j == 0 )  
                P[i] = 0;  
        }  
    }  
    printf("Print prime numbers results:\n\n");  
    for (i = 2; i <= n ; ++i) {  
        if ( P[i] != 0 )   
            printf("%i\n", i);  
    }  
      
    printf(" \n");  
    printf("Print prime numbers original program #results:\n\n");  
    //Original program referenced. 
    int p, d, isPrime;  
    for ( p = 2; p <= 150; ++p ) {   
        isPrime = 1;  
        for ( d = 2; d < p; ++d )   
            if ( p % d == 0 )  
                isPrime = 0;  
        if ( isPrime != 0 )   
            NSLog (@"%i ", p);  
    }  
    return 0;  
}  
