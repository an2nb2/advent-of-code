package main

import (
	"bufio"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("./day3/input/1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close() // #nosec

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	var repeated []string
	var elfingroup int = 1
	itemsMap := make(map[string]int)
	for fileScanner.Scan() {
		scanned := fileScanner.Text()
		items := strings.Split(scanned, "")

		for _, item := range items {
			itemsMap[item] |= (1 << (elfingroup - 1))
		}

		elfingroup++

		if elfingroup > 3 {
			for item, value := range itemsMap {
				if value == 7 {
					repeated = append(repeated, item)
				}
			}

			itemsMap = map[string]int{}
			elfingroup = 1
		}
	}

	var sum int
	for _, v := range repeated {
		sum += getItemValue([]rune(v)[0])
	}

	log.Printf("Total sum - %d", sum)
}

func getItemValue(c rune) int {
	upper := 65
	lower := 97

	if int(c) >= upper && int(c) <= upper+25 {
		return int(c) - 38
	}
	if int(c) >= lower && int(c) <= lower+25 {
		return int(c) - 96
	}

	return 0
}
