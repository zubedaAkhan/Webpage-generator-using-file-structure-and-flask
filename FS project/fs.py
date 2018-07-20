from flask import Flask,redirect,render_template,url_for,request
import os
app = Flask(__name__)


# Home page
@app.route('/',methods=['POST','GET'])
def index():
    if(request.method=='POST'):
        company_name=request.form["company_name"]
        f=open(company_name+".txt","w")
        home_para_body=request.form["company_desc"]
        footer=request.form["footer"]
        about_para=request.form["about_para"]
        serv_1_head=request.form["service_1_head"]
        serv_1_desc=request.form["service_1_desc"]
        serv_2_head=request.form["service_2_head"]
        serv_2_desc=request.form["service_2_desc"]
        serv_3_head=request.form["service_3_head"]
        serv_3_desc=request.form["service_3_desc"]
        street_name=request.form["street_address"]
        city_name=request.form["city_name"]
        state_name=request.form["state_name"]
        
        phone=request.form["phone"]
        email=request.form["email"]
        facebook=request.form["facebook"]
        twitter=request.form["twitter"]
        google=request.form["google_plus"]
        f.write("HOME###")
        f.write("TITLE|"+company_name+"###")
        f.write("PARA|WHAT WE DO!!!|"+home_para_body+"###")
        f.write("FOOTER|"+footer+"###\n")
        #writing home end
        #writing about page
        f.write("ABOUT###")
        f.write("PARA|ABOUT US|"+about_para+"###\n")
        #writing about page end
        # services page
        f.write("SERVICES###")
        f.write("SERVICE1|"+serv_1_head+"|"+serv_1_desc+"###")
        f.write("SERVICE2|"+serv_2_head+"|"+serv_2_desc+"###")
        f.write("SERVICE3|"+serv_3_head+"|"+serv_3_desc+"###\n")

        #writing contact us page
        f.write("CONTACT###")
        f.write("ADDRESS|"+street_name+"|"+city_name+"|"+state_name+"###")
        f.write("PHONE|"+phone+"###")
        f.write("MAIL|"+email+"###\n")
        # contact us page ends
        # social media
        f.write("SOCIAL###")
        if(facebook!="None"):
            f.write("FB|"+facebook+"###")
        if(google!="None"):
            f.write("GPLUS|"+google+"###")
        f.write("TWITTER|"+twitter+"###")

        f.close()
        return redirect(url_for('process',company_name=company_name))
    else:
        return render_template('ui page.html')

@app.route('/process/<company_name>')
def process(company_name):
    return render_template('process.html',company_name=company_name)

@app.route('/display/<company_name>')
def display(company_name):
    f = open(company_name+'.txt')
    return render_template('display.html',company_name=f)

@app.route('/convert/<company_name>')
def convert(company_name):
    f=open(company_name+'.txt','r')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    output_file = open(dir_path+'/templates/'+company_name+'.html','w')
    footer=''
