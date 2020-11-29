package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {
	var input string
	var slice = make([]int, 3, 3)

	for i := 0; ; i++ {
		_, _ = fmt.Scan(&input)

		if input == "X" {
			break
		} else {
			intInput, err := strconv.Atoi(input)
			if err != nil {
				fmt.Println(err)
				continue
			}

			if i < len(slice) {
				slice[i] = intInput
			} else {
				slice = append(slice, intInput)
			}

			sortedSlice := make([]int, len(slice), cap(slice))
			copy(sortedSlice, slice)
			sort.Ints(sortedSlice)
			fmt.Println(sortedSlice)
		}
	}
}
