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
	input, err := getInput()
	if err != nil {
		log.Fatal(err)
	}

	nums, err := getNumsFromInput(input)
	if err != nil {
		log.Fatal(err)
	}

	cut := len(nums) / 4

	var numsOne []int
	var numsTwo []int
	var numsThree []int
	var numsFour []int

	numsOne = append(numsOne, nums[0:cut]...)
	numsTwo = append(numsTwo, nums[cut:cut*2]...)
	numsThree = append(numsThree, nums[cut*2:cut*3]...)
	numsFour = append(numsFour, nums[cut*3:]...)

	var c = make(chan []int, 4)

	go sortNums(numsOne, c)
	go sortNums(numsTwo, c)
	go sortNums(numsThree, c)
	go sortNums(numsFour, c)

	sortedNumsOne := <-c
	sortedNumbersTwo := <-c
	sortedNumbersThree := <-c
	sortedNumbersFour := <-c

	var mergedNums []int
	mergedNums = append(mergedNums, sortedNumsOne...)
	mergedNums = append(mergedNums, sortedNumbersTwo...)
	mergedNums = append(mergedNums, sortedNumbersThree...)
	mergedNums = append(mergedNums, sortedNumbersFour...)

	sort.Ints(mergedNums)

	fmt.Printf("result: %v\n", mergedNums)
}

func getInput() (string, error) {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("input: ")
	input, err := reader.ReadString('\n')
	if err != nil {
		return "", err
	}

	return strings.Trim(input, "\n"), nil
}

func getNumsFromInput(input string) ([]int, error) {
	splitInput := strings.Split(input, " ")

	var numbers = make([]int, len(splitInput))
	for i, s := range splitInput {
		num, err := strconv.Atoi(s)
		if err != nil {
			return nil, err
		}
		numbers[i] = num
	}

	return numbers, nil
}

func sortNums(nums []int, c chan []int) {
	fmt.Printf("to be sorted: %v\n", nums)
	sort.Ints(nums)
	c <- nums
}
