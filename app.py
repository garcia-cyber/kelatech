from flask import Flask , render_template , redirect , session 



app = Flask(__name__) 
app.secret_key = "Kelatech_sitaEgeune " 

## page d'accueil 
@app.route('/')
@app.route("/kelatech")
def kelatech():
    return render_template('index.html')
 
     

#boucle 
if __name__ == '__main__' :
    app.run(debug = True) 