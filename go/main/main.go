package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
	"strings"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	var x int
	var s string
	fmt.Fscan(r, &x)
	for i := 0; i < x; i++ {
		left := list.New()
		right := list.New()
		fmt.Fscan(r, &s)
		s = strings.Trim(s, "\n")
		now := lst.Front()
		for _, c := range s {
			if c == '<' {
				if now != nil && now.Prev() != nil {
					now = now.Prev()
				}
			} else if now != nil && c == '>' {
				if now.Next() != nil {
					now = now.Next()
				}
			} else if now != nil && c == '-' {
				if now.Next() != nil {
					now = now.Next()
				}
			} else if now != nil {
				el := list.Element{
					Value: c,
				}
				n := now.Next()
				now.Next = el
				n.Prev = el
			} else {
				now := list.Element{
					Value: c,
				}
				lst.PushBack(now)
			}
		}
	}
}
