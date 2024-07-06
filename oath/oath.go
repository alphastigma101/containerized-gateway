package oath

import (
	"fmt"
)

type Oath interface {
	isAuthenticated() bool
	checkCredentials() bool
}

func isAuthenticated() {
	fmt.Println("Caled isAuthenticated!")
	return false
}

func checkCredentials() {
	fmt.Println("Called checkCredentials")
	return false
}

