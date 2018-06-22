const http = require('http');
// sudo npm install -S ip
const ip = require('ip');

const hostname = ip.address();
const port = 4000;

const server = http.createServer((req, res) => {





    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

server.listen(port, () => {
    console.log('icecandy..');
    console.log(`Server running at http://${hostname}:${port}/`);
});
