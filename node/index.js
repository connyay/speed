'use strict';
var express = require('express');
var app = express();

app.get('/', function (req, res) {
  return res.send('lub dub');
});

var server = app.listen(9999, function () {
  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);
});
