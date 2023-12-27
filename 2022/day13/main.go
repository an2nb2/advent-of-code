package main

import (
	"adventofcode2022/coercion"
	"adventofcode2022/files"
	"bufio"
	"fmt"
	"sort"
	"strings"

	"github.com/gammazero/deque"
)

type Element struct {
	value any
}

type List struct {
	elements []Element
}

func main() {
	d1 := deepParse("[[2]]")
	d2 := deepParse("[[6]]")
	lists := []*List{
		d1,
		d2,
	}

	files.MustOpenWithScanner("./day13/input/1.txt", func(scanner *bufio.Scanner) {
		for scanner.Scan() {
			if scanner.Text() != "" {
				lists = append(lists, deepParse(scanner.Text()))
			}
		}
	})

	sort.Slice(lists, func(i, j int) bool {
		return eq(lists[i], lists[j]) == 1
	})

	var d1i, d2i int
	for i := 0; i < len(lists); i++ {
		if lists[i] == d1 {
			d1i = i + 1
		} else if lists[i] == d2 {
			d2i = i + 1
		}
	}
	fmt.Println(d1i * d2i)
}

func eq(left, right *List) int {
	until := maxLen(right, left)
	for i := 0; i < until; i++ {
		if i == len(left.elements) {
			return 1
		}

		if i == len(right.elements) {
			return 0
		}

		_, lint := left.elements[i].value.(int)
		_, rint := right.elements[i].value.(int)

		if lint && rint {
			d := left.elements[i].value.(int) - right.elements[i].value.(int)
			if d < 0 {
				return 1
			} else if d > 0 {
				return 0
			}
		} else if !lint && !rint {
			res := eq(left.elements[i].value.(*List), right.elements[i].value.(*List))
			if res >= 0 {
				return res
			}
		} else if lint && !rint {
			value := left.elements[i].value.(int)
			res := eq(&List{[]Element{Element{value}}}, right.elements[i].value.(*List))
			if res >= 0 {
				return res
			}
		} else {
			value := right.elements[i].value.(int)
			res := eq(left.elements[i].value.(*List), &List{[]Element{Element{value}}})
			if res >= 0 {
				return res
			}
		}
	}

	return -1
}

func maxLen(a, b *List) int {
	if len(a.elements) > len(b.elements) {
		return len(a.elements)
	}
	return len(b.elements)
}

func deepParse(s string) *List {
	q := deque.New[*List]()

	var current *List
	for i := 0; i < len(s); i++ {
		switch s[i] {
		case '[':
			l := &List{}
			if current != nil {
				current.elements = append(current.elements, Element{l})
				q.PushBack(current)
			}
			current = l
		case ']':
			if q.Len() > 0 {
				current = q.PopBack()
			}
		case ',':
		default:
			n, newi := sliceNumber(string(s[i:]))
			i += newi
			current.elements = append(current.elements, sliceStrToElements(strings.Split(n, ","))...)
		}
	}

	return current
}

func sliceNumber(s string) (string, int) {
	bracket := strings.Index(s, "]")
	coma := strings.Index(s, ",")
	if bracket >= 0 && (coma < 0 || coma > bracket) {
		return string(s[0:bracket]), bracket - 1
	} else if coma >= 0 {
		return string(s[0:coma]), coma - 1
	}
	return s, 0
}

func sliceStrToElements(strs []string) (result []Element) {
	for _, s := range strs {
		result = append(result, Element{coercion.ToInt(s)})
	}
	return
}
