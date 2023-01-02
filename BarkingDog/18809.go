package main

import (
	"bufio"
	"fmt"
	"os"
	"sync"
)

type void interface{}

type Answer struct {
	val   int
	mutex *sync.Mutex
}

type Ele struct {
	x, y  int
	color rune
	days  int
}

var (
	N, M, G, R   int
	originGarden [][][2]int
	waterPos     [][2]int
	Nothing      void
	dx           = [4]int{0, -1, 0, 1}
	dy           = [4]int{-1, 0, 1, 0}
	answer       = Answer{
		val:   0,
		mutex: &sync.Mutex{},
	}
	wg = sync.WaitGroup{}
)

func main() {
	wg.Add(1)
	parseInformation()
	all_cases := generator(len(waterPos), G+R)
	for all := range all_cases {
		green_cases := generator(G+R, G)
		for green := range green_cases {
			allCopy := make([]int, len(*all))
			copy(allCopy, *all)
			greenCopy := make([]int, len(*green))
			copy(greenCopy, *green)
			go bLogic(allCopy, greenCopy, deepcopy(originGarden))
		}
	}
	wg.Done()
	wg.Wait()
	fmt.Println(answer.val)
}

func deepcopy(origin [][][2]int) [][][2]int {
	ret := [][][2]int{}
	for i := 0; i < len(origin); i++ {
		iLine := make([][2]int, len(origin[0]))
		ret = append(ret, iLine)
		for j := 0; j < len(origin[0]); j++ {
			iLine[j][0] = origin[i][j][0]
			iLine[j][1] = origin[i][j][1]
		}
	}
	return ret
}

func generator(part int, cnt int) <-chan *[]int {
	channel := make(chan *[]int)
	tmp := make([]int, cnt)
	var dfs func(now *[]int, start, depth int)
	dfs = func(now *[]int, start, depth int) {
		if depth == cnt {
			nowCopy := make([]int, len(*now))
			copy(nowCopy, *now)
			channel <- &nowCopy
			return
		}
		for i := start; i < part; i++ {
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

func bLogic(all_pos []int, green_pos []int, board [][][2]int) {
	wg.Add(1)
	q := map[Ele]void{}
	// fmt.Println(all_pos, green_pos, waterPos)
	// fmt.Println(v, all_pos[v], len(waterPos))
	for _, v := range green_pos {
		p := waterPos[all_pos[v]]
		board[p[0]][p[1]][0] = int('G')
		q[Ele{
			x:     p[0],
			y:     p[1],
			color: 'G',
			days:  0,
		}] = Nothing
		all_pos[v] = -1
	}
	for _, v := range all_pos {
		if v == -1 {
			continue
		}
		p := waterPos[v]
		board[p[0]][p[1]][0] = int('R')
		q[Ele{
			x:     p[0],
			y:     p[1],
			color: 'R',
			days:  0,
		}] = Nothing
	}
	now_answer := 0
	for len(q) > 0 {
		tmp := map[Ele]void{}
		for k := range q {
			now_day := k.days + 1
			for i := 0; i < 4; i++ {
				nx := dx[i] + k.x
				ny := dy[i] + k.y
				if 0 <= nx && nx < len(board) && 0 <= ny && ny < len(board[0]) && board[nx][ny][0] != 0 {
					if board[nx][ny][0] == 1 || board[nx][ny][0] == 2 {
						board[nx][ny][0] = int(k.color)
						board[nx][ny][1] = now_day
						tmp[Ele{
							x:     nx,
							y:     ny,
							color: k.color,
							days:  now_day,
						}] = Nothing
					} else if board[nx][ny][1] == now_day {
						if board[nx][ny][0] == int('G') && k.color == 'R' {
							delete(tmp, Ele{
								x:     nx,
								y:     ny,
								color: 'R',
								days:  now_day,
							})
							delete(tmp, Ele{
								x:     nx,
								y:     ny,
								color: 'G',
								days:  now_day,
							})
							now_answer++
							board[nx][ny][0] = 0
						} else if board[nx][ny][0] == int('R') && k.color == 'G' {
							delete(tmp, Ele{
								x:     nx,
								y:     ny,
								color: 'R',
								days:  now_day,
							})
							delete(tmp, Ele{
								x:     nx,
								y:     ny,
								color: 'G',
								days:  now_day,
							})
							now_answer++
							board[nx][ny][0] = 0
						}
						continue
					}
				}
			}
		}
		q = tmp
	}
	answer.mutex.Lock()
	if answer.val < now_answer {
		answer.val = now_answer
	}
	answer.mutex.Unlock()
	wg.Done()
}

func parseInformation() {
	r := bufio.NewReader(os.Stdin)
	fmt.Fscan(r, &N, &M, &G, &R)
	if R < G {
		G, R = R, G
	}
	originGarden = make([][][2]int, N)
	for i := 0; i < N; i++ {
		originGarden[i] = make([][2]int, M)
	}
	for y := 0; y < N; y++ {
		for x := 0; x < M; x++ {
			fmt.Fscan(r, &originGarden[y][x][0])
			if originGarden[y][x][0] == 2 {
				waterPos = append(waterPos, [2]int{y, x})
				originGarden[y][x][0] = 1
			}
		}
	}
}
