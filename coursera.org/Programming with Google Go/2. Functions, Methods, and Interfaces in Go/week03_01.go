package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Animal struct {
	food       string
	locomotion string
	noise      string
}

func (a *Animal) Eat() string {
	return a.food
}

func (a *Animal) Move() string {
	return a.locomotion
}

func (a *Animal) Speak() string {
	return a.noise
}

func main() {
	cow, bird, snake := initAnimals()

	reader := bufio.NewReader(os.Stdin)

	for {
		animal, action, err := parseInput(reader)
		if err != nil {
			log.Fatal(err)
		}
		if animal == "X" {
			return
		}

		printAnimalAction(animal, action, &cow, &bird, &snake)
	}
}

func initAnimals() (Animal, Animal, Animal) {
	return Animal{food: "grass", locomotion: "walk", noise: "moo"},
		Animal{food: "worms", locomotion: "fly", noise: "peep"},
		Animal{food: "mice", locomotion: "slither", noise: "hss"}
}

func parseInput(reader *bufio.Reader) (string, string, error) {
	fmt.Print("> ")
	input, err := reader.ReadString('\n')
	if err != nil {
		return "", "", err
	}

	input = strings.Trim(input, "\n")
	if input == "X" {
		return "X", "", nil
	}

	splitInput := strings.Split(input, " ")
	if len(splitInput) <= 1 {
		return "", "", nil
	}

	animal := splitInput[0]
	action := splitInput[1]

	return animal, action, nil
}

func printAnimalAction(animal string, action string, cow *Animal, bird *Animal, snake *Animal) {
	if animal == "cow" {
		switch action {
		case "eat":
			fmt.Println(cow.Eat())
		case "move":
			fmt.Println(cow.Move())
		case "speak":
			fmt.Println(cow.Speak())
		}
	} else if animal == "bird" {
		switch action {
		case "eat":
			fmt.Println(bird.Eat())
		case "move":
			fmt.Println(bird.Move())
		case "speak":
			fmt.Println(bird.Speak())
		}
	} else if animal == "snake" {
		switch action {
		case "eat":
			fmt.Println(snake.Eat())
		case "move":
			fmt.Println(snake.Move())
		case "speak":
			fmt.Println(snake.Speak())
		}
	}
}
