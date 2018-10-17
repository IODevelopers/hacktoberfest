#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPalindrome(char *word, int size)
{
    int i;
    for(i = 0; i < size; i++)
    {
        if(word[i] != word[size - i - 1])
        {
            return false;
        }
    }

    return true;
}

int main()
{
    int size;
    printf("Enter the word length:");
    scanf("%d", &size);
    char *word = (char*)malloc(sizeof(char) * (size + 1)); //allocate size + 1 for \0
    printf("Enter the word:");
    scanf("%s", word);

    if(isPalindrome(word, size))
    {
        printf("Word is palindrome.");
    }
    else
    {
        printf("Word is not palindrome.");
    }
    return EXIT_SUCCESS;
}
