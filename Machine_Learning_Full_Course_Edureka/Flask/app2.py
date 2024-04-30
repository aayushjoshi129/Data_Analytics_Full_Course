from flask import Flask, render_template, request
import model_train
app = Flask(__name__)

@app.route("/",  methods=['GET','POST'])

def hello():
    if request.method == "POST":
        power = request.form['engine']
        engine_pred = model_train.engine_pred(int(power))
        print(engine_pred)
    return render_template("engine_power.html")

if __name__ == "__main__":
    app.run(debug=True)
