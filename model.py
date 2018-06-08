from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import pickle
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        'index.html')

@app.route("/launch")
def launch():
    return render_template(
        'RoP.html')

@app.route("/about")
def about():
    return render_template(
        'generic.html')

@app.route('/model', methods = ['POST'])
def model():
    # features = ["TIME_PASSED", "SYSSUP", "DIASTND",  "AGE",
    #       "DIASUP", "UPDRS_I", "TIME_SINCE_DIAGNOSIS", "HRSUP",
    #       "TOTAL", "UPDRS_III", "EDUCYRS", "SYSSTND",
    #       "UPDRS_II", "HRSTND", "UPDRS_II_AND_III", "TIME_SINCE_FIRST_SYMPTOM"]

    # X = [[request.form[feature] for feature in features]]

    X = [[request.form["TIME_PASSED"], request.form["SYSSUP"], request.form["DIASTND"], request.form["AGE"],
          request.form["DIASUP"], request.form["UPDRS_I"], request.form["TIME_SINCE_DIAGNOSIS"], request.form["HRSUP"],
          request.form["UPDRS_I"] + request.form["UPDRS_II"] + request.form["UPDRS_III"],
          request.form["UPDRS_III"], request.form["EDUCYRS"], request.form["SYSSTND"],
          request.form["UPDRS_II"], request.form["HRSTND"], request.form["UPDRS_II"] + request.form["UPDRS_III"],
          request.form["TIME_SINCE_FIRST_SYMPTOM"]]]

    pred = loaded_model.predict(X)

    future_score = round(pred[0], 2)

    return redirect(url_for('predict', future_score=future_score))

@app.route("/prediction")
def predict():
    return render_template("prediction.html", future_score=request.args.get('future_score'))


if __name__ == "__main__":
    model_name = 'saved_models/model_future_severity_untreated_off_SCORE_FUTURE_UPDRS_III_0.001_ranking_PD_GENPD_' \
                 'REGPD_0_to_0.33_timeframe'

    loaded_model = pickle.load(open(model_name, 'rb'))

    app.run(host='0.0.0.0', port=5001)
