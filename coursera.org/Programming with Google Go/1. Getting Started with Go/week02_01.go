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
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("input: ")
	input, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	input = strings.Trim(input, "\n")

	num, err := strconv.ParseFloat(input, 64)
	if err != nil {
		log.Fatal(err)
	}

	intNum := int(num)
	fmt.Println("result:", intNum)
}
