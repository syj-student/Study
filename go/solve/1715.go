package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) { *h = append(*h, x.(int)) }

func (h *IntHeap) Pop() any {
	last := len(*h) - 1
	ret := (*h)[last]
	*h = (*h)[:last]
	return ret
}

func main() {
	var n, x int
	var h IntHeap

	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &n)
	heap.Init(&h)
	for n != 0 {
		fmt.Fscan(r, &x)
		heap.Push(&h, x)
		n--
	}
	if len(h) == 1 {
		fmt.Println(0)
	} else {
		acc := 0
		for len(h) != 1 {
			a := heap.Pop(&h).(int)
			b := heap.Pop(&h).(int)
			heap.Push(&h, a+b)
			acc += a + b
		}
		fmt.Println(acc)
	}
}
