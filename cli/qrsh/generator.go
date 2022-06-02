package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strings"

	qrcode "github.com/skip2/go-qrcode"
)

// generate a qr code from a string
func generateQRFromString(s string) {
	qrcode.WriteFile(s, qrcode.Low, 1, "/home/qr/qr.png")
}

// run a command and return the output
// return []byte
func runCommand(command []string) string {
	// run the command
	output, err := exec.Command(command[0], command[1:]...).Output()
	if err != nil {
		return err.Error()
	}
	return string(output)
}

// get one line of user input
// return string
func getInput() string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("user@host:~$ ")
	text, _ := reader.ReadString('\n')
	return text
}

func main() {
	os.Clearenv()
	os.Setenv("PATH", "/bin")
	for {
		// get user input
		s := getInput()

		// run command
		output := runCommand(strings.Fields(s))

		// generate qr code
		generateQRFromString(output)

		// convert to xxd
		xxd_output := runCommand([]string{"xxd", "/home/qr/qr.png"})
		fmt.Println(xxd_output)
	}
}
