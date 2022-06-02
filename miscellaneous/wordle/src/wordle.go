package main

import (
	"bufio"
	"bytes"
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"strings"
	"time"
)

func isIn(val string, slice []string) bool {
	for _, item := range slice {
		if item == val {
			return true
		}
	}
	return false
}

// Counter

type counter struct {
	mapping map[byte]int
}

func newCounter() *counter {
	c := &counter{
		mapping: map[byte]int{},
	}
	return c
}

func (c *counter) add(item byte) {
	if count, ok := c.mapping[item]; ok {
		c.mapping[item] = count + 1
	} else {
		c.mapping[item] = 1
	}
}

func (c *counter) subtract(item byte) {
	if count, ok := c.mapping[item]; ok {
		c.mapping[item] = count - 1
	} else {
		c.mapping[item] = -1
	}
}

func (c *counter) get(item byte) int {
	if count, ok := c.mapping[item]; ok {
		return count
	} else {
		return 0
	}
}

// Guess

type guess struct {
	userGuess string
	status    []byte
}

func newGuess(userGuess string, real string) *guess {
	letterCounter := newCounter()
	for i := 0; i < len(real); i++ {
		r := real[i]
		letterCounter.add(r)
	}

	status := []byte("xxxxx")

	for i := 0; i < len(userGuess); i++ {
		g := userGuess[i]
		r := real[i]
		if g == r {
			letterCounter.subtract(g)
			status[i] = 'g'
		}
	}

	for i := 0; i < len(userGuess); i++ {
		if status[i] == 'x' {
			g := userGuess[i]
			if letterCounter.get(g) > 0 {
				letterCounter.subtract(g)
				status[i] = 'y'
			}
		}
	}

	g := &guess{
		userGuess: userGuess,
		status:    status,
	}

	return g
}

func (g *guess) toString() string {
	result := ""
	colorMap := map[byte]string{
		'x': "\033[91m",
		'y': "\033[93m",
		'g': "\033[92m",
	}
	for i := 0; i < len(g.userGuess); i++ {
		if color, ok := colorMap[g.status[i]]; ok {
			result += color
		}
		result += string(g.userGuess[i]) + "\033[00m"
	}
	return result
}

// Wordle

type wordle struct {
	largeDictionary []string
	smallDictionary []string
	flag            string
	word            string
	userWord        string
	previousGuesses []guess
	validationError string
	isRunning       bool
	isWon           bool
	tries           int
}

func (w *wordle) chooseWord() {
	n := rand.Intn(len(w.smallDictionary))
	w.word = w.smallDictionary[n]
}

func (w *wordle) loop() {
	w.input()
	w.calculate()
	w.draw()
}

func (w *wordle) input() {
	w.userInput()
}

func (w *wordle) calculate() {
	w.clearError()
	w.validateGuess()
	w.evaluateGuess()
	w.determineTries()
}

func (w *wordle) draw() {
	w.clearScreen()
	w.drawTitle()
	w.drawGuesses()
	w.drawTriesLeft()
	w.drawWin()
	w.drawError()
}

func (w *wordle) userInput() {
	fmt.Print(">>> ")
	var input string
	fmt.Scanln(&input)
	w.userWord = string(input)
	w.userWord = strings.ToLower(w.userWord)
	w.userWord = strings.Trim(w.userWord, " \n")
	fmt.Println(w.userWord)
}

func (w *wordle) clearError() {
	w.validationError = ""
}

func (w *wordle) validateGuess() {
	if !isIn(w.userWord, w.largeDictionary) {
		w.validationError = w.userWord + ": Not a valid word"
	}
}

func (w *wordle) evaluateGuess() {
	if w.validationError != "" {
		return
	}
	w.previousGuesses = append(w.previousGuesses, *newGuess(w.userWord, w.word))
	if w.userWord == w.word {
		w.isWon = true
		w.isRunning = false
	}
}

func (w *wordle) determineTries() {
	if len(w.previousGuesses) == w.tries {
		w.isRunning = false
	}
}

func (w *wordle) clearScreen() {
	fmt.Printf("\033[2J\033[H")
}

func (w *wordle) drawTitle() {
	fmt.Println("WORDLE\n")
}

func (w *wordle) drawGuesses() {
	for _, guess := range w.previousGuesses {
		fmt.Println(guess.toString())
	}
}

func (w *wordle) drawTriesLeft() {
	for i := 0; i < w.tries-len(w.previousGuesses); i++ {
		fmt.Println("_____")
	}
}

func (w *wordle) drawWin() {
	if w.isWon {
		fmt.Println(w.flag)
	} else if !w.isRunning {
		fmt.Printf("The word was %s\n", w.word)
	}
}

func (w *wordle) drawError() {
	if w.validationError != "" {
		fmt.Println(w.validationError)
	}
}

func (w *wordle) run() {
	w.isRunning = true
	w.draw()
	for w.isRunning {
		w.loop()
	}
}

func readFlag() string {
	flag_file, _ := os.Open("flag.txt")
	defer flag_file.Close()

	scanner := bufio.NewScanner(flag_file)
	scanner.Scan()
	flag := scanner.Text()
	return flag
}

func readWholeFile(filename string) []string {
	file, _ := ioutil.ReadFile(filename)
	result := []string{}
	for _, line := range bytes.Split(file, []byte("\n")) {
		result = append(result, string(line))
	}
	return result
}

func newWordle() *wordle {
	w := &wordle{
		flag:            readWholeFile("flag.txt")[0],
		largeDictionary: readWholeFile("large.txt"),
		smallDictionary: readWholeFile("small.txt"),
		word:            "",
		userWord:        "",
		previousGuesses: make([]guess, 0),
		validationError: "",
		isRunning:       false,
		isWon:           false,
		tries:           6,
	}
	w.chooseWord()
	return w
}

func main() {
	rand.Seed(time.Now().Unix())
	w := newWordle()
	w.run()
}
