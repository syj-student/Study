package main

import (
	"bufio"
	"fmt"
	"os"
)

func max(num int, nums ...int) int {
	if nums == nil {
		return num
	}
	ret := num
	for _, k := range nums {
		if ret < k {
			ret = k
		}
	}
	return ret
}

func main() {
	r := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(r, &n)
	n++
	table := make([]int, n)
	dp := make([]int, n)
	for i := 1; i < n; i++ {
		fmt.Fscan(r, &table[i])
	}
	dp[1] = table[1]
	if n-1 > 1 {
		dp[2] = table[1] + table[2]
	}
	for i := 3; i < n; i++ {
		dp[i] = max(dp[i-1], dp[i-3]+table[i-1]+table[i], dp[i-2]+table[i])
	}
	fmt.Println(dp[n-1])
}
