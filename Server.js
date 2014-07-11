var http = require('http');
var fs = require('fs');
function readFile(path, callback) {
	path = path + "/index.html";
	fs.readFile(path, function (err, data) {
		callback.apply(null, [err, data]);
	});
}

http.createServer(function (req, res) {
  var url = req.headers.host.split('.');
  var filePath = "";
  if(url.length >= 2 && url[0] == "www") {
	filePath = url[1];
  } else {
	filePath = url[0];
  }
  readFile(filePath, function(err, data) {
	if(err) {
		console.log(err);
		res.writeHead(500, {'Content-Type': 'text/plain'});
		res.end('Something is wrong\n');
		return;
	}  
	res.writeHead(200, {'Content-Type': 'text/html'});
    res.end(data);
  });


  
}).listen(80, '127.0.0.1');
console.log('Server running at http://127.0.0.1:80/');
