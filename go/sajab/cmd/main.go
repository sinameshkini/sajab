package main

import (
	"sajab/cmd/service"
)

func main() {
	if err := service.Run(); err != nil{
		panic(err)
	}
}


