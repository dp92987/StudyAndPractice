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

	name, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	name = strings.Trim(name, "\n")

	address, err := reader.ReadString('\n')
	if err != nil {
		log.Fatal(err)
	}
	address = strings.Trim(address, "\n")

	var m = make(map[string]string)
	m["name"] = name
	m["address"] = address

	j, err := json.MarshalIndent(m, "", "\t")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(string(j))
}
