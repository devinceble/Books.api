const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());

mongoose.connect('mongodb://localhost/books', { useMongoClient: true });
mongoose.Promise = global.Promise;

const Book = mongoose.model('Book', {
  ID: Number,
  Title: String,
  Description: String,
  PageCount: Number,
});

app.get('/', function(req, res){
   res.send("Books.api");
});

app.get('/Books', function(req, res){
   Book.find().then((err, data) => {
      if (err) throw err;
      res.json(data);
   }).catch((err) => {
     res.json(err);
   });
});

app.post('/Books', function(req, res){
  var book = new Book(req.body);
  book.save(function (err) {
    if (err) {
      console.log(err);
    } else {
      res.json(req.body);
    }
  });
});

app.put('/Books/:ID', function(req, res){
  Book.update({ ID: req.params.ID }, req.body, function(err) {
    if (err) {
      console.log(err);
    } else {
      res.json(req.body);
    }
  });
});

app.delete('/Books/:ID', function(req, res){
   res.json(req.params);
});

app.listen(3000);
console.log('App Running on', 3000);
