#include <stdio.h>

int g_a[15];

int main()
{
	int a[15];
	for (int i = 0; i < 15; i++)
		printf("%d\n", g_a[i]);
}