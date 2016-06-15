var express       =   require("express"),
    app           =   express(),
    ruta          =   "proba",
    dostupno      =   true,
    events        =   require("events"),
    wsevent       =   new events.EventEmitter(),
    formidable    =   require("formidable"),
    fs            =   require("fs"),
    io            =   require("socket.io")(),
    odbroj        =   undefined,
    odg           =   true,
    podesavanje   =   require('./proba.json'),
    vreme         =   podesavanje.vreme,
    clientTimeout =   0,
    radi          =   false,
    proc          =   require('child_process'),
    child         =   undefined,
    cookieParser  =   require('cookie-parser'),
    bodyParser    =   require('body-parser'),
    session       =   require('express-session'),
    pwd           =   require('password-hash'),
    ime           =   undefined,
    indeks        =   undefined,
    sw0           =   undefined,
    sw1           =   undefined,
    ssw0          =   0,
    ssw1          =   0;
    var five = require("johnny-five");

app.set('view engine', 'ejs');
app.use('/public',express.static(__dirname + '/public'));
app.use(cookieParser());
app.use(bodyParser.urlencoded({extended:true}));
app.use(session({
	secret: 'WebLabL3L4ExperimentalnaPostavka2MIU',
	resave: true,
	saveUninitialized:true,
	expires: new Date(Date.now() + 3600000)
}));


app.get('/home/:ime/:indeks',function(req,res){
  if (!req.session.auth){
    req.session.auth = true;
    req.session.ime = req.params.ime;
    req.session.indeks = req.params.indeks;
  }
  res.render('desc',require('./langs/srpski.json'));
  delete require.cache[require.resolve('./langs/srpski.json')];
});

app.get('/lab/:id',function(req,res){
  if (req.params.id == ruta){
    res.sendFile(__dirname + "/index3.html");
    wsevent.emit('zauzeto');
  } else {
    res.sendFile(__dirname + "/index2.html");
  }
});
app.post('/lab/upload/:id',function(req,res){
  if (req.params.id == ruta){

    var form = new formidable.IncomingForm();
    form.uploadDir = __dirname + '/script/';
    form.parse(req, function(err, fields, files) {
      res.sendFile(__dirname + "/index3.html");
      odb = true;
      fs.unlinkSync(form.uploadDir  + "program.bit")
      fs.renameSync(files.upload.path, form.uploadDir  + "program.bit");
      if (radi){
        child.kill();
        radi = false;
      };
      ime = req.session.ime;
      indeks = req.session.indeks;
      child = proc.spawn('run.bat');
      radi = 1;
      child.stdout.on('data',function(data){
        console.log(data.toString('utf8'));
      });
      child.stderr.on('data', function(data){
        console.log(data.toString('utf8'));
      });
    });
  } else {
    res.sendFile(__dirname + "/index2.html");
  }
});

// tajmer
function tajmer(){
  clientHomeNamespace.emit('zauzeto', vreme);
  if (odg){
    odg = false;
    clientLabNamespace.emit('Jel si tu?');
    clientTimeout = 0;
  } else {
    clientTimeout++;
    if (clientTimeout == podesavanje.timeout) {
      wsevent.emit('kraj');
      clientTimeout = 0;
    }
  }
  if (!vreme--){
    wsevent.emit('kraj');
  }
  clientLabNamespace.emit('vreme', vreme);
}


//Unutrasnji eventovi u serveru

wsevent.on('kraj', function(){
  vreme = podesavanje.vreme;
  clearInterval(odbroj);
  dostupno = true;
  clientHomeNamespace.emit('slobodno',ruta);
  clientLabNamespace.emit('kraj');
});
wsevent.on('zauzeto', function(){
  dostupno = false;
  if (odbroj){
    clearInterval(odbroj);
  };
  odbroj = setInterval(tajmer, 1000);
})


//Startovanje servera

var server = app.listen(podesavanje.port,function(){
    console.log(":) " + podesavanje.port);
});

// Socket.IO komunikacija
var board = new five.Board();
board.on("ready", function() {
    console.log('Arduino connected');
    sw0 = new five.Led(3);
    sw1 = new five.Led(4);

});

io.listen(server);

var clientLabNamespace = io.of('/client-lab');

clientLabNamespace.on('connection', function(socket){
  odg = true;
  socket.emit('w', 'jeeej :)');
  socket.emit('ssw0', ssw0);
  socket.emit('ssw1', ssw1);
  socket.on('ruta', function(rt){
    ruta = rt;
  });
  socket.on('Jesam', function(){
    odg = true;
  });
  socket.on('sw0', function(){
    if (ssw0){
      sw0.off();
      ssw0 = 0;
    } else {
      sw0.on();
      ssw0 = 1;
    }
  socket.emit('ssw0', ssw0);
  console.log('a');
  })
  socket.on('sw1', function(){
    if (ssw0){
      sw1.off();
      ssw1 = 0;
    } else {
      sw1.on();
      ssw1 = 1;
    }
    socket.emit('ssw1', ssw1);
    console.log('b');
  })
});

var clientHomeNamespace = io.of('/client-home');

clientHomeNamespace.on('connection',function(socket){
  if (dostupno){
    clientHomeNamespace.emit('slobodno',ruta);
  }
})
