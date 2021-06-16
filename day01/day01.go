package main

import "fmt"

func sum_up_k(myArray []int, k int) bool {

	for i := 0; i < len(myArray)-1; i++ {
		for j := 1; j < len(myArray); j++ {
			if i != j {
				if myArray[i]+myArray[j] == k {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	arrayTest := []int{10, 15, 3, 7}
	k := 17

	fmt.Println(sum_up_k(arrayTest, k))
}
