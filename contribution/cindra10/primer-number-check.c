#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int number)
{
    int i;
    for(i = 2; i <= sqrt(number); i++)
    {
        if(number % i == 0)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    int input;
    printf("Enter a number:");
    scanf("%d", &input);

    if(isPrime(input))
    {
        printf("Number %d is prime.\n", input);
    }
    else
    {
       printf("Number %d is not prime.\n", input);
    }

    return EXIT_SUCCESS;
}
