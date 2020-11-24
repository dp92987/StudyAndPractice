package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	var name string
	var address string
	var m = make(map[string]string)

	_, _ = fmt.Scan(&name, &address)

	m["name"] = name
	m["address"] = address

	j, _ := json.Marshal(m)

	fmt.Println(j)
}
