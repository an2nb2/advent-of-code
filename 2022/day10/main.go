package main

import (
	"adventofcode2022/files"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type State struct {
	X int
}

type CRT struct {
	row    int
	column int
}

func (c *CRT) tick(s State) {
	if math.Abs(float64(s.X-c.column)) <= 1 {
		fmt.Print("#")
	} else {
		fmt.Print(".")
	}

	if c.column == 39 {
		fmt.Print("\n")
		c.column = 0
		c.row++
	} else {
		c.column += 1
	}
}

var (
	cycle int
	state State = State{X: 1}
	crt   *CRT  = &CRT{}
)

func main() {
	files.MustScanFile("./day10/input/1.txt", func(s string) {
		instruction := strings.Split(s, " ")
		if len(instruction) > 1 {
			execute(instruction[0], instruction[1])
		} else {
			execute(instruction[0], "")
		}
	})
}

func execute(instruction, args string) {
	switch instruction {
	case "addx":
		tick()
		tick()
		inc, _ := strconv.Atoi(args)
		state.X += inc
	case "noop":
		tick()
	default:
		os.Exit(1)
	}
}

func tick() {
	cycle++
	crt.tick(state)
}
