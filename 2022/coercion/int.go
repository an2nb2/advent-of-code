package coercion

import "strconv"

func ToInt(s string) int {
	val, _ := strconv.Atoi(s)
	return val
}

func SliceStrToInt(strs []string) (result []int) {
	for _, s := range strs {
		result = append(result, ToInt(s))
	}
	return
}

func ToUint(s string) uint64 {
	val := ToInt(s)
	return uint64(val)
}

func SliceStrToUint(strs []string) (result []uint64) {
	for _, s := range strs {
		result = append(result, ToUint(s))
	}
	return
}
