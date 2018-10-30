#include <stdio.h>
#include <stdlib.h>

void printMatrix(int **array, int row, int column);

int main(int argc, char const *argv[])
{
    int i, j;
    int **matrix;
    int row, column;
    int row_sum = 0, col_sum = 0, diagonal_sum1 = 0, diagonal_sum2 = 0;

    printf("Row size?: ");
    scanf("%d",&row);

    printf("Column size?: ");
    scanf("%d",&column);

    // Check if it's a square
    if (row != column) {
        fprintf(stderr, "Error: Not a square. Row size does not equal to column size.\n");
        return -1;
    }

    // Allocate 2D array
    matrix = malloc(row * sizeof(int*));

    for(i = 0; i < row; i++)
        matrix[i] = malloc(column * sizeof(int*));

    // Get the matrix from user
    printf("Enter the elements of your matrix:\n");
    for(i = 0; i < row; i++)
    {
        printf("%d. row:\n",i+1);
        for(j = 0; j < column; j++)
        {
            printf("[%d][%d]: ",i,j);
            scanf("%d",&matrix[i][j]);
        }
        printf("\n");
    }

    // Check diagonals
    for(i = 0; i < row; i++)
    {
        diagonal_sum1 += matrix[i][i];
        diagonal_sum2 += matrix[i][row - i - 1];
    }

    // If diagonals does not equal, terminate
    if (diagonal_sum1 != diagonal_sum2) {
        printMatrix(matrix, row, column);
        printf("\nThis is not a magic square!\n");
        return 0;
    }

    // Check rows
    for(i = 0; i < row; i++)
    {
        for(j = 0; j < column; j++)
        {
            row_sum += matrix[i][j];
        }

        if(row_sum != diagonal_sum1)
        {
            printMatrix(matrix, row, column);
            printf("\nThis is not a magic square!\n");
            return 0;
        }

        row_sum = 0;
    }

    // Check columns
    for(i = 0; i < row; i++)
    {
        for(j = 0; j < column; j++)
        {
            col_sum += matrix[j][i];
        }

        if(col_sum != diagonal_sum1)
        {
            printMatrix(matrix, row, column);
            printf("\nThis is not a magic square!\n");
            return 0;
        }

        col_sum = 0;
    }

    printMatrix(matrix, row, column);
    printf("\nThis is a magic square!\n");

    return 0;
}

void printMatrix(int **array, int row, int column)
{
    int i,j;

    for(i = 0; i < row; i++)
    {
        for(j = 0; j < column; j++)
        {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
}
