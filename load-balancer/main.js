const http = require('http');

function createServer(port) {
  http.createServer((req, res) => {
    res.writeHead(200);
    res.end(`Hello, World! from port ${port}`);
  }).listen(port);
}

createServer(8000);
createServer(9000);