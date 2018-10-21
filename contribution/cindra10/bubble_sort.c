#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int *arr, int size)
{
    int i, j, t;
    for(i = 0; i < size - 1; i++)
    {
        for(j = i + 1; j < size; j++)
        {
            if(arr[i] > arr[j])
            {
                t = arr[i];
                arr[i] = arr[j];
                arr[j] = t;
            }
        }
    }
}

void print_array(int *arr, int size)
{
    int i;
    for(i = 0; i < size; i++)
    {
        printf("arr[%d]=%d\n", i, arr[i]);
    }
}
int main()
{
    int n,i;
    printf("Size of the array:");
    scanf("%d",&n);
    int *arr = malloc(sizeof(int) * n);
    printf("Insert integer values:\n");
    for(i = 0; i < n; i++)
    {
        printf("arr[%d]:",i);
        scanf("%d",&arr[i]);
    }
    printf("Unsorted array:\n");
    print_array(arr,n);
    bubble_sort(arr,n);
    printf("Sorted array:\n");
    print_array(arr,n);

    return EXIT_SUCCESS;
}
