package main

import (
	"adventofcode2022/coercion"
	"adventofcode2022/files"
	"adventofcode2022/helpers"
	"fmt"
	"regexp"
	"strings"
)

var (
	xyre = regexp.MustCompile(`x=(-?[0-9]+), y=(-?[0-9]+)`)
)

type Coordinate [3]int

func (c Coordinate) X() int {
	return c[0]
}

func (c Coordinate) Y() int {
	return c[1]
}

func (c Coordinate) D() int {
	return c[2]
}

func main() {
	var sensors []Coordinate
	var beacons []Coordinate
	files.MustScanFile("./day15/input/1.txt", func(s string) {
		l := strings.Split(s, ":")
		smatches := xyre.FindAllStringSubmatch(l[0], -1)
		bmatches := xyre.FindAllStringSubmatch(l[1], -1)

		sensor := Coordinate{
			coercion.ToInt(smatches[0][1]),
			coercion.ToInt(smatches[0][2]),
		}

		beacon := Coordinate{
			coercion.ToInt(bmatches[0][1]),
			coercion.ToInt(bmatches[0][2]),
		}

		sensor[2] = helpers.Abs(sensor.X()-beacon.X()) + helpers.Abs(sensor.Y()-beacon.Y())

		sensors = append(sensors, sensor)
		beacons = append(beacons, beacon)
	})

	r := Find(sensors, beacons)
	fmt.Println(r.X()*4000000 + r.Y())
}

func Find(sensors, beacons []Coordinate) (result Coordinate) {
	for _, s := range sensors {
		directions := []Coordinate{
			Coordinate{1, -1},
			Coordinate{1, 1},
			Coordinate{-1, -1},
			Coordinate{-1, 1},
		}

		for i := 0; i < len(directions); i++ {
			var x int
			y := s.Y()

			if directions[i].X() > 0 {
				x = (s.X() - s.D() - 1)
			} else {
				x = (s.X() + s.D() + 1)
			}

			for j := 0; j < s.D()+2; j++ {
				if x >= 0 && x <= 4000000 && y >= 0 && y <= 4000000 && !Within(x, y, sensors) && !In(x, y, beacons) {
					result[0] = x
					result[1] = y
					return result
				}

				x += directions[i].X()
				y += directions[i].Y()
			}
		}
	}
	return result
}

func Within(x, y int, sensors []Coordinate) bool {
	for _, s := range sensors {
		d := helpers.Abs(x-s.X()) + helpers.Abs(y-s.Y())
		if (s.X() == x && s.Y() == y) || d <= s.D() {
			return true
		}
	}
	return false
}

func In(x, y int, beacons []Coordinate) bool {
	for _, b := range beacons {
		if b.X() == x && b.Y() == y {
			return true
		}
	}
	return false
}
