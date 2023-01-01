package main

import (
	"bufio"
	"fmt"
	"os"
	"sync"
)

type Answer struct {
	val   int
	mutex *sync.Mutex
}

var (
	N, M, G, R   int
	originGarden [][]int
	waterPos     [][2]int
	dx           = [4]int{0, -1, 0, 1}
	dy           = [4]int{-1, 0, 1, 0}
	answer       = Answer{
		val:   0,
		mutex: &sync.Mutex{},
	}
)

func main() {
	parseInformation()
	fmt.Println("option", waterPos)
	cases := generator(G + R)
	for v := range cases {
		fmt.Println(v)
	}
}

func generator(cnt int) <-chan []int {
	channel := make(chan []int, 100)
	tmp := make([]int, cnt)
	var dfs func(now *[]int, start, depth int)
	dfs = func(now *[]int, start, depth int) {
		if depth == cnt {
			nowCopy := make([]int, len(*now))
			copy(nowCopy, *now)
			channel <- nowCopy
			return
		}
		for i := start; i < len(waterPos); i++ {
			(*now)[depth] = i
			dfs(now, i+1, depth+1)
		}
		if depth == 0 {
			close(channel)
		}
	}
	go dfs(&tmp, 0, 0)
	return channel
}

func bLogic() {

}

func parseInformation() {
	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &N, &M, &G, &R)
	if R < G {
		G, R = R, G
	}
	originGarden = make([][]int, N)
	for i := 0; i < N; i++ {
		originGarden[i] = make([]int, M)
	}
	for y := 0; y < N; y++ {
		for x := 0; x < M; x++ {
			fmt.Fscan(r, &originGarden[y][x])
			if originGarden[y][x] == 2 {
				waterPos = append(waterPos, [2]int{x, y})
				originGarden[y][x] = 1
			}
		}
	}
}
