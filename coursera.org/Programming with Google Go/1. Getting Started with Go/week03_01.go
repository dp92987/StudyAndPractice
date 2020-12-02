package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	var slice = make([]int, 3)
	reader := bufio.NewReader(os.Stdin)

	for i := 0; ; i++ {
		fmt.Print("input (X to quit): ")
		input, err := reader.ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}
		input = strings.Trim(input, "\n")

		if input == "X" {
			break
		}

		intInput, err := strconv.Atoi(input)
		if err != nil {
			fmt.Println(err)
			continue
		}

		if i < len(slice) {
			slice[i] = intInput
			sortedSlice := make([]int, len(slice), cap(slice))
			copy(sortedSlice, slice)
			sort.Ints(sortedSlice)
			fmt.Println("slice:", sortedSlice)
		} else {
			slice = append(slice, intInput)
			sort.Ints(slice)
			fmt.Println("slice:", slice)
		}
	}
}
