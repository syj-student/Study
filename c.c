#include <stdio.h>

int g_table[20][20];
int	g_team[20];

void	teamreset(int n)
{
	for (int i = 0; i < n; i++)
		g_team[i] = 0;
}

int		teamscore()
{

}

void	dfs()
{

}

int		main()
{
	int num;

	scanf("%d", &num);
	for (int i = 0; i < num; i++)
		for (int j = 0; j < num; j++)
			scanf("%d", g_table[i][j]);
	
}