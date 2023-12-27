package main

import (
	"adventofcode2022/coercion"
	"adventofcode2022/files"
	"fmt"
	"strings"
)

func XYString(x, y int) string {
	return fmt.Sprintf("%d:%d", x, y)
}

func main() {
	field := make(map[string]bool)
	var bottom int

	files.MustScanFile("./day14/input/1.txt", func(s string) {
		line := strings.Split(s, " -> ")

		for i := 0; i < len(line)-1; i++ {
			fromxy := strings.Split(line[i], ",")
			fromx := coercion.ToInt(fromxy[0])
			fromy := coercion.ToInt(fromxy[1])

			toxy := strings.Split(line[i+1], ",")
			tox := coercion.ToInt(toxy[0])
			toy := coercion.ToInt(toxy[1])

			bottom = max(bottom, toy)

			for j := min(fromy, toy); j <= max(fromy, toy); j++ {
				for k := min(fromx, tox); k <= max(fromx, tox); k++ {
					field[XYString(k, j)] = true
				}
			}
		}
	})

	var total int
	for emulateSandUnit(field, bottom) {
		total++
	}
	fmt.Println(total + 1)
}

func emulateSandUnit(field map[string]bool, bottom int) bool {
	x := 500
	y := 0
	ground := bottom + 1
	for y <= ground {
		if y == ground {
			field[XYString(x, y)] = false
			break
		} else if _, ok := field[XYString(x, y+1)]; !ok { // Down
			y++
		} else if _, ok := field[XYString(x-1, y+1)]; !ok { // Down Left
			y++
			x--
		} else if _, ok := field[XYString(x+1, y+1)]; !ok { // Down Right
			y++
			x++
		} else {
			field[XYString(x, y)] = false
			break
		}
	}
	return y != 0
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}
