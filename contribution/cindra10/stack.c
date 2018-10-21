#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node
{
    int data;
    struct Node *previous;
}Node;

typedef struct
{
    Node *top;
}Stack;

Node* getNode()
{
    Node *node = (Node*)malloc(sizeof(Node));
    node->previous = NULL;
    return node;
}

void Push(Stack *s, int data)
{
    if(s != NULL)
    {
        Node *node = getNode();
        node->data = data;
        node->previous = s->top;
        s->top = node;
    }
    else
    {
        printf("Stack is not initialized properly.\n");
    }
}

int Pop(Stack *s)
{
    if(s != NULL)
    {
        if(s->top != NULL)
        {
            int data = s->top->data;
            Node *previous = s->top->previous;
            free(s->top);
            s->top = previous;
            return data;
        }
        else
        {
            printf("Stack has no data in it.\n");
        }
    }
    else
    {
        printf("Stack is not initialized properly.\n");
    }

    return -1;
}

Stack* initializeStack()
{
    Stack *stack = (Stack*)malloc(sizeof(Stack));
    stack->top = NULL;
    return stack;
}

void menu(Stack *s)
{
    clearScreen();
    printf("---------MENU---------\n");
    if(s == NULL)
    {
        printf("1. Initialize stack\n");
        printf("2. Exit\n");
    }
    else if(s->top == NULL)
    {
        printf("1. Push data to stack\n");
        printf("2. Delete stack\n");
        printf("3. Exit\n");
    }
    else
    {
        printf("1. Push data to stack\n");
        printf("2. Pop data from stack\n");
        printf("3. Delete stack\n");
        printf("4. Exit\n");
    }
    printf("Your choice:");
}

void deleteStack(Stack **s)
{
    if(*s != NULL)
    {
        while((*s)->top != NULL)
        {
            Node *temp = (*s)->top->previous;
            free((*s)->top);
            (*s)->top = temp;
        }
        free(s);
        *s = NULL;
    }
}

void clearScreen()
{
    system("cls");
}

void pauseExecution()
{
    system("pause");
}

void close()
{
    exit(EXIT_SUCCESS);
}

int main()
{
    Stack *s = NULL;
    int choice, data;
    while(true)
    {
        menu(s);
        scanf("%d", &choice);
        switch(choice)
        {
            case 1:
                if(s == NULL)
                {
                    s = initializeStack(s);
                }
                else
                {
                    printf("Enter data you want to be pushed to stack:");
                    scanf("%d", &data);
                    Push(s,data);
                }
                break;
            case 2:
                if(s == NULL)
                {
                    close();
                }
                else if(s->top == NULL)
                {
                    deleteStack(&s);
                }
                else
                {
                    data = Pop(s);
                    if(data != -1)
                    {
                        printf("Popped data:%d\n", data);
                    }
                }
                break;
            case 3:
                if(s == NULL)
                {
                    printf("Incorrect option, please try again.\n");
                }
                else if(s->top == NULL)
                {
                    close();
                }
                else
                {
                    deleteStack(&s);
                }
                break;
            case 4:
                if(s == NULL)
                {
                    printf("Incorrect option, please try again.\n");
                }
                else if(s->top == NULL)
                {
                    printf("Incorrect option, please try again.\n");
                }
                else
                {
                    close();
                }
                break;
            default:
                printf("Incorrect option, please try again.\n");
                break;
        }
        pauseExecution();
    }
    return EXIT_SUCCESS;
}
