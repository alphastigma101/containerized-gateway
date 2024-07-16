package main

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"strings"
)

// Helper function to run shell commands
func runCommand(command string, args ...string) error {
	cmd := exec.Command(command, args...)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	return cmd.Run()
}

// Function to check if a command exists
func commandExists(cmd string) bool {
	_, err := exec.LookPath(cmd)
	return err == nil
}

// Function to get the installation directory based on the OS
func getInstallDir() string {
	switch runtime.GOOS {
	case "windows":
		return `C:\Program Files`
	case "darwin":
		return `/Applications`
	case "linux":
		return `/usr/local`
	default:
		return "./"
	}
}

// Function to install GitHub repository
func installGitHubRepo(repoURL, targetPath string) error {
	if commandExists("git") {
		fmt.Println("Git is already installed.")
	} else {
		return fmt.Errorf("git is not installed")
	}

	// Clone only the main branch to the specified path
	if err := runCommand("git", "clone", "--branch", "main", "--single-branch", repoURL, targetPath); err != nil {
		return fmt.Errorf("failed to clone repository: %v", err)
	}

	// Set the remote URL to read-only
	originalDir, err := os.Getwd()
	if err != nil {
		return fmt.Errorf("failed to get current directory: %v", err)
	}

	if err := os.Chdir(targetPath); err != nil {
		return fmt.Errorf("failed to change directory to repository: %v", err)
	}

	readOnlyURL := strings.Replace(repoURL, "https://", "git://", 1)
	if err := runCommand("git", "remote", "set-url", "origin", readOnlyURL); err != nil {
		return fmt.Errorf("failed to set remote URL to read-only: %v", err)
	}

	if err := os.Chdir(originalDir); err != nil {
		return fmt.Errorf("failed to change back to original directory: %v", err)
	}

	return nil
}

// Function to install Docker
func installDocker() error {
	if commandExists("docker") {
		fmt.Println("Docker is already installed.")
		return nil
	}

	var installCmds []string
	switch runtime.GOOS {
	case "windows":
		installCmds = []string{
			"choco install docker-desktop",
		}
	case "darwin":
		installCmds = []string{
			"brew install --cask docker",
		}
	case "linux":
		installCmds = []string{
			"sudo apt-get update",
			"sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common",
			"curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
			"sudo add-apt-repository \"deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\"",
			"sudo apt-get update",
			"sudo apt-get install -y docker-ce docker-ce-cli containerd.io",
		}
	default:
		return fmt.Errorf("unsupported platform")
	}

	for _, cmd := range installCmds {
		if err := runCommand("sh", "-c", cmd); err != nil {
			return err
		}
	}
	return nil
}

// Function to install Docker Compose
func installDockerCompose() error {
	if commandExists("docker-compose") {
		fmt.Println("Docker Compose is already installed.")
		return nil
	}

	var installCmds []string
	switch runtime.GOOS {
	case "windows":
		installCmds = []string{
			"choco install docker-compose",
		}
	case "darwin":
		installCmds = []string{
			"brew install docker-compose",
		}
	case "linux":
		installCmds = []string{
			"sudo curl -L \"https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose",
			"sudo chmod +x /usr/local/bin/docker-compose",
		}
	default:
		return fmt.Errorf("unsupported platform")
	}

	for _, cmd := range installCmds {
		if err := runCommand("sh", "-c", cmd); err != nil {
			return err
		}
	}
	return nil
}

func main() {
	// Hard-coded GitHub repository URL
	repoURL := "https://github.com/alphastigma101/containerized-gateway.git"
	installDir := getInstallDir()
	targetPath := filepath.Join(installDir, "containerized-gateway")

	fmt.Printf("Installing to %s\n", targetPath)

	fmt.Println("Checking and installing GitHub repository...")
	if err := installGitHubRepo(repoURL, targetPath); err != nil {
		fmt.Printf("Failed to install GitHub repository: %v\n", err)
		return
	}

	fmt.Println("Checking and installing Docker...")
	if err := installDocker(); err != nil {
		fmt.Printf("Failed to install Docker: %v\n", err)
		return
	}

	fmt.Println("Checking and installing Docker Compose...")
	if err := installDockerCompose(); err != nil {
		fmt.Printf("Failed to install Docker Compose: %v\n", err)
		return
	}

	fmt.Println("Installation completed successfully.")
}
