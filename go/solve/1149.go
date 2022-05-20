package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

type container struct {
	totalSum float64
	RGB      [][]float64
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)
	con := container{}
	for i := 0; i < n; i++ {
		var a, b, c float64
		fmt.Fscanln(reader, &a, &b, &c)
		con.RGB = append(con.RGB, []float64{a, b, c})
	}
	for i := range con.RGB {
		if i == 0 {
			continue
		}
		con.RGB[i][0] = con.RGB[i][0] + math.Min(con.RGB[i-1][1], con.RGB[i-1][2])
		con.RGB[i][1] = con.RGB[i][1] + math.Min(con.RGB[i-1][0], con.RGB[i-1][2])
		con.RGB[i][2] = con.RGB[i][2] + math.Min(con.RGB[i-1][0], con.RGB[i-1][1])
	}
	tmp := math.Min(con.RGB[len(con.RGB)-1][0], con.RGB[len(con.RGB)-1][1])
	fmt.Println(math.Min(tmp, con.RGB[len(con.RGB)-1][2]))
}
