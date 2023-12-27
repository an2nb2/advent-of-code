package files

import (
	"bufio"
	"fmt"
	"os"
)

type TextProcessor func(s string)
type WithScanner func(s *bufio.Scanner)

func ScanFile(filepath string, p TextProcessor) error {
	file, err := os.Open(filepath) // #nosec
	if err != nil {
		return err
	}
	defer file.Close() // #nosec

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		p(fileScanner.Text())
	}

	return nil
}

func MustScanFile(filepath string, p TextProcessor) {
	err := ScanFile(filepath, p)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func MustOpenWithScanner(filepath string, p WithScanner) {
	file, err := os.Open(filepath) // #nosec
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer file.Close() // #nosec

	fileScanner := bufio.NewScanner(file)
	fileScanner.Split(bufio.ScanLines)

	p(fileScanner)
}
