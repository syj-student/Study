package main

import (
	"bufio"
	"fmt"
	"os"
)

type info struct {
	x      int
	y      int
	answer int
	table  [][]int
	base   [][]int
	cases  [][2]int
}

func main() {
	s := info{}
	s.init()
	s.solveProblem(3)
	fmt.Println(s.answer)
}

func (s *info) init() {
	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &s.x, &s.y)
	s.answer = 0
	s.table = make([][]int, s.x)
	s.base = make([][]int, s.x)
	for i := 0; i < s.x; i++ {
		s.table[i] = make([]int, s.y)
		for j := 0; j < s.y; j++ {
			fmt.Fscan(r, &s.table[i][j])
		}
		s.base[i] = make([]int, s.y)
		copy(s.base[i], s.table[i])
	}
}

func (s *info) resetTable() {
	for i := 0; i < s.x; i++ {
		copy(s.table[i], s.base[i])
	}
}

func (s *info) countSafeZone() {
	ret := 0
	for i := 0; i < s.x; i++ {
		for j := 0; j < s.y; j++ {
			if s.table[i][j] == 0 {
				ret++
			}
		}
	}
	if s.answer < ret {
		s.answer = ret
	}
}

func (s *info) combinations(n int) [][][2]int {
	ret := [][][2]int{}
	rec := func(lst [][2]int, dep, l int) {}
	rec = func(lst [][2]int, dep, l int) {
		if dep == n {
			tmp := make([][2]int, n)
			copy(tmp, lst)
			ret = append(ret, tmp)
			return
		}
		for i := l; i < len(s.cases); i++ {
			lst[dep] = s.cases[i]
			rec(lst, dep+1, i+1)
		}
	}
	rec(make([][2]int, n), 0, 0)
	return ret
}

func (s *info) makeCases() {
	for i := 0; i < s.x; i++ {
		for j := 0; j < s.y; j++ {
			if s.table[i][j] == 0 {
				s.cases = append(s.cases, [2]int{i, j})
			}
		}
	}
}

func (s *info) bfs(i, j int) {
	stack := [][2]int{{i, j}}
	s.table[i][j] = -1
	dx := [4]int{0, 0, -1, 1}
	dy := [4]int{-1, 1, 0, 0}
	for len(stack) != 0 {
		now := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for i := 0; i < 4; i++ {
			nx := dx[i] + now[0]
			ny := dy[i] + now[1]
			if (0 <= nx && nx < s.x) &&
				(0 <= ny && ny < s.y) &&
				(s.table[nx][ny] == 0) {
				s.table[nx][ny] = -1
				stack = append(stack, [2]int{nx, ny})
			}
		}
	}
}

func (s *info) solveProblem(n int) {
	s.makeCases()
	wall := s.combinations(n)
	for _, k := range wall {
		s.resetTable()
		for _, w := range k {
			s.table[w[0]][w[1]] = 9999
		}
		for i := 0; i < s.x; i++ {
			for j := 0; j < s.y; j++ {
				if s.table[i][j] == 2 {
					s.bfs(i, j)
				}
			}
		}
		s.countSafeZone()
	}
}
