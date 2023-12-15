package main

func main() {
	r := routes.InitRouter()
	r.Run(":8080")
}
