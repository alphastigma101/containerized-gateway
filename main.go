package main


//TODO: Make a class that here that inherits from operations
// What it is going to look like if go supports classes:
// operations -> Oath -> Logging -> Terminal
// Name of the class here should be called Main
import (
	"fmt"
	"io/ioutil"
	"net/http" // Same thing as the request library in python
	"os"
	"os/exec" // Required for launching terminal
	"operations"
)
func prompt() {
	// This function will ask the user for the name of the file 
	// It will determine if it is a .csv or .jsnol, or json file 
	// If it is either of them, log the error and return or exit

}
func main() {
	root := "http://your-django-app-api-endpoint-url/data"

	req, err := http.NewRequest("GET", root, nil)
	if err != nil {
		fmt.Println("Error creating request:", err)
		os.Exit(1)
	}

	
	Data := prompt() // Implement a function to prompt user for JSON data

	// Optional: Send HTTP request with JSON payload
	// req, err = http.NewRequest("POST", root, bytes.NewBuffer([]byte(jsonData)))
	// req.Header.Set("Content-Type", "application/json")

	// Send HTTP request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Println("Error sending request:", err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	// Read response body
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("Error reading response:", err)
		os.Exit(1)
	}

	// Print response body
	fmt.Println("Response from Django app API:")
	fmt.Println(string(body))

	// Launch a terminal connected to the Django app
	launchTerminal()
}


