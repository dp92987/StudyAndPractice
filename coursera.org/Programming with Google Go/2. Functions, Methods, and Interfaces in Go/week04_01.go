package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Animal interface {
	Eat() string
	Move() string
	Speak() string
	getName() string
}

type Cow struct {
	name       string
	food       string
	locomotion string
	noise      string
}

func (a *Cow) Eat() string {
	return "grass"
}

func (a *Cow) Move() string {
	return "walk"
}

func (a *Cow) Speak() string {
	return "moo"
}

func (a *Cow) getName() string {
	return a.name
}

type Bird struct {
	name       string
	food       string
	locomotion string
	noise      string
}

func (a *Bird) Eat() string {
	return "worms"
}

func (a *Bird) Move() string {
	return "fly"
}

func (a *Bird) Speak() string {
	return "peep"
}

func (a *Bird) getName() string {
	return a.name
}

type Snake struct {
	name       string
	food       string
	locomotion string
	noise      string
}

func (a *Snake) Eat() string {
	return "mice"
}

func (a *Snake) Move() string {
	return "slither"
}

func (a *Snake) Speak() string {
	return "hsss"
}

func (a *Snake) getName() string {
	return a.name
}

func main() {
	var animals []Animal

	reader := bufio.NewReader(os.Stdin)

	for {
		action, name, valTypeOrAction, err := parseInput(reader)
		if err != nil {
			log.Fatal(err)
		}
		if action == "X" {
			return
		}

		if action == "newanimal" {
			animals = addAnimal(animals, valTypeOrAction, name)
		} else if action == "query" {
			animal := getAnimal(animals, name)
			if animal != nil {
				printAnimalAction(animal, valTypeOrAction)
			}
		}
	}
}

func parseInput(reader *bufio.Reader) (string, string, string, error) {
	fmt.Print("> ")
	input, err := reader.ReadString('\n')
	if err != nil {
		return "", "", "", err
	}

	input = strings.Trim(input, "\n")
	if input == "X" {
		return "X", "", "", nil
	}

	splitInput := strings.Split(input, " ")
	if len(splitInput) <= 2 {
		return "", "", "", nil
	}

	action := splitInput[0]
	name := splitInput[1]
	type_ := splitInput[2]

	return action, name, type_, nil
}

func addAnimal(animals []Animal, valTypeOrAction string, name string) []Animal {
	switch valTypeOrAction {
	case "cow":
		animals = append(animals, &Cow{name: name})
	case "bird":
		animals = append(animals, &Bird{name: name})
	case "snake":
		animals = append(animals, &Snake{name: name})
	}

	return animals
}

func getAnimal(animals []Animal, name string) Animal {
	for _, animal := range animals {
		if animal.getName() == name {
			return animal
		}
	}

	return nil
}

func printAnimalAction(animal Animal, valTypeOrAction string) {
	switch valTypeOrAction {
	case "eat":
		fmt.Println(animal.Eat())
	case "move":
		fmt.Println(animal.Move())
	case "speak":
		fmt.Println(animal.Speak())
	}
}
