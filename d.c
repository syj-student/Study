#include <stdio.h>

int	main(void)
{
	char x, y, z;
	printf("%c %c %c\n", x, y, z);
	scanf("%c", &x);
	scanf("%c", &y);
	scanf("%c", &z);
	printf("%c %c %c", x, y, z);
} 