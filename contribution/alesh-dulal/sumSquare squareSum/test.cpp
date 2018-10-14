// C++ program to find the difference
// between sum of the squares of the
// first n natural numbers and square
// of sum of first n natural number
#include <bits/stdc++.h>
using namespace std;
 
int Square_Diff(int n){
 
int l, k, m;
 
    // Sum of the squares of the
    // first n natural numbers is
    l = (n * (n + 1) * (2 * n + 1)) / 6;
     
    // Sum of n naturals numbers
    k = (n * (n + 1)) / 2;
 
    // Square of k
    k = k * k;
     
    // Differences between l and k
    m = abs(l - k);
     
    return m;
 
}
 
// Driver Code
int main()
{
    int n = 10;
    cout << Square_Diff(n);
    return 0;
     
}
