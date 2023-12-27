package main

import (
	"adventofcode2022/coercion"
	"adventofcode2022/files"
	"bufio"
	"fmt"
	"regexp"
	"sort"
	"strings"
)

var (
	itemsre     = regexp.MustCompile(`Starting items: (.+)$`)
	operationre = regexp.MustCompile(`Operation: (.+) = (.+) (.+) (.+)$`)
	testre      = regexp.MustCompile(`Test: divisible by (.*)$`)
	testtruere  = regexp.MustCompile(`If true: throw to monkey (.*)$`)
	testfalsere = regexp.MustCompile(`If false: throw to monkey (.*)$`)
)

type Monkey struct {
	items        []int
	operation    Operation
	devisibleBy  int
	truOutcome   int
	falseOutcome int
	inspected    int
}

type Operation struct {
	result   string
	op1      string
	op2      string
	operator string
}

func (o Operation) execute(item int) int {
	var op1, op2 int
	if o.op1 == "old" {
		op1 = item
	} else {
		op1 = coercion.ToInt(o.op1)
	}

	if o.op2 == "old" {
		op2 = item
	} else {
		op2 = coercion.ToInt(o.op2)
	}

	switch o.operator {
	case "+":
		return op1 + op2
	case "-":
		return op1 - op2
	case "*":
		return op1 * op2
	case "/":
		return op1 / op2
	}

	return 0
}

func (m *Monkey) play() int {
	m.inspected++
	item := m.items[0]
	m.items = m.items[1:len(m.items)]
	return m.operation.execute(item)
}

func scanMonkey(scanner *bufio.Scanner) *Monkey {
	scanner.Scan()
	itemsmatches := itemsre.FindAllStringSubmatch(scanner.Text(), -1)
	scanner.Scan()
	operationmatches := operationre.FindAllStringSubmatch(scanner.Text(), -1)
	scanner.Scan()
	testmatches := testre.FindAllStringSubmatch(scanner.Text(), -1)
	scanner.Scan()
	testtrumatches := testtruere.FindAllStringSubmatch(scanner.Text(), -1)
	scanner.Scan()
	testfalsematches := testfalsere.FindAllStringSubmatch(scanner.Text(), -1)
	return &Monkey{
		items: coercion.SliceStrToInt(strings.Split(itemsmatches[0][1], ", ")),
		operation: Operation{
			result:   operationmatches[0][1],
			op1:      operationmatches[0][2],
			op2:      operationmatches[0][4],
			operator: operationmatches[0][3],
		},
		devisibleBy:  coercion.ToInt(testmatches[0][1]),
		truOutcome:   coercion.ToInt(testtrumatches[0][1]),
		falseOutcome: coercion.ToInt(testfalsematches[0][1]),
	}
}

func main() {
	var monkeys []*Monkey
	files.MustOpenWithScanner("./day11/input/1.txt", func(scanner *bufio.Scanner) {
		for scanner.Scan() {
			s := scanner.Text()

			if strings.HasPrefix(s, "Monkey") {
				monkeys = append(monkeys, scanMonkey(scanner))
			}
		}
	})

	var mod int = 1
	for _, m := range monkeys {
		mod *= m.devisibleBy
	}

	for k := 0; k < 10000; k++ {
		for _, monkey := range monkeys {
			for len(monkey.items) != 0 {
				item := monkey.play()
				item %= mod
				if item%monkey.devisibleBy == 0 {
					monkeys[monkey.truOutcome].items = append(monkeys[monkey.truOutcome].items, item)
				} else {
					monkeys[monkey.falseOutcome].items = append(monkeys[monkey.falseOutcome].items, item)
				}
			}
		}
	}

	sort.Slice(monkeys, func(i, j int) bool {
		return monkeys[i].inspected > monkeys[j].inspected
	})

	fmt.Println(monkeys[0].inspected * monkeys[1].inspected)
}
