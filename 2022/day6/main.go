package main

import (
	"log"
	"os"
	"strings"
)

func main() {
	data, err := os.ReadFile("./day6/input/1.txt")
	if err != nil {
		log.Fatal(err)
	}

	var from int
	var to int = 1
	for to < len(data) {
		index := strings.Index(string(data[from:to-1]), string(data[to-1]))
		if index >= 0 {
			from = from + index + 1
		}

		if to-from >= 14 {
			if index < 0 {
				break
			}
			from++
		}
		to++
	}

	log.Printf("Start position - %d", to)
}
