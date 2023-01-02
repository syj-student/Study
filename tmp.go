package main

import "fmt"

func change(l [][][2]int) {
	l[0][0][0] = 10
}

func main() {
	a := [][][2]int{{{1, 2}}}
	fmt.Println(a)
	change(a)
	fmt.Println(a)
}
