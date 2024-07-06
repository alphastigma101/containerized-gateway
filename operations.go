package operations

import ( 
	"terminal"
	"oath"
	"logging"
)

type Operations interface {
	Terminal
	Logging
	Oath
	update() bool
	insert() bool
	del() bool

}

func update {
 // This function wilil update the user's database 


}

func insert {
 // This function will insert new data into the user's database 
 // Must check and see if the database already exists or not 
}

func del {
	// This function will delete data from the database 
}

