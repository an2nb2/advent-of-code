package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("./day4/input/1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close() // #nosec

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	var sum int
	for fileScanner.Scan() {
		ranges := strings.Split(fileScanner.Text(), ",")
		first := strings.Split(ranges[0], "-")
		second := strings.Split(ranges[1], "-")

		f1, _ := strconv.Atoi(first[0])
		f2, _ := strconv.Atoi(first[1])
		s1, _ := strconv.Atoi(second[0])
		s2, _ := strconv.Atoi(second[1])

		if (f1 >= s1 && f1 <= s2) || (f1 <= s1 && f2 >= s1) {
			log.Println(ranges)
			sum += 1
		}
	}

	log.Printf("Total - %d", sum)
}
