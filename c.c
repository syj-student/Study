#include <stdio.h>

int	map[9][9], checker[10];

void	CheckerReset(int *lst, int len)
{
	for (int i = 0; i < len; i++)
		lst[i] = 0;
}

void	RowCheck(void)
{
	int num;

	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			(checker[map[i][j]])++;
			if (map[i][j] == 0)
				num = j;
		}
		if (checker[0] == 1)
		{
			for (int k = 1; k < 10; k++)
				if (checker[k] == 0)
				{
					map[i][num] = k;
					break;
				}
		}
		CheckerReset(checker, 10);
	}
}

void	ColCheck(void)
{
	int num;

	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			(checker[map[j][i]])++;
			if (map[j][i] == 0)
				num = j;
		}
		if (checker[0] == 1)
		{
			for (int k = 1; k < 10; k++)
				if (checker[k] == 0)
				{
					map[num][i] = k;
					break;
				}
		}
		CheckerReset(checker, 10);
	}
}

void	ZoneCheckSub(int Xstart, int Xend, int Ystart, int Yend)
{
	int num[2];

	for (int i = Xstart; i < Xend; i++)
	{
		for (int j = Ystart; j < Yend; j++)
		{
			(checker[map[i][j]])++;
			if (map[i][j] == 0)
			{
				num[0] = i;
				num[1] = j;
			}
		}
	}
	if (checker[0] == 1)
	{
		for (int k = 1; k < 10; k++)
			if (checker[k] == 0)
			{
				map[num[0]][num[1]] = k;
				break;
			}
	}
	CheckerReset(checker, 10);
}

void	ZoneCheck(void)
{
	for (int i = 0; i < 9; i += 3)
		for (int j = 0; j < 9; j +=3)
			ZoneCheckSub(i, i + 3, j, j +3);
}

void	ExecCheck(void)
{
	RowCheck();
	ColCheck();
	ZoneCheck();
}

int		main(void)
{
	// input
	for (int i = 0; i < 9; i++)
		scanf("%d %d %d %d %d %d %d %d %d", 
			&map[i][0], &map[i][1], &map[i][2],
			&map[i][3], &map[i][4], &map[i][5],
			&map[i][6], &map[i][7], &map[i][8]);

	// solve
	ExecCheck();
	ExecCheck();

	// print
	for (int i = 0; i < 9; i++)
		printf("%d %d %d %d %d %d %d %d %d\n", 
			map[i][0], map[i][1], map[i][2],
			map[i][3], map[i][4], map[i][5],
			map[i][6], map[i][7], map[i][8]);
}