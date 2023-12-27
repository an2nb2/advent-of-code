package main

import (
	"adventofcode2022/files"
	"fmt"
	"strings"

	"github.com/gammazero/deque"
)

type Position struct {
	row    int
	column int
	dist   int
}

func (p Position) String() string {
	return fmt.Sprintf("%d:%d", p.row, p.column)
}

func (p Position) Eq(s Position) bool {
	return p.row == s.row && p.column == s.column
}

func main() {
	var field [][]int
	var end Position

	files.MustScanFile("./day12/input/1.txt", func(s string) {
		var row []int
		for _, value := range strings.Split(s, "") {
			var height int
			if value == "S" {
				height = getItemValue('a')
			} else if value == "E" {
				end = Position{len(field), len(row), 0}
				height = getItemValue('z')
			} else {
				height = getItemValue([]rune(value)[0])
			}
			row = append(row, height)
		}
		field = append(field, row)
	})

	fmt.Println(find(Position{0, 0, 0}, end, field))
}

func find(start, end Position, field [][]int) int {
	steps := make(map[string]int)
	q := deque.New[Position]()

	steps[start.String()] = 1
	q.PushBack(start)

	for q.Len() != 0 {
		c := q.PopFront()

		neighbours := [4]Position{
			Position{c.row + 1, c.column, c.dist + 1},
			Position{c.row - 1, c.column, c.dist + 1},
			Position{c.row, c.column + 1, c.dist + 1},
			Position{c.row, c.column - 1, c.dist + 1},
		}
		for _, n := range neighbours {
			if _, ok := steps[n.String()]; ok {
				continue
			}
			if n.row < 0 || n.column < 0 {
				continue
			}
			if n.row >= len(field) || n.column >= len(field[n.row]) {
				continue
			}
			if field[n.row][n.column]-field[c.row][c.column] > 1 {
				continue
			}
			if field[n.row][n.column] == getItemValue('a') {
				n.dist = 0
			}
			if n.Eq(end) {
				return n.dist
			}
			steps[n.String()] += 1
			q.PushBack(n)
		}
	}
	return 0
}

func getItemValue(c rune) int {
	return int(c) - 96
}
