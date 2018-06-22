const http = require('http');
const fs = require('fs');
const url = require('url');
const qs = require('querystring');
const path = require('path');
// sudo npm install -S ip
const ip = require('ip');

const hostname = ip.address();
const port = 4000;

const template = require('./web_template.js');

const server = http.createServer( (request, response) => {
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;
    console.log(pathname);

    if(pathname === '/'){
        if(queryData.id === undefined){
            fs.readdir('./database_json', function(error, filelist){
                // console.log(filelist);
                var title = 'Welcome';
                var list = template.List(filelist);
                var html = template.HTML(title, list);
                response.writeHead(200);
                response.end(html);
            });
        }
    } else {
        response.writeHead(404);
        response.end('Not found');
    }
});

server.listen(port, () => {
    console.log('icecandy..');
    console.log(`Server running at http://${hostname}:${port}/`);
});
