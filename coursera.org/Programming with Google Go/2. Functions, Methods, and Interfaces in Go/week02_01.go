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
	a, err := getValue("acceleration")
	if err != nil {
		log.Fatal(err)
	}

	v0, err := getValue("initial velocity")
	if err != nil {
		log.Fatal(err)
	}

	s0, err := getValue("initial displacement")
	if err != nil {
		log.Fatal(err)
	}

	t, err := getValue("time")
	if err != nil {
		log.Fatal(err)
	}

	fn := genDisplaceFn(a, v0, s0)
	fmt.Println("result:", fn(t))
}

func getValue(prompt string) (float64, error) {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print(prompt, ": ")
	input, err := reader.ReadString('\n')
	if err != nil {
		return 0, err
	}

	val, err := strconv.ParseFloat(strings.Trim(input, "\n"), 64)
	if err != nil {
		return 0, err
	}

	return val, nil
}

func genDisplaceFn(a float64, v0 float64, s0 float64) func(t float64) float64 {
	return func(t float64) float64 { return 1/2*a*t*t + v0*t + s0 }
}
