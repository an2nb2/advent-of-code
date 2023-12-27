package main

import (
	"bufio"
	"log"
	"os"
	"strings"
)

var (
	shapeWinMap = map[string]string{
		"X": "C",
		"Y": "A",
		"Z": "B",
		"A": "Z",
		"B": "X",
		"C": "Y",
	}

	shapeLoseMap = map[string]string{
		"A": "Y",
		"B": "Z",
		"C": "X",
		"X": "B",
		"Y": "C",
		"Z": "A",
	}

	drawScore = 3
	winScore  = 6
)

func main() {
	file, err := os.Open("./day2/input/1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close() // #nosec

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	var score int
	for fileScanner.Scan() {
		scanned := fileScanner.Text()

		shapes := strings.Split(scanned, " ")
		if len(shapes) != 2 {
			log.Fatalf("Invalid input - %s", scanned)
		}

		switch shapes[1] {
		case "X":
			score += shapeScore(shapeWinMap[shapes[0]])
		case "Y":
			score += shapeScore(shapes[0]) + drawScore
		case "Z":
			score += shapeScore(shapeLoseMap[shapes[0]]) + winScore
		}
	}

	log.Printf("Total score - %d", score)
}

func shapeScore(shape string) int {
	switch shape {
	case "A", "X":
		return 1
	case "B", "Y":
		return 2
	case "C", "Z":
		return 3
	default:
		log.Fatalf("Uknown shape %s", shape)
	}
	return 0
}
