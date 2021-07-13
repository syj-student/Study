#include <stdio.h>
#include <stdlib.h>

#define swap(type, x, y) do {type t = x; x = y; y = t; } while(0)

void	quick(int *a, int left, int right)
{
	int pl = left;
	int pr = right;
	int p = a[(pl + pr) / 2];
	do
	{
		while (a[pl] < p) pl++;
		while (a[pr] > p) pr--;
		if (pl <= pr)
		{
			swap(int, a[pl], a[pr]);
			pl++;
			pr--;
		}
	} while (pl <= pr);
	if (left < pr) quick(a, left, pr);
	if (pl < right) quick(a, pl, right);
}

int	main(void)
{
	int i, nx;
	int *x;

	scanf("%d", &nx);
	x = (int *)calloc(nx, sizeof(int));
	for (i = 0; i < nx; i++)
		scanf("%d", &x[i]);
	quick(x, 0, nx - 1);
	for (i = 0; i < nx; i++)
		printf("%d\n", x[i]);
	free(x);
	return 0;
}