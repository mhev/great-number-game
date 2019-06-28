import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def index():
    session['number']=random.randint(1,100)
    return render_template("index.html")

@app.route("/correct")
def success():
    return render_template("correct.html", answer=session['number'])
    

@app.route("/low")
def low():
    return render_template("toolow.html")

@app.route("/high")
def high():
    return render_template("toohigh.html")

@app.route("/process", methods=["POST"])
def process():
    guess = request.form['guess']
    print(request.form['guess'])

    if int(guess) == (session['number']):
        return redirect("/correct")

    elif int(guess) < (session['number']):
        return redirect("/low")

    elif int(guess) > (session['number']):
        return redirect("/high")



    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)