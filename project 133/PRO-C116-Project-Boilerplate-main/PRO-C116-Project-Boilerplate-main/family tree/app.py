
from flask import Flask , render_template


app = Flask(__name__)


@app.route("/")
def home():

    name = "Pugal"
    age = "12"
    return render_template('index.html' , name = name , age = age)


@app.route("/father")
def father():

    name = "Kasi" 
    age = "40" 

    return render_template('father.html' , name = name , age = age)


@app.route("/mother")
def mother():

    name = "Saranya" 
    age = "37" 

    return render_template('mother.html' , name = name , age = age)



@app.route("/friend")
def friend():

    name = "Hari" 
    age = "12" 

    return render_template('friend.html' , name = name , age = age)






if __name__  ==  '__main__':
    app.run(debug=True)