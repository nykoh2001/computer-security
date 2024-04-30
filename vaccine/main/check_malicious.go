package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {
	var filePath string
	fmt.Print("Pleas enter the file name: ")
	fmt.Scanln(&filePath)

	hash, _error := calculateMD5(filePath)
	if _error != nil {
		fmt.Println(_error)
		fmt.Println("Error in calculating MD5 hash")
		return
	}

	found, _error := checkVirusDB(hash)
	if _error != nil {
		fmt.Println(_error)
		fmt.Println("Error in checkVirusDB")
		return
	}

	if found {
		fmt.Println("File in ", filePath, " is malicious.")
	} else {
		fmt.Println("File is safe.")
	}
}

func calculateMD5(filePath string) (string, error) {
	file, _error := os.Open(filePath)
	if _error != nil {
		return "", _error
	}

	defer file.Close()

	hasher := md5.New()
	if _, _error := io.Copy(hasher, file); _error != nil {
		return "", _error
	}
	return hex.EncodeToString(hasher.Sum(nil)), nil
}

func checkVirusDB(hash string) (bool, error) {
	data, _error := os.ReadFile("~/kali/computer_security_6/virus_samples/virus.db")
	if _error != nil {
		return false, _error
	}

	for _, line := range strings.Split(string(data), "\n") {
		if strings.TrimSpace(line) == hash {
			return true, nil
		}
	}
	return false, nil
}
