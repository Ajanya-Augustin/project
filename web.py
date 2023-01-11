from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/air_quality")
def iris():
    return render_template('air_quality.html')

@app.route('/predict',methods = ['POST', 'GET'])
def predict():
  if request.method == 'POST':
      pm2.5 = request.form['pm2.5']
      pm10 = request.form['pm10']
      no2 = request.form['no2']
      co = request.form['co']
      so2 = request.form['so2']
      o3 = request.form['o3']
      sample = [int(pm2.5),int(pm10),int(no2),int(co),int(so2),int(o3)]
      pred = score(sample)
      return render_template("pred.html", value=pred)

if __name__ == "__main__":
    app.run()