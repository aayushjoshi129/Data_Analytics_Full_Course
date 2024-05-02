from flask import Flask, render_template, request, redirect, url_for
import model_train
app = Flask(__name__)

@app.route("/",  methods=['GET','POST'])

def pow():
    ep = None
    if request.method == "POST":
        power = request.form['engine']
        engine_pred = model_train.engine_pred(int(power))
        ep = engine_pred
        print(engine_pred)

    return render_template("engine_power.html", eng = ep)

if __name__ == "__main__":
    app.run(debug=True)
