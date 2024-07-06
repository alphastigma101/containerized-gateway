

func launchTerminal() {
	// Example: Launching a new terminal session (platform-specific)
	var cmd *exec.Cmd
	switch os := runtime.GOOS; os {
	case "windows":
		cmd = exec.Command("cmd", "/c", "start", "http://your-django-app-url")
	case "darwin":
		cmd = exec.Command("open", "-a", "Terminal", "http://your-django-app-url")
	case "linux":
		cmd = exec.Command("xdg-open", "http://your-django-app-url")
	default:
		fmt.Println("Unsupported operating system")
		return
	}

	err := cmd.Start()
	if err != nil {
		fmt.Println("Error launching terminal:", err)
	}
}

