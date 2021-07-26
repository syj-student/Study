#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define cnt 500000

void	CountingSort(int *lst)
{
	// counting
	static int lstmax[cnt];
	for (int i = 0; i < cnt; i++)
		(lstmax[lst[i]])++;
	for (int i = 1; i < cnt; i++)
		lstmax[i] = lstmax[i] + lstmax[i - 1];
	
	// sorting
	int ret[cnt];
	for (int i = 0; i < cnt; i++)
	{
		ret[lstmax[lst[i]] - 1] = lst[i];
		(lstmax[lst[i]])--;
	}
	for (int i = 0; i < cnt; i++)
		lst[i] = ret[i];
}

int	main(void)
{
	// make random
	int random[cnt];
	srand(time(NULL));
	for (int i = 0; i < cnt; i++)
		random[i] = rand() % cnt;

	// sorting
	CountingSort(random);

	// print
	for (int i = 0; i < cnt; i++)
		printf("%d ", random[i]);
	printf("\n");
	return 0;
}