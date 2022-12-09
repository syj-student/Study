package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"sort"
	"time"
)

var r *bufio.Reader

func main() {
	var a, b, c, x, y int
	r = bufio.NewReader(os.Stdin)
	rand.Seed(time.Now().UnixNano())
	fmt.Fscan(r, &x, &y)
	fmt.Println(x, y)
	lst := make([][3]int, y)

	for i := 0; i < y; i++ {
		fmt.Fscan(r, &a, &b, &c)
		lst[i][0] = c
		lst[i][1] = a
		lst[i][2] = b
	}
	sort.Slice(lst, func(i, j int) bool {
		switch {
		case lst[i][0] < lst[j][0]:
			return true
		case lst[i][0] == lst[j][0]:
			switch {
			case lst[i][1] > lst[j][1]:
				return true
			default:
				return false
			}
		default:
			return false
		}
	})
	answer := 0
	var aaa interface{}
	connections := map[int]interface{}{}
	connections[lst[0][1]] = aaa
	for {
		if len(connections) == x {
			break
		}
		for _, el := range lst {
			_, one := connections[el[1]]
			_, two := connections[el[2]]
			if one && two {
				continue
			}
			if one || two {
				connections[el[1]] = aaa
				connections[el[2]] = aaa
				answer += el[0]
				break
			}
		}
	}
	fmt.Println(answer)
}
