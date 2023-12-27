package main

import (
	"adventofcode2022/coercion"
	"adventofcode2022/files"
	"adventofcode2022/helpers"
	"fmt"
	"regexp"
	"strings"

	"github.com/gammazero/deque"
)

var (
	re = regexp.MustCompile(`^Valve ([A-Z]+) has flow rate=([0-9]+); tunnels* leads* to valves* (.+)$`)
)

type Valve struct {
	name string
	rate int
	adj  []string
}

func main() {
	valves := make(map[string]*Valve)

	files.MustScanFile("./day16/input/1.txt", func(s string) {
		matches := re.FindAllStringSubmatch(s, -1)

		valves[matches[0][1]] = &Valve{
			name: matches[0][1],
			rate: coercion.ToInt(matches[0][2]),
			adj:  strings.Split(matches[0][3], ", "),
		}
	})

	paths := CalculatePaths(valves)
	cache := make(map[string]int)
	valveIndx := make(map[string]int)

	var i int
	for name := range valves {
		if valves[name].rate == 0 {
			continue
		}
		valveIndx[name] = i
		i++
	}

	to := (1 << len(valveIndx)) - 1

	var max int
	for i := 0; i < (to/2)-1; i++ {
		max = helpers.Max(max, Solve(valves["AA"], 0, i, valves, paths, cache, valveIndx)+Solve(valves["AA"], 0, to^i, valves, paths, cache, valveIndx))
	}

	fmt.Println(max)
}

// This function uses BFS algoright to calculate shortest paths for
// every node to every other reachable node in the valves graph
func CalculatePaths(valves map[string]*Valve) map[string]map[string]int {
	paths := make(map[string]map[string]int)

	for name, valve := range valves {
		paths[name] = make(map[string]int)
		paths[name][name] = 0

		q := deque.New[*Valve]()
		q.PushBack(valve)

		visits := make(map[string]bool)
		visits[name] = true

		for q.Len() != 0 {
			v := q.PopFront()

			for _, n := range v.adj {
				if _, ok := visits[n]; ok {
					continue
				}
				paths[name][n] = paths[name][v.name] + 1
				visits[n] = true
				q.PushBack(valves[n])
			}
		}
	}

	return paths
}

// This function uses DFS algorithm to calculate the optimal path
func Solve(current *Valve, minute int, visited int, valves map[string]*Valve, paths map[string]map[string]int, cache map[string]int, valveIndx map[string]int) int {
	if minute >= 26 {
		return 0
	}

	if val, ok := cache[CacheKey(current, minute, visited)]; ok {
		return val
	}

	var max int
	for name, path := range paths[current.name] {
		currBit := 1 << valveIndx[name]
		if (visited & currBit) > 0 {
			continue
		}
		time := minute + path + 1
		rate := valves[name].rate * (26 - time)

		max = helpers.Max(max, Solve(valves[name], time, visited|currBit, valves, paths, cache, valveIndx)+rate)
	}

	cache[CacheKey(current, minute, visited)] = max

	return max
}

func CacheKey(current *Valve, minute int, visited int) string {
	return fmt.Sprintf("%s-%d-%d", current.name, minute, visited)
}
