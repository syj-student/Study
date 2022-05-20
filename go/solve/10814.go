package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

type PersonalInfo struct {
	age  int
	name string
	idx  int
}

type PersonalInfoHeap []PersonalInfo

func (h PersonalInfoHeap) Len() int { return len(h) }
func (h PersonalInfoHeap) Less(a, b int) bool {
	if h[a].age == h[b].age {
		return h[a].idx < h[b].idx
	} else {
		return h[a].age < h[b].age
	}
}
func (h PersonalInfoHeap) Swap(a, b int) {
	h[a], h[b] = h[b], h[a]
}
func (h *PersonalInfoHeap) Push(x any) {
	*h = append(*h, x.(PersonalInfo))
}
func (h *PersonalInfoHeap) Pop() any {
	last := len(*h) - 1
	ret := (*h)[last]
	*h = (*h)[:last]
	return ret
}

var (
	r = bufio.NewReader(os.Stdin)
)

func main() {
	h := &PersonalInfoHeap{}
	heap.Init(h)
	n := 0
	age, name := 0, ""
	fmt.Fscan(r, &n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &age, &name)
		heap.Push(h, PersonalInfo{age, name, i})
	}
	for h.Len() > 0 {
		t := heap.Pop(h).(PersonalInfo)
		fmt.Println(t.age, t.name)
	}
}
