#include <stdio.h>
#include <math.h>
 
int main(){
    double x;
    int d,sum;
 
    x = pow(2,15);
 
    while (x>0){
        d = (int) fmod(x,10);
        sum = sum + d;
        x = x / 10;     
    }
    printf("%d\n",sum);
    return 0;
}

