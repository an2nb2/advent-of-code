package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("./day1/input/1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close() // #nosec

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	var maxCallories [3]int
	var currElfCallories int
	for {
		proceed := fileScanner.Scan()
		scanned := fileScanner.Text()

		if scanned != "" {
			callories, err := strconv.Atoi(scanned)
			if err != nil {
				log.Fatal(err)
			}
			currElfCallories += callories
		}

		if !proceed || scanned == "" {
			for i := 0; i < len(maxCallories); i++ {
				if currElfCallories >= maxCallories[i] {
					maxCallories[i], currElfCallories = currElfCallories, maxCallories[i]
				}
			}
			currElfCallories = 0
		}

		if !proceed {
			break
		}
	}

	var sum int
	for _, v := range maxCallories {
		sum += v
	}

	log.Printf("Sum of Callories of Top 3 Elfs - %d", sum)
}
