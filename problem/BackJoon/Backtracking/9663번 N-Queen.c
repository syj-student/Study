#include <stdio.h>

int g_answer[15];
int g_check[15];

int	check(int depth)
{
	for (int i = 0; i < depth; i++)
		if (g_answer[i] - g_answer[depth] == depth - i || g_answer[depth] - g_answer[i] == depth - i)
			return 0;
	return 1;
}

void	dfs(int n,int depth, int *ret)
{
	if (depth == n)
	{
		(*ret)++;
		return ;
	}
	for (int i = 0; i < n ;i++)
	{
		if (!(g_check[i]))
		{
			g_check[i] = 1;
			g_answer[depth] = i;
			if (check(depth))
				dfs(n, depth + 1, ret);
			g_check[i] = 0;
		}
	}
}

int	main(void)
{
	int n;
	int ret = 0;

	scanf("%d", &n);
	dfs(n, 0, &ret);
	printf("%d", ret);
	return 0;
}