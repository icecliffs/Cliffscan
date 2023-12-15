package routes

import (
	"cliffscan/app/Controller"

	"github.com/gin-gonic/gin"
)

func InitRouter() *gin.Engine {
	r := gin.Default()
	r.Static("/public", "./public")
	r.LoadHTMLGlob("views/**/*")

	r.GET("/", Controller.Home)

	//v1:=r.Group("/api"){
	//v1.GET("/ping", Controller.Ping)
	//}

	return r
}
