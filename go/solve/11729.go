package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func hanoi(n, a, b int) {
	if n > 1 {
		hanoi(n-1, a, 6-a-b)
	}
	fmt.Fprintln(w, a, b)
	if n > 1 {
		hanoi(n-1, 6-a-b, b)
	}
}

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()
	n := 0
	fmt.Fscanln(r, &n)
	fmt.Fprintln(w, math.Pow(2, float64(n))-1)
	hanoi(n, 1, 3)
}
