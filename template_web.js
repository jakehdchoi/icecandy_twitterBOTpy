module.exports = {
    HOME: function(title, list, body){
        return `
        <!doctype html>
        <html>
        <head>
          <title>WEB - ${title}</title>
          <meta charset="utf-8">
        </head>
        <body>
          <h1><a href="/">WEB</a></h1>
          ${list}
        </body>
        </html>
        `;
    },
    HTML: function(title, body){
        return `
        <!doctype html>
        <html>
        <head>
          <title>WEB - ${title}</title>
          <meta charset="utf-8">
        </head>
        <body>
          <h1><a href="/">WEB</a></h1>
          ${body}
        </body>
        </html>
        `;
    },
    List: function(filelist){
        var list = '<ul>';
        var i = filelist.length - 1;
        while (i >= 0) {
            list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`
            i = i - 1;
        }
        list = list + '</ul>';
        return list;
    },
    Tweets: function(data){
        var list = '<ul>';
        var i = data.length - 1;
        while (i >= 0) {
            list = list + `<li>${data[i].created_at}</li>`
            i = i - 1;
        }
        list = list + '</ul>';
        return list;
    }
}