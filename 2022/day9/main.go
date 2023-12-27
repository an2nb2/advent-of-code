package main

import (
	"adventofcode2022/files"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Position [2]int

func main() {
	visited := make(map[string]int)
	var knots [10]Position
	files.MustScanFile("./day9/input/1.txt", func(s string) {
		rule := strings.Split(s, " ")
		direction := rule[0]
		steps, _ := strconv.Atoi(rule[1])

		for i := 0; i < steps; i++ {
			knots = move(knots, direction)
			visited[fmt.Sprintf("%d:%d", knots[len(knots)-1][0], knots[len(knots)-1][1])] += 1
		}
	})

	fmt.Println(len(visited))
}

func move(knots [10]Position, direction string) [10]Position {
	switch direction {
	case "R":
		knots[0][1] += 1
	case "L":
		knots[0][1] -= 1
	case "D":
		knots[0][0] += 1
	case "U":
		knots[0][0] -= 1
	default:
		os.Exit(1)
	}

	return moveTail(knots)
}

func moveTail(knots [10]Position) [10]Position {
	for k := 1; k < len(knots); k++ {
		id := knots[k-1][0] - knots[k][0]
		jd := knots[k-1][1] - knots[k][1]

		if math.Abs(float64(id)) > 1 && math.Abs(float64(jd)) > 1 {
			if id > 0 {
				knots[k][0] = knots[k-1][0] - 1
			} else {
				knots[k][0] = knots[k-1][0] + 1
			}
			if jd > 0 {
				knots[k][1] = knots[k-1][1] - 1
			} else {
				knots[k][1] = knots[k-1][1] + 1
			}
		} else if math.Abs(float64(id)) > 1 {
			if id > 0 {
				knots[k][0] = knots[k-1][0] - 1
			} else {
				knots[k][0] = knots[k-1][0] + 1
			}
			knots[k][1] = knots[k-1][1]
		} else if math.Abs(float64(jd)) > 1 {
			if jd > 0 {
				knots[k][1] = knots[k-1][1] - 1
			} else {
				knots[k][1] = knots[k-1][1] + 1
			}
			knots[k][0] = knots[k-1][0]
		}
	}
	return knots
}
