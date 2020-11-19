package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	var s string

	_, _ = fmt.Scan(&s)

	if unicode.ToLower(rune(s[len(s)-1])) == 'n' && unicode.ToLower(rune(s[0])) == 'i' && strings.Contains(s, "a") {
		fmt.Println("Found!")
	} else {
		fmt.Println("Not found!")
	}
}
