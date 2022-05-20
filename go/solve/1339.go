package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

func input(r *bufio.Reader) string {
	var ret string
	fmt.Fscan(r, &ret)
	return ret
}

func main() {
	var n int
	m := map[rune]float64{}

	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &n)
	for i := 0; i < n; i++ {
		n := input(r)
		for i, rn := range n {
			m[rn] += math.Pow10(len(n) - i - 1)
		}
	}
	lst := make([]float64, len(m))
	j := 0
	for _, k := range m {
		lst[j] = k
		j++
	}
	acc := 0
	sort.Float64s(lst)
	for i, num := len(lst)-1, 9; i >= 0; i, num = i-1, num-1 {
		acc += num * int(lst[i])
	}
	fmt.Println(acc)
}
