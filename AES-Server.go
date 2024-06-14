package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"encoding/base64"
	"io"
	"log"
)

func main() {
	originalText := "this is negar honarvar's implementation of AES using GO"
	key := []byte("negarhonarvarsedighianisme------") // 32 bytes for AES-256

	encryptedText, err := encryptText(originalText, key)
	if err != nil {
		log.Fatal(err)
	}

	log.Println("Encrypted:", encryptedText)
}

func encryptText(plaintext string, key []byte) (string, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return "", err
	}

	aesGCM, err := cipher.NewGCM(block)
	if err != nil {
		return "", err
	}

	nonce := make([]byte, aesGCM.NonceSize())
	if _, err = io.ReadFull(rand.Reader, nonce); err != nil {
		return "", err
	}

	ciphertext := aesGCM.Seal(nil, nonce, []byte(plaintext), nil)
	encodedText := base64.StdEncoding.EncodeToString(append(nonce, ciphertext...))
	return encodedText, nil
}
