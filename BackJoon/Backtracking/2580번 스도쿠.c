#include<stdio.h>
#include<stdlib.h>
int board[9][9];

void dfs(int n);
int check(int x, int y, int num);
void printboard();

int main() {

	int i, j;
	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			scanf("%d", &board[i][j]);
		}
	}

	dfs(0);
}

void dfs(int n) {
	int row = n / 9;
	int col = n % 9;
	if (n == 81) {
		printboard();
		exit(0);
	}
	else if (board[row][col] != 0) dfs(n + 1);
	else {
		
		int i, j;
		
		for (i = 1; i <= 9; i++) {
			if (check(row, col, i)) {
				board[row][col] = i;
				dfs(n + 1);
				board[row][col] = 0;
			}
		}

	}
}
int check(int x, int y, int num) {
	int i, j;
	int sq_x = (x / 3) * 3;
	int sq_y = (y / 3) * 3;

	for (i = 0; i < 9; i++) {
		
		if (board[x][i] == num) return 0;
	}
		
	for (i = 0; i < 9; i++) {
		
		if (board[i][y] == num) return 0;
	}

	for (i = sq_x; i < sq_x + 3; i++) {
		for (j = sq_y; j < sq_y + 3; j++) {

			if (board[i][j] == num) return 0;
		}
	}
	return 1;
}

void printboard(){
	int i, j;
	printf("\n");
	for (i = 0; i < 9; i++) {
		for (j = 0; j < 9; j++) {
			printf("%d ", board[i][j]);
		}
		printf("\n");
	}
}