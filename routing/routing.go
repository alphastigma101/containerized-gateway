package operations

import (
	"fmt"
	"terminal"
	"oath"
	"logging"
)

type Routing interface {
	terminal.Terminal
	logging.Logging
	oath.Oath
	update() bool
	insert() bool
	del() bool

}

func update {
 // This function wilil update the user's database
 fmt.Println("Hello, World!")
	return false;
}

func insert {
 // This function will insert new data into the user's database 
 // Must check and see if the database already exists or not 
 return false;
}

func del {
	// This function will delete data from the database 

	return false;
}

