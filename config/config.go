package config

import (
	"log"
	"os"

	"github.com/joho/godotenv"
)

func init() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error load .config file!!!")
	}
	PORT := os.Getenv("HTTP_PORT")
	log.Println(PORT)
}
