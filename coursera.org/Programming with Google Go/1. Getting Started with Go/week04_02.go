package main

import (
	"bufio"
	"log"
	"os"
	"strings"
)

func main() {
	type Name struct {
		fname string
		lname string
	}

	var err error
	var file *os.File
	var persons []Name

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	fileName := scanner.Text()

	file, err = os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}

	scanner = bufio.NewScanner(file)
	for scanner.Scan() {
		fullName := strings.Split(scanner.Text(), " ")
		person := Name{fullName[0], fullName[1]}
		persons = append(persons, person)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	err = file.Close()
	if err != nil {
		log.Fatal(err)
	}

	log.Println(persons)
}
