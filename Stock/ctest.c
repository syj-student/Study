#include <stdio.h>
#include <stdlib.h>

int main()
{
    int memsize, answersize;
    int *lst, *answerlst;

    scanf("%d", &memsize);
    lst = malloc(sizeof(int) * memsize);
    for (int i = 0; i < memsize; i++)
    {
        scanf("%d", &lst[i]);
    }
}