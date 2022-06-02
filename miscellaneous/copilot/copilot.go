package main

import (
	"bufio"
	"fmt"
	"os"
)

// encrypts a string using a key
func encrypt(key []byte, message []byte) []byte {
	var cipher []byte
	for i := 0; i < len(message); i++ {
		cipher = append(cipher, message[i]^key[i%len(key)])
	}
	return cipher
}

// reads the first line from a file
// returns a []byte
func readFirstLine(fileName string) []byte {
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
		return nil
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	return scanner.Bytes()
}

// generates a random key
// returns a []byte
func generateKey(n int) []byte {
	var key []byte
	for i := 0; i < n; i++ {
		key = append(key, byte(i))
	}
	return key
}

func main() {
	// the message is the flag
	message := readFirstLine("flag.txt")
	// this is the key
	key := generateKey(len(message))
	// encrypt the message
	cipher := encrypt([]byte(key), []byte(message))
	// print the cipher
	fmt.Println(cipher)
}
