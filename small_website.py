#website with Flask

#importinf Flask Class from Flask framework
from flask import Flask, render_template

#Instantiaing object
app=Flask(__name__)

#loading in home page
@app.route('/')

def home():
    return render_template("home.html")

@app.route('/about/')

def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
