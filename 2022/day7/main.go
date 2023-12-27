package main

import (
	"adventofcode2022/files"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var (
	commandre = regexp.MustCompile(`^\$ ([a-zA-Z0-9]+) *(.*)$`)
)

func parseCommand(s string) (cmd string, args string) {
	matches := commandre.FindAllStringSubmatch(s, -1)
	if len(matches) == 1 || len(matches[0]) == 3 {
		cmd = matches[0][1]
		args = matches[0][2]
	} else {
		fmt.Printf("invalid command - %s\n", s)
		os.Exit(1)
	}
	return
}

func main() {
	folders := map[string]int{}
	var currentPath []string
	var currentCmd string

	err := files.ScanFile("./day7/input/1.txt", func(s string) {
		if s[0] == '$' {
			cmd, args := parseCommand(s)
			if cmd == "cd" {
				switch args {
				case "..":
					currentPath = currentPath[0 : len(currentPath)-1]
				case "/":
					currentPath = []string{""}
				default:
					currentPath = append(currentPath, args)
				}
			}
			currentCmd = cmd
		} else {
			if currentCmd == "ls" {
				output := strings.Split(s, " ")
				if len(output) > 1 {
					if output[0] != "dir" {
						size, _ := strconv.Atoi(output[0])
						for i := 0; i < len(currentPath); i++ {
							folders[strings.Join(currentPath[0:i+1], "/")] += size
						}
					}
				}
			}
		}
	})
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	used := 70000000 - folders[""]
	required := 30000000
	minFolderSize := required - used

	var total, min int
	for _, size := range folders {
		if size <= 100000 {
			total += size
		}
		if size >= minFolderSize {
			if min == 0 || size < min {
				min = size
			}
		}
	}
	fmt.Println(total, min)
}
