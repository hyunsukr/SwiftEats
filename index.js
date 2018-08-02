var http = require('http');
var fs = require('fs');
var dt = require('./timemodule.js');
var path = require('path');
//var formidable = require('formidable');
//var nodemailer = require('nodemailer');
http.createServer(function (req, res) {
  if (!req.url.includes('.js') && !req.url.includes('.css') && !req.url.includes('.jpg') && !req.url.includes('.png')) {
    console.log(req.url + "this is the req.url");
    if (req.url == '/') {
      fs.readFile('home.html', function(err, data) {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write(data);
        res.end();
      });
    }
    else if (req.url == '/breakfast') {
        fs.readFile('interfacebreak.html', function(err, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            res.end();
          });
    
    }
    else if (req.url =='/about'){
         fs.readFile('about.html',function(err,data){
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            res.write('</div>');
            footbot(res);
            res.end();
         });
    }
    else if (req.url == '/Register') {
        fs.readFile('register.html', function(err, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            res.write('<div class="container">');
            res.write('<div class="container">');
            res.write('<form name="makeuser" method="post" action="/createduser" >');
            res.write('Username: <input type="text" class="form-control" name = "Username" id="Username" placeholder="" required="required">');
            res.write('Password: <input type="password" class="form-control" name="Password" id="password" placeholder="" pattern=".{8,}"   required title="8 characters minimum" required="required">');
            res.write('Reenter Password: <input type="password" class="form-control" pattern=".{8,}"   required title="8 characters minimum"  name = "RePassword" id="RePassword" placeholder="" required="required">');
            res.write('Email: <input type="text" class="form-control" name = "Email" id="Email" placeholder="" required="required">');
            res.write('Phonenumber: <input type="text" class="form-control" name = "Phonenumber" id="Username" placeholder="" required="required">');
            res.write('CreditCard: <input type="text" class="form-control" name = "Creditcard" id="Username" placeholder="" required="required">');
            res.write('ccv: <input type="text" class="form-control" name = "ccv" id="ccv" placeholder="" required="required">');
            res.write('zip: <input type="text" class="form-control" name = "zip" id="zip" placeholder="" required="required">');
            res.write('Firstname: <input type="text" class="form-control" name = "Firstname" id="Username" placeholder="" required="required">');
            res.write('Lastname: <input type="text" class="form-control" name = "Lastname" id="Username" placeholder="" required="required">');
            res.write('</br><button type="submit" value="Submit" class="btn btn-primary">Submit</button>');
            res.write('</form>');
            res.write('<form action="/" method="post">')
            res.write('</br><button type="submit" id="newuser" class="btn btn-danger">Go Back to Log in</button>');
            res.write('</form>');
            res.write('</div>');
            res.write('</div>');
            res.write('</div>');
            res.write('</body>');
            res.end();
        });
    }
    else if (req.url =='/createduser') {
        var body = '';
        req.on('data', function(chunk) {
            body += chunk;
        });
        req.on('end', function() {
            var username = body.split('Username=')[1].split('&Password=')[0];
            var password = body.split('Password=')[1].split('&Re')[0];
            var repass = body.split('RePassword=')[1].split('&Email=')[0];
            var username = body.split('Username=')[1].split('&Password=')[0];
            var password = body.split('Password=')[1].split('&Re')[0];
            var repass = body.split('RePassword=')[1].split('&Email=')[0];
            var email = body.split('Email=')[1].split('&Phonenumber=')[0];
            var phonenumber = body.split('Phonenumber=')[1].split('&Creditcard')[0];
            var credicard = body.split('Creditcard=')[1].split('&ccv')[0];
            var ccv = body.split('ccv=')[1].split('&zip')[0];
            var zip = body.split('zip=')[1].split('&Firstname')[0];
            var firstname = body.split('Firstname=')[1].split('&Lastname')[0];
            var lastname = body.split('Lastname=')[1];
            if (password.trim() != repass.trim()) {
                fs.readFile('register.html', function(err, data) {
                    res.writeHead(200, {'Content-Type': 'text/html'});
                    res.write(data);
                    res.write('<div class="container">');
                    res.write('<div class="alert alert-danger">');
                    res.write('<strong>ERROR!</strong> Passwords Do Not Match');
                    res.write('</div>');
                    res.write('<div class="container col-lg-4">');
                    res.write('<form name="makeuser" method="post" action="/createduser" >');
                    res.write('Username: <input type="text" class="form-control" name = "Username" id="Username" placeholder="" required="required">');
                    res.write('Password: <input type="password" class="form-control" name="Password" id="password" placeholder="" pattern=".{8,}"   required title="8 characters minimum" required="required">');
                    res.write('Re-enter Password: <input type="password" class="form-control" pattern=".{8,}"   required title="8 characters minimum"  name = "RePassword" id="RePassword" placeholder="" required="required">');
                    res.write('Email: <input type="text" class="form-control" name = "Email" id="Email" placeholder="" required="required">');
                    res.write('Phone number: <input type="text" class="form-control" name = "Phonenumber" id="Username" placeholder="" required="required">');
                    res.write('Credit Card: <input type="text" class="form-control" name = "Creditcard" id="Username" placeholder="" required="required">');
                    res.write('ccv: <input type="text" class="form-control" name = "ccv" id="ccv" placeholder="" required="required">');
                    res.write('zip: <input type="text" class="form-control" name = "zip" id="zip" placeholder="" required="required">');
                    res.write('Firstname: <input type="text" class="form-control" name = "Firstname" id="Username" placeholder="" required="required">');
                    res.write('Lastname: <input type="text" class="form-control" name = "Lastname" id="Username" placeholder="" required="required">');
                    res.write('</br><button type="submit" value="Submit" class="btn btn-primary">Submit</button>');
                    res.write('</form>');
                   
                    res.write('<form action="/" method="post">')
                    res.write('</br><button type="submit" id="newuser" class="btn btn-danger">Go Back to Log in</button>');
                    res.write('</form>');
                    res.write('</div>');
                    res.write('</div>');
                    res.write('</body>');
                    res.end();
                });
            }
            else {
                var spawn = require("child_process").spawn;
                var pyFile = 'insert_users.py';
                const pyspawn = spawn('python', [pyFile, username, password, email, phonenumber, credicard, ccv, firstname, lastname, zip]);
                pyspawn.stdout.on('data', (data) => {
                    console.log(`stdout: ${data}`);
                    var str = String.fromCharCode.apply(null, data);
                    if (str.trim() == "False".trim()) {
                        fs.readFile('register.html', function(err, data) {
                            res.writeHead(200, {'Content-Type': 'text/html'});
                            res.write(data);
                            res.write('<div class="container">');
                            res.write('<div class="alert alert-danger">');
                            res.write('<strong>ERROR!</strong> Username Taken');
                            res.write('</div>');
                            res.write('<form name="makeuser" method="post" action="/createduser" >');
                            res.write('Username: <input type="text" class="form-control" name = "Username" id="Username" placeholder="" required="required">');
                            res.write('Password: <input type="password" class="form-control" name="Password" id="password" placeholder="" pattern=".{8,}"   required title="8 characters minimum" required="required">');
                            res.write('Reenter Password: <input type="password" class="form-control" pattern=".{8,}"   required title="8 characters minimum"  name = "RePassword" id="RePassword" placeholder="" required="required">');
                            res.write('Email: <input type="text" class="form-control" name = "Email" id="Email" placeholder="" required="required">');
                            res.write('Phonenumber: <input type="text" class="form-control" name = "Phonenumber" id="Username" placeholder="" required="required">');
                            res.write('CreditCard: <input type="text" class="form-control" name = "Creditcard" id="Username" placeholder="" required="required">');
                            res.write('ccv: <input type="text" class="form-control" name = "ccv" id="ccv" placeholder="" required="required">');
                            res.write('zip: <input type="text" class="form-control" name = "zip" id="zip" placeholder="" required="required">');
                            res.write('Firstname: <input type="text" class="form-control" name = "Firstname" id="Username" placeholder="" required="required">');
                            res.write('Lastname: <input type="text" class="form-control" name = "Lastname" id="Username" placeholder="" required="required">');
                            res.write('</br><button type="submit" value="Submit" class="btn btn-primary">Submit</button>');
                            res.write('</form>');
                            res.write('<form action="/" method="post">')
                            res.write('</br><button type="submit" id="newuser" class="btn btn-danger">Go Back to Log in</button>');
                            res.write('</form>');
                            res.write('</div>');
                            res.write('</div>');
                            res.write('</body>');
                            res.end();
                        });
                    }
                    else if (str.trim() == "made".trim()) {
                        fs.readFile('register.html', function(err, data) {
                            res.writeHead(200, {'Content-Type': 'text/html'});
                            res.write(data);
                            res.write('<div class="container">');
                            res.write("<div class='alert alert-success'>");
                            res.write('<strong>Success!</strong>');
                            res.write('</div>');
                            res.write('</div>');
                            res.write('</div>');
                            res.write('</body>');
                            res.end();
                        });
                    }
                    else {
                        res.write(str);
                        res.end();
                    }
                });
                pyspawn.stderr.on('data', (data) => {
                    console.log(`stderr: ${data}`);
                });
                pyspawn.on('close', (code) => {
                    console.log(`child process exited with code ${code}`);
                });
            }
         });
    }
    else if (req.url =='/orderprocess') {
        var body = '';
        req.on('data', function(chunk) {
            body += chunk;
        });
        req.on('end', function() {
            var items = body.split('&Username=')[0]
            var username = body.split('Username=')[1].split('&Password')[0]
            var password = body.split('Password=')[1]
            var spawn = require("child_process").spawn;
            var pyFile = 'find_users.py';
            const pyspawn = spawn('python', [pyFile, username, password]);
            pyspawn.stdout.on('data', (data) => {
                console.log(`stdout: ${data}`);
                var str = String.fromCharCode.apply(null, data);
                if (str.trim() == "loggedin".trim()) {
                    fs.readFile('home.html', function(err, data) {
                        res.writeHead(200, {'Content-Type': 'text/html'});
                        res.write(data);
                        res.write('<div class="container">');
                        res.write("<div class='alert alert-success'>");
                        res.write('<strong>Order Made!</strong>');
                        res.write('</div>');
                        res.write('<div>');
                        res.write('</body>');
                        res.end();
                    });
                    var spawn1 = require("child_process").spawn;
                    var pyFile = 'send_notification.py';
                    const pyspawn = spawn1('python', [pyFile, username, items]);
                    pyspawn.stdout.on('data', (data) => {
                        console.log(`stdout: ${data}`);
                    });
                    pyspawn.stderr.on('data', (data) => {
                        console.log(`stderr: ${data}`);
                    });
                    pyspawn.on('close', (code) => {
                        console.log(`child process exited with code ${code}`);
                    });
                }
                else if (str.trim() == "Notlogged".trim()) {
                    fs.readFile('home.html', function(err, data) {
                        res.writeHead(200, {'Content-Type': 'text/html'});
                        res.write(data);
                        res.write('<div class="container">');
                        res.write("<div class='alert alert-success'>");
                        res.write('<strong>Success!</strong>');
                        res.write('</div>');
                        res.write('</body>');
                        res.end();
                    });
                }
            });
            pyspawn.stderr.on('data', (data) => {
                console.log(`stderr: ${data}`);
            });
            pyspawn.on('close', (code) => {
                console.log(`child process exited with code ${code}`);
            });
        });
    }
    else if (req.url == '/lunch') {
        if (dt.myDateTime().split(' ')[1] == 'Jan') {
            var num = '01';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Feb') {
            var num = '02';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Mar') {
            var num = '03';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Apr') {
            var num = '04';
        }
        else if (dt.myDateTime().split(' ')[1] == 'May') {
            var num = '05';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Jun') {
            var num = '06';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Jul') {
            var num = '07';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Aug') {
            var num = '08';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Sep') {
            var num = '09';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Oct') {
            var num = '10';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Nov') {
            var num = '11';
        }
        else if (dt.myDateTime().split(' ')[1] == 'Dec') {
            var num = '12';
        }
        var date = dt.myDateTime().split(' ')[3] + '-' + num + '-' + dt.myDateTime().split(' ')[2];
        fs.readFile('interfacelunch.html', function(err, data) {
            res.writeHead(200, {'Content-Type': 'text/html'});
            res.write(data);
            var spawn = require("child_process").spawn;
            var pyFile = 'today_menu.py';
            const pyspawn = spawn('python', [pyFile, date]);
            pyspawn.stdout.on('data', (data) => {
                console.log(`stdout: ${data}`);
                //res.write('<form name="validation" method="post" action="/answers">');
                //res.write(data);
                var arr = String(data).split('),')
                //res.write('<form name="order" method="post" action="/orderprocess">');
               /* res.write('<table class="table table-hover table-bordered table-condensed">');
                res.write('<thead>');
                res.write('<tr class="success">');
                res.write('<th scope="col">Item</th>');
                res.write('<th scope="col">Description</th>');
                res.write('<th scope="col">Selection</th>');
                res.write('</tr>');
                res.write('<tbody>');
                */
                //res.write('<tr> <td> <span style="color:#FF0000"> Daily Specials </span></td> </tr>');
            
                
                for (var i = 0; i<arr.length; i++) {
                    var time = "Approx wait time: " + arr[i].split(", u'")[4].split("', ")[1] + " min" + '</br>';
                    var name = arr[i].split(", u'")[1].split("',")[0] + '</br>';
                    var calories = arr[i].split(", u'")[1].split("',")[1] + ' calories' + '</br>';
                    var ingredients = arr[i].split(", u'")[2].split("',")[0] + "</br>";
                    var price = '$'+ arr[i].split(", u'")[2].split("',")[1];
                    if (price.length == 5) {
                        price = price + '0'
                    }
                    else if (price.length == 2) {
                        price = price + '0'
                    }
                    
                    var picture = arr[i].split(", u'")[3].split("'")[0];
                    if (i == 3) {
                        res.write('<div class="container">')
                        res.write('<form name="order" method="post" action="/orderprocess">');
                        res.write('<table class="table table-hover table-bordered table-condensed">');
                        res.write('<thead>');
                        res.write('<tr class="success">');
                        res.write('<th scope="col">Item</th>');
                        res.write('<th scope="col">Description</th>');
                        res.write('<th scope="col">Selection</th>');
                        res.write('</tr>');
                        res.write('<tbody>');
                        res.write('<tr> <td> <span style="color:#FF0000"> Constant Menu </span></td> </tr>');
                        res.write('<tr>');
                        res.write('<td>' + '<img src = "/pics/foodpic/' + picture + '" class="rounded float-right" style="width:200px;height:200px;"alt="">' + '</td>');
                        res.write('<td>' + name + calories + ingredients + price + '</br>' + time + '</td>');
                        //res.write('<td>' + picture + '</td>');
                        res.write('<td> <input type="checkbox"  name="item' + name + '" value="selected"/></td></tr>');
                    }
                    else if (i == 1 || i == 2 || i == 0) {
        /*
                       res.write('<tr>');
                        res.write('<td>' + '<img src = "/pics/foodpic/' + picture + '" class="rounded float-right" style="width:200px;height:200px;"alt="">'  + '</td>');
                        res.write('<td>' + name + calories + ingredients + price + '</td>');
                        res.write('<td> <input type="checkbox" name="item' + name + '" value="selected" disabled/></td></tr>');
                    */
                        if(i == 0){
                            res.write('<div class="container">');
                            res.write('<div id="myCarousel" class="carousel slide" data-ride="carousel">');
                            res.write('<ol class="carousel-indicators">');
                            res.write('<li data-target="#myCarousel" data-slide-to="0" class="active"></li>');
                            res.write('<li data-target="#myCarousel" data-slide-to="1"></li>');
                            res.write('<li data-target="#myCarousel" data-slide-to="2"></li>');
                            res.write(' </ol>');
                            res.write('<div class="carousel-inner">');
                            res.write('<div class="carousel-item active">');
                            res.write('<img class="first-slide" align="center" src = "pics/foodpic/'+ picture +'" height="400px" width="100%" padding-left= "200px"; alt="First slide">');
                            res.write('<div class="container">');
                            res.write('<div class="carousel-caption text-left">');
                            res.write("<font color='#514c4c'</font><h1>Today\'s Entrees</h1><p>"+ name +"</p>");
                            res.write('</div></div></div>');
                        }
                        else if (i==1){
                            res.write('<div class="carousel-item"><img class="second-slide" src="pics/foodpic/Seared-Cajun-Tilapia-Fish.jpg" height="400px" width="100%" alt="Second slide"><div class="container"><div class="carousel-caption text-left "><font color="#fff"</font><h1>Today\'s Entrees</h1><p>Seared Cajun Tilapia Fish</p></div></div></div>');
                            res.write('<div class="carousel-item"><img class="third-slide" src="pics/foodpic/Cabbage-Chick-Pea-Stew.jpg" height="400px" width="100%" alt="Third slide"><div class="container"><div class="carousel-caption text-left"><font color="#fff"</font><h1>Today\'s Entrees</h1><p>Green Cabbage with Chick pea Stew</p></div></div></div></div><a class="carousel-control-prev" href="#myCarousel" role="button" data-slide="prev"><span class="carousel-control-prev-icon" aria-hidden="true"></span><span class="sr-only">Previous</span></a><a class="carousel-control-next" href="#myCarousel" role="button" data-slide="next"><span class="carousel-control-next-icon" aria-hidden="true"></span><span class="sr-only">Next</span></a></div>');
                        }
                        else if(i==2){
                            res.write('</div></div></div></div>');
                        }
                    }
                         else {
                        res.write('<tr>');
                        res.write('<td>' + '<img src = "/pics/foodpic/' + picture + '" class="rounded float-right" style="width:200px;height:200px;"alt="">'  + '</td>');
                        res.write('<td>' + name + calories + ingredients + price + '</br>' + time + '</td>');
                        res.write('<td> <input type="checkbox" name="item' + name + '" value="selected"/></td></tr>');
                }
            }
                    
                res.write('</tbody></table></br>');
                res.write('Username: <input type="text" class="form-control" name = "Username" id="Username" placeholder="Username" required="required">');
                res.write('Password: <input type="password" class="form-control" pattern=".{8,}"   required title="8 characters minimum" name = "Password" id="Password" placeholder="Password" required="required">');
                res.write('</br><button type="submit" value="Submit" class="btn btn-primary">Submit</button>');
                res.write('</form>');

                res.write('<form action="/Register" method="post">')
                res.write('</br><button type="submit" id="newuser" class="btn btn-danger">New User?</button>');
                res.write('</div>');
                footbot(res);
                res.write('</div>');
                res.end();
            });
            pyspawn.stderr.on('data', (data) => {
                console.log(`stderr: ${data}`);
            });
            pyspawn.on('close', (code) => {
                console.log(`child process exited with code ${code}`);
            });
        });
            /*
            res.write('<form name="order" method="post" action="/orderprocess">');
            
            res.write('<table class="table table-hover">');
            res.write('<thead>');
            res.write('<tr>');

            res.write('<th scope="col">Menu</th>')
            res.write('<th scope="col"></th>');
            res.write('</tr>');
            res.write('</thead>');

            res.write('<tbody>');

            res.write('<tr>');
            res.write('<td><a href="/randomrow"><span class="pull-left"><img src="https://static.tildacdn.com/tild6438-3565-4838-b266-363130326466/GrapefruitMethod.jpg" class="rounded float-right" style="width:300px;height:200px;"alt=""></span></a></td>');
            res.write('<td><span class: "pull-left" style="text-align:left"><strong>Networking KSEA & UVa Faculty!</strong></br>');
            res.write('</br>Come network with the fellow faculty at UVa. Faculty memebers are from all schools including the medical school. If you are looking for a research opportunity or internship come join us! </br>');
            res.write('</br> Click on picture for more details');
            res.write('</td>');
            res.write('</tr>');

            res.write('<td><a href="/activitiesfair"><span class="pull-left"><img src="http://www.uvastudentcouncil.com/wp-content/uploads/2016/07/IMG_7770.jpg" class="rounded float-right" style="width:300px;height:200px;"alt=""></span></a></td>');
            res.write('<td><span class: "pull-left" style="text-align:left"><strong>Activities Fair</strong></br>');
            res.write('</br>Check out the KSEA booth at the Acitivites fair this fall semester! Learn more about KSEA and see whats in store for the year!</br>');
            res.write('</br> Click on picture for more details');
            res.write('</td>');
            res.write('</tr>');

            res.write('</tbody>');
            res.write('</table>');
            res.end();*/
    }
    else {
      res.write('nopage');
      res.end();
    }
  } 
  else {
      var filePath = '.' + req.url;
      if (filePath == './')
          filePath = './index.html';
      var extname = path.extname(filePath);
      var contentType = 'text/html';
      switch (extname) {
          case '.js':
              contentType = 'text/javascript';
              break;
          case '.css':
              contentType = 'text/css';
              break;
          case '.json':
              contentType = 'application/json';
              break;
          case '.png':
              contentType = 'image/png';
              break;
          case '.jpg':
              contentType = 'image/jpg';
              break;
          case '.wav':
              contentType = 'audio/wav';
              break;
      }
  
      fs.readFile(filePath, function(error, content) {
          if (error) {
              if(error.code == 'ENOENT'){
                  fs.readFile('./404.html', function(error, content) {
                      res.writeHead(200, { 'Content-Type': contentType });
                      res.end(content, 'utf-8');
                  });
              }
              else {
                  res.writeHead(500);
                  res.end('Sorry, check with the site admin for error: '+error.code+' ..\n');
                  res.end();
              }
          }
          else {
              res.writeHead(200, { 'Content-Type': contentType });
              res.end(content, 'utf-8');
          }
      });
    }
}).listen(1234, '0.0.0.0'); //connect to local ip
//}).listen(2020); //connect to localhost

function footbot (res) {
    res.write('<div class="page-footer font-small blue  small text-light bg-dark" role = "contentinfo" style="width:100%; bottom: 0; padding-top: 1em; padding-bottom: 1em; margin-top: 10px;">');
    res.write('  <div class="container" style = "text-align:center">');
    res.write('&copy; Swift Interns');
    res.write('  </div>');
    res.write('</div>');
  }