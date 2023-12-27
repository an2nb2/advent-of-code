package main

import (
	"adventofcode2022/files"
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var trees [][]int
	files.MustScanFile("./day8/input/1.txt", func(s string) {
		var row []int
		for _, v := range strings.Split(s, "") {
			height, _ := strconv.Atoi(v)
			row = append(row, height)
		}
		trees = append(trees, row)
	})

	max := 0
	for i := 1; i < len(trees)-1; i++ {
		for j := 1; j < len(trees[i])-1; j++ {
			res := calculateUp(i, j, trees) * calculateDown(i, j, trees) * calculateRight(i, j, trees) * calculateLeft(i, j, trees)
			if res > max {
				max = res
			}
		}
	}
	fmt.Println(max)
}

func calculateUp(i, j int, trees [][]int) (result int) {
	for k := i - 1; k >= 0; k-- {
		result += 1
		if trees[i][j] <= trees[k][j] {
			break
		}
	}
	return
}

func calculateDown(i, j int, trees [][]int) (result int) {
	for k := i + 1; k < len(trees); k++ {
		result += 1
		if trees[i][j] <= trees[k][j] {
			break
		}
	}
	return
}

func calculateLeft(i, j int, trees [][]int) (result int) {
	for k := j - 1; k >= 0; k-- {
		result += 1
		if trees[i][j] <= trees[i][k] {
			break
		}
	}
	return
}

func calculateRight(i, j int, trees [][]int) (result int) {
	for k := j + 1; k < len(trees[i]); k++ {
		result += 1
		if trees[i][j] <= trees[i][k] {
			break
		}
	}
	return
}
