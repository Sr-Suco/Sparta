var http = require('http');

http.createServer(function(req, res){
        res.end("Bem-vindo ao Servidor Sparta Web criado pelo MRX");
}).listen(8081)

console.log("O servidor está rodando na porta 8081")
