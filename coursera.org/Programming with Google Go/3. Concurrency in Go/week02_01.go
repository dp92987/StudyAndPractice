package main

import "fmt"

/// Both goroutines communicate via x variable, which causes race condition.
/// Sync result always will be 0, while async result could differ from 0.
func main() {
	var x int

	for i := 0; i < 1000; i++ {
		incInt(&x)
		decInt(&x)
	}
	fmt.Println("sync result is always 0:", x)

	for i := 0; i < 1000; i++ {
		go incInt(&x)
		go decInt(&x)
	}
	fmt.Println("async result is not always 0:", x)
}

func incInt(x *int) {
	*x++
}

func decInt(x *int) {
	*x--
}
