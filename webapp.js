// npm init
const http = require('http');
const fs = require('fs');
const url = require('url');
// const qs = require('querystring');
const path = require('path');
// sudo npm install -S ip
const ip = require('ip');
// sudo npm install -S sanitize-html
const sanitizeHtml = require('sanitize-html');

const hostname = ip.address();
const port = 4000;

const template = require('./template_web.js');

const server = http.createServer( (request, response) => {
    var _url = request.url;
    var queryData = url.parse(_url, true).query;
    var pathname = url.parse(_url, true).pathname;
    // console.log(pathname);

    if(pathname === '/'){
        if(queryData.id === undefined){
            fs.readdir('./database_json', function(error, filelist){
                // console.log(filelist);
                var title = 'Welcome';
                var list = template.List(filelist);
                var html = template.HOME(title, list);
                response.writeHead(200);
                response.end(html);
            });
        } else {
            fs.readdir('./database_json', function(error, filelist){
                // console.log(filelist);
                var filteredId = path.parse(queryData.id).base;
                fs.readFile(`database_json/${filteredId}`, 'utf8', function(err, data){
                    var objData = JSON.parse(data);
                    var title = queryData.id;
                    var sanitizedTitle = sanitizeHtml(title);
                    // var sanitizeData = sanitizeHtml(data, {
                    //     allowedTags:['h1']
                    // });
                    var tweets = template.Tweets(objData)
                    var html = template.HTML(title, tweets,
                        `<h2>${sanitizedTitle}</h2><p>${tweets}</p>`);
                    response.writeHead(200);
                    response.end(html);
                });
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
