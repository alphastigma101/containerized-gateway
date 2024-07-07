package oath

import (
	"fmt"
)

func IsAuthenticated() bool {
	fmt.Println("Caled isAuthenticated!")
	return false
}

func CheckCredentials() bool {
	fmt.Println("Called checkCredentials")
	return false
}

