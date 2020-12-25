package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	input, err := getInput()
	if err != nil {
		log.Fatal(err)
	}

	numbers, err := getTenNumbersFromInput(input)
	if err != nil {
		log.Fatal(err)
	}

	sortBubble(numbers)

	fmt.Println("result:", numbers)
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

func getTenNumbersFromInput(input string) ([]int, error) {
	splitInput := strings.Split(input, " ")
	if len(splitInput) > 10 {
		splitInput = splitInput[0:10]
	}

	var numbers = make([]int, len(splitInput))
	for i, s := range splitInput {
		num, err := strconv.Atoi(s)
		if err != nil {
			return []int{}, err
		}
		numbers[i] = num
	}

	return numbers, nil
}

func sortBubble(numbers []int) {
	var sorted bool

	for {
		sorted = true
		for i := 1; i < len(numbers); i++ {
			if numbers[i] < numbers[i-1] {
				sorted = false
				swapNumbers(numbers, i)
			}
		}
		if sorted == true {
			break
		}
	}
}

func swapNumbers(numbers []int, i int) {
	tmp := numbers[i]
	numbers[i] = numbers[i-1]
	numbers[i-1] = tmp
}
