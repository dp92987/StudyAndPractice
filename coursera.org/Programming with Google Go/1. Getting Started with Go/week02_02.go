package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("input: ")
	input, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	input = strings.Trim(input, "\n")

	if len(input) == 0 {
		return
	}

	firstChar := strings.ToLower(string(input[0]))
	lastChar := strings.ToLower(string(input[len(input)-1]))

	if firstChar == "i" && lastChar == "n" && strings.Contains(input, "a") {
		fmt.Println("result: Found!")
	} else {
		fmt.Println("result: Not found!")
	}
}
