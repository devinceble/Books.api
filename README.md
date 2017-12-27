## Introduction to cross platform native mobile app using React Native API

*** Install MongoDB: https://goo.gl/xEotYP ***
*** Source Code: https://git.io/vbiLi ***
*** App Source Code: https://goo.gl/dcJszC ***

## Using API
---

### golang
```bash
cd go
# bash set GOPATH
$ export $GOPATH=$(pwd)
# install dependencies
$ go get gopkg.in/mgo.v2
$ go get github.com/go-martini/martini
$ go get github.com/martini-contrib/binding
# run martini
$ go run main.go
```
---

### python
```bash
$ cd python
# Use python pip to install requirements
$ pip install -r requirements.txt
# export FLASK_APP env
$ export FLASK_APP=main.py
# run flask
$ flask run --port=3000
```
---

### ruby
```bash
$ cd ruby
# use gem to install bundler
$ sudo gem install bundler
# use bundler to install dependencies
$ bundle install --path vendor/bundle
# run sinatra
$ bundle exec ruby main.rb
```
---

### node
```bash
$ cd node
# use yarn or npm to install packages
$ yarn install
# run express
$ node index.js
```
---
