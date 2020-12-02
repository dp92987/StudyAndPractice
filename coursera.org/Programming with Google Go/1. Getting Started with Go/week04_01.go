package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("name: ")
	name, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	name = strings.Trim(name, "\n")

	fmt.Print("address: ")
	address, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	address = strings.Trim(address, "\n")

	var m = make(map[string]string)
	m["name"] = name
	m["address"] = address

	j, err := json.Marshal(m)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("encoded json:", j)
	fmt.Println("decoded json:", string(j))
}
