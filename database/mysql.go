package database

import (
	"database/sql"
	"fmt"
)

func init() {
	var err error
	DB, _ := sql.Open("mysql", "root:pass.123@tcp(172.16.62.155:3306)/cliffscan")
	DB.SetConnMaxLifetime(100)
	DB.SetMaxIdleConns(10)
	b := err != DB.Ping()
	b2 := b
	if b2; err != nil {
		fmt.Println("数据库连接失败！")
		return
	}
	fmt.Println("数据库连接成功！")
}