# reading the file
    for line in f:
        hash_splitter = line.split("###")
    # HOME 
        if(hash_splitter[0]=="HOME"):
        # Head part of html
            output_file.write(''' <!DOCTYPE html> <html> <head>
        <!--Import Google Icon Font-->
        <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed" rel="stylesheet">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Jua" rel="stylesheet"> 
        <!--Import materialize.css-->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/css/materialize.min.css">
        <script defer src="https://use.fontawesome.com/releases/v5.0.10/js/all.js" integrity="sha384-slN8GvtUJGnv6ca26v8EzVaR9DC58QEwsIk9q1QXdCU8Yu8ck/tL/5szYlBbqmS+" crossorigin="anonymous"></script>
        <!--Let browser know website is optimized for mobile-->
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <style>
        body{
            font-family: 'Roboto Condensed', sans-serif;
            font-size: 18px;
        }
        .nav-wrapper ul li a{
            font-size: 18px;
            font-weight: bold;
        }
        .card{
            background-color: rgba(15, 13, 13, 0.9);
        }
        h1,h2,h3,h4,h5{
            font-family: 'Jua', sans-serif;
            font-size: 40px;
            
        }
        #label{
            font-size:25px;
        }
        footer{
            font-family: 'Jua', sans-serif;
        }
        
        </style>
        <title> ''')
            pipeliner = hash_splitter[1].split("|")
            company_name=pipeliner[1]
            output_file.write(company_name)
            output_file.write('''</title> 
        </head>
        <body id="home" class="scrollspy">
        <div class="navbar-fixed">
            <nav class="blue darken-4">
            <div class="container">
                <div class="nav-wrapper">
                <a href="#home" class="brand-logo scrollspy">''')
            output_file.write(company_name)
            output_file.write(''' </a>
                <a href="" data-target="mobile-menu" class="sidenav-trigger">
                    <i class="material-icons ">menu</i>
                </a>
                <ul class="right hide-on-med-and-down">
                <li>
                    <a href="#home" class="font-weight-bold">Home</a>
                </li>
                <li>
                    <a href="#about">About</a>
                </li>
                <li>
                    <a href="#services">Services</a>
                </li>
                <li>
                    <a href="#contact-us">Contact us</a>
                </li>
                <li>
                    <a href="#social-media">Social Media</a>
                </li>
                </ul>
                </div>
            </div>
            </nav>
        </div>
        <ul class="sidenav" id="mobile-menu">
            <li>
                <a href="#home" class="font-weight-bold">Home</a>
            </li>
            <li>
                <a href="#about">About</a>
            </li>
            <li>
                <a href="#services">Services</a>
            </li>
            <li>
                <a href="#contact-us">Contact us</a>
            </li>
            <li>
                <a href="#social-media">Social Media</a>
            </li>
            </ul>

            <!-- showcase -->
            <section class="slider">
                <ul class="slides">
                    <li>
                    <img src="/static/showcase.jpeg"> <!-- random image -->
                    <div class="caption center-align ">
                        <h1 class="red-text lighten-5 z-depth-5 width: 85%; margin:auto; font-size:50px; padding:10px;font-weight: bold;">What we do?</h3>
                        <p class="grey-text flow-text text-lighten-3 black lighten-4">''')
            pipeliner=hash_splitter[2].split("|")
            output_file.write(pipeliner[2])
            output_file.write(''' </p>
                    </div>
                    </li>
                </ul>
            </section>
    ''')
            pipeliner=hash_splitter[3].split("|")
            footer=pipeliner[1]
        elif(hash_splitter[0]=="ABOUT"):
            output_file.write(''' <section class="section white container scrollspy" id="about">
            <div class="row">
                <div class="col s12">
                <h2 class="teal-text darken-4 center-align z-depth-5" style="font-size:50px; padding:10px;font-weight: bold; width: 85%; margin:auto;"> ABOUT US</h2>
                <p class="flow-text center-align">
            ''')
            pipeliner=hash_splitter[1].split("|")
            output_file.write(pipeliner[2])
            output_file.write(''' </p>
                </div>
            </div>
            </section> ''')


        elif(hash_splitter[0]=="SERVICES"):
            output_file.write(''' <section class="section parallax-container scrollspy" style="padding: 30px; height:100%;" id="services">
                <h2 class="red-text text-darken-2 center-align z-depth-5" style="font-size:50px; padding:10px;font-weight: bold; width: 85%; margin:auto;">SERVICES WE PROVIDE</h2>
                <div class="parallax"><img src="/static/showcase1.jpeg"></div>
                <div class="container-fluid">
                <div class="row">
                    <div class="col s12 m12 l4">
                    <div class="card">
                        <div class="card-content white-text">
                        <h4 class="center-align blue-text text-darken-4">''')
            pipeliner=hash_splitter[1].split("|")
            output_file.write(pipeliner[1])
            output_file.write('''</h4>
                        <p class="flow-text center-align z-depth-3">''')
            output_file.write(pipeliner[2])
            output_file.write('''</p>
                        </div>
                    </div>
                    </div>
                    <div class="col s12 m12 l4">
                    <div class="card">
                        <div class="card-content white-text">
                        <h4 class="center-align teal-text text-lighten-4">''')
        # service 2
            pipeliner=hash_splitter[2].split("|")
            output_file.write(pipeliner[1])
            output_file.write('''</h4>
                        <p class="flow-text center-align z-depth-3">''')
            output_file.write(pipeliner[2])
            output_file.write(''' </div>
                    </div>
                    </div>
                    <div class="col s12 m12 l4">
                    <div class="card">
                        <div class="card-content white-text">
                        <h4 class="center-align blue-text text-darken-4">''')
        # service 3
            pipeliner=hash_splitter[3].split("|")
            output_file.write(pipeliner[1])
            output_file.write('''</h4>
                        <p class="flow-text center-align z-depth-3">''')
            output_file.write(pipeliner[2])
            output_file.write('''</div>
                    </div>
                    </div>
                </div>
                </div>
            </section>''')
        elif(hash_splitter[0]=="CONTACT"):
            output_file.write('''<section class="section scrollspy white" id="contact-us" style="width: 85%; margin:auto;">
                <h2 class="materialize-red-text text-accent-3 center-align z-depth-5" style="font-size:50px; padding:10px;font-weight: bold; width: 85%; margin:auto;">CONTACT US AT</h2>
                <br>  
                <div class="row">
                
                <div class="col m12 s12 l6 left" >
                    <div class="light-blue  card z-depth-3" style="height: 550px;">
                    <div class="card-content black-text">
                        <h2 class="center-align white-text z-depth-3">ADDRESS</h2> <hr>
                        <i class="material-icons medium white-text">home</i><br>
                        <span class="left-align">''')
            pipeliner=hash_splitter[1].split("|")
            output_file.write(pipeliner[1])
            output_file.write('''</span> <br>
                        <span class="left-align">''')
            output_file.write(pipeliner[2])   
            output_file.write('''</span> <br>
                        <span class="left-align">''')
            addresss = pipeliner[3]
            output_file.write(addresss)
            output_file.write('''</span>
                        <hr class="grey-text">
                        <i class="material-icons medium white-text">mail</i><br>
                        <span class="left-align">''')
            pipeliner=hash_splitter[3].split("|")
            output_file.write(pipeliner[1])
            output_file.write('''</span>
                        <hr>
                        <i class="material-icons medium white-text">phone</i><br>
                        <span class="left-align">''')
            pipeliner=hash_splitter[2].split("|")
            output_file.write(pipeliner[1])
            output_file.write('''</span>
                        <hr>
                    </div>
                    </div>
                </div>
                <div class="col m12 s12 l6">
                    <div class="light-blue  card" style="height: 550px;">
                    <div class="card-content white-text">
                    <h2 class="center-align white-text z-depth-3">QUERIES</h2> <hr>
                    <form class="row">
                        <div class="row">
                            <div class="input-field col s12">
                            <input id="first_name" type="text" class="validate">
                            <label for="first_name" class="grey-text text-darken-3" id="label">First Name</label>
                            </div>
                            <div class="input-field col s12">
                            <input id="last_name" type="text" class="validate" >
                            <label for="last_name" class="grey-text text-darken-3" id="label">Last Name</label>
                            </div>
                            <div class="input-field col s12">
                            <input type="email" id="mail_id" class="validate">
                            <label for="mail_id" class="grey-text text-darken-3" id="label">Email Address</label>
                            </div>
                            <div class="input-field col s12">
                            <textarea id="query" class="materialize-textarea" cols="30" rows="5"></textarea>
                            <label for="query" class="grey-text text-darken-3" id="label">Enter your query</label>
                            </div>
                            <button class="btn waves-effect waves-blue teal darken-4 large" type="submit" name="action" style="margin-left: 10px;">Submit
                            </button>
                        </div>
                        </form>
                    </div>
                    </div>
                </div>
                </div>
            </section>
                ''')

        elif(hash_splitter[0]=="SOCIAL"):
            output_file.write(''' <section class="section scrollspy parallax-container" style="padding: 50px; height:100%;" id="social-media">
                <div class="parallax"><img src="/static/social.jpeg"></div>
            <div class="container center-align">
                <h2 class="center-align white-text z-depth-5" style="font-size:50px; padding:10px;font-weight: bold;">CONNECT WITH US AT</h2>
                <div class="z-depth-3" style="padding: 10px;">
                <div class="card light-blue lighten-5  " style="width: 100%; padding: 30px; margin: auto; ">
                    <div class="row card-content">
                    ''')
            for i in hash_splitter:
                pipeliner=i.split("|")
                if(pipeliner[0]=="FB"):
                    output_file.write('''<div class="col s12">
                        <i class="fab fa-facebook-square fa-4x blue-text text-darken-4"></i> 
                        <p class="black-text" style="font-size: 20px; font-weight: bold">''')    
                    output_file.write(pipeliner[1])
                    output_file.write('''</p>
                        <hr>
                    </div>''')
                elif(pipeliner[0]=="GPLUS"):
                    output_file.write('''<div class="col s12"> <i class="fab  fa-google-plus-g fa-4x red-text text-darken-4"></i> 
                        <p class="black-text" style="font-size: 20px; font-weight: bold">''')
                    output_file.write(pipeliner[1])
                    output_file.write('''</p>
                        <hr>
                    </div> ''')
                elif(pipeliner[0]=="TWITTER"):
                    output_file.write('''<div class="col s12">
                        <i class="fab fa-twitter fa-4x blue-text text-darken-2"></i> 
                        <p class="black-text" style="font-size: 20px; font-weight: bold">''')
                    output_file.write(pipeliner[1])
                    output_file.write('''</p>
                        <hr>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </section>''')



    output_file.write('''<footer class="page-footer  section blue darken-4">
                <div class="center-align">
                    <p class="flow-text" style="font-weight: bold"> &copy;''')
    output_file.write(footer)
    output_file.write('''</p>
                </div>
            </footer>
        



        <!--JavaScript at end of body for optimized loading-->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js"></script>
        <script>
            const navbar = document.querySelector(".sidenav");
            M.Sidenav.init(navbar,{})
            const slider = document.querySelector(".slider");
            M.Slider.init(slider,{indicators:false})
            const parallax = document.querySelectorAll(".parallax")
            M.Parallax.init(parallax,{});
            
            const scrollspy = document.querySelectorAll(".scrollspy")
            M.ScrollSpy.init(scrollspy, {});
        </script>
                
        </body>
    </html>''')

    return render_template('finish.html',company_name=company_name)
@app.route('/<company_name>')
def company(company_name):
    return render_template(company_name+'.html')
    
if(__name__=='__main__'):
    app.run()
