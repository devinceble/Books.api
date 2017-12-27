package main

import "github.com/go-martini/martini"

func main() {
	m := martini.Classic()
	m.Get("/", func() string {
		return "Hello world!"
	})
	m.Get("/Books", func() string {
		return "GET /Books"
	})
	m.Post("/Books", func() string {
		return "Post /Books"
	})
	m.Put("/Books", func() string {
		return "Put /Books"
	})
	m.Delete("/Books", func() string {
		return "Delete /Books"
	})

	m.Run()
}
