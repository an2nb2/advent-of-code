package main

import (
	"bufio"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type stack []string

func (s stack) Push(v []string) stack {
	return append(s, v...)
}

func (s stack) Pop(length int) (stack, []string) {
	l := len(s)
	if l == 0 || length > l {
		log.Fatal("stack is empty")
	}
	return s[:l-length], s[l-length : l]
}

var (
	stacks = [9]stack{
		stack{"F", "H", "B", "V", "R", "Q", "D", "P"},
		stack{"L", "D", "Z", "Q", "W", "V"},
		stack{"H", "L", "Z", "Q", "G", "R", "P", "C"},
		stack{"R", "D", "H", "F", "J", "V", "B"},
		stack{"Z", "W", "L", "C"},
		stack{"J", "R", "P", "N", "T", "G", "V", "M"},
		stack{"J", "R", "L", "V", "M", "B", "S"},
		stack{"D", "P", "J"},
		stack{"D", "C", "N", "W", "V"},
	}
)

func main() {
	file, err := os.Open("./day5/input/1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close() // #nosec

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	r := regexp.MustCompile("^move ([0-9]+) from ([0-9]+) to ([0-9]+)$")
	var cranes []string
	for fileScanner.Scan() {
		s := fileScanner.Text()

		matches := r.FindAllStringSubmatch(s, -1)
		if len(matches) > 0 && len(matches[0]) == 4 {
			num, _ := strconv.Atoi(matches[0][1])
			from, _ := strconv.Atoi(matches[0][2])
			to, _ := strconv.Atoi(matches[0][3])

			stacks[from-1], cranes = stacks[from-1].Pop(num)
			stacks[to-1] = stacks[to-1].Push(cranes)
		}
	}

	var result string
	for _, s := range stacks {
		if len(s) > 0 {
			_, v := s.Pop(1)
			result += strings.Join(v, "")
		}
	}

	log.Printf("Result - %s", result)
}
