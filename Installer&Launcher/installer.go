package installer

import (
    "fmt"
    "os"
    "os/exec"
    "path/filepath"
    "runtime"
    "strings"

    "fyne.io/fyne/v2"
    "fyne.io/fyne/v2/app"
    "fyne.io/fyne/v2/container"
    "fyne.io/fyne/v2/dialog"
    "fyne.io/fyne/v2/widget"
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

// Function to install GitHub repository
func installGitHubRepo(repoURL string) error {
    if commandExists("git") {
        fmt.Println("Git is already installed.")
    } else {
        fmt.Println("Git is not installed. Please install Git before proceeding.")
        return fmt.Errorf("git not installed")
    }

    // Clone the repository
    fmt.Println("Downloading the files...")
	if err := runCommand("git", "clone", "--branch", "main", "--single-branch", repoURL); err != nil {
        return fmt.Errorf("failed to clone repository: %v", err)
    }

    // Set the remote URL to read-only
    repoName := getRepoNameFromURL(repoURL)
    if err := os.Chdir(repoName); err != nil {
        return fmt.Errorf("failed to change directory to repository: %v", err)
    }

    readOnlyURL := getReadOnlyURL(repoURL)
    if err := runCommand("git", "remote", "set-url", "origin", readOnlyURL); err != nil {
        return fmt.Errorf("failed to set remote URL to read-only: %v", err)
    }

    return nil
}

// Function to extract the repository name from the URL
func getRepoNameFromURL(url string) string {
    parts := strings.Split(url, "/")
    return strings.TrimSuffix(parts[len(parts)-1], ".git")
}

// Function to get the read-only URL for a GitHub repository
func getReadOnlyURL(url string) string {
    return strings.Replace(url, "https://", "git://", 1)
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
    a := app.New()
    w := a.NewWindow("Installer")

    repoURL := "https://github.com/alphastigma101/containerized-gateway.git"
    targetPath := widget.NewEntry()
    targetPath.SetPlaceHolder("Choose installation path...")

    choosePathButton := widget.NewButton("Choose Path", func() {
        dialog.ShowFolderOpen(func(uri fyne.ListableURI, err error) {
            if uri != nil {
                targetPath.SetText(uri.Path())
            }
        }, w)
    })

    installButton := widget.NewButton("Install", func() {
        path := targetPath.Text
        if path == "" {
            dialog.ShowInformation("Error", "Please choose a valid path", w)
            return
        }

        fmt.Println("Checking and installing GitHub repository...")
        if err := installGitHubRepo(repoURL, path); err != nil {
            dialog.ShowInformation("Error", fmt.Sprintf("Failed to install GitHub repository: %v", err), w)
            return
        }

        fmt.Println("Checking and installing Docker...")
        if err := installDocker(); err != nil {
            dialog.ShowInformation("Error", fmt.Sprintf("Failed to install Docker: %v", err), w)
            return
        }

        fmt.Println("Checking and installing Docker Compose...")
        if err := installDockerCompose(); err != nil {
            dialog.ShowInformation("Error", fmt.Sprintf("Failed to install Docker Compose: %v", err), w)
            return
        }

        dialog.ShowInformation("Success", "Installation completed successfully.", w)
    })

    w.SetContent(container.NewVBox(
        targetPath,
        choosePathButton,
        installButton,
    ))

    w.ShowAndRun()
}