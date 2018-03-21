from flask import Flask, flash, redirect, render_template, request, session, abort
import pickle
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        'index.html')


if __name__ == "__main__":
    model_name = 'saved_models/model_future_severity_untreated_off_SCORE_FUTURE_UPDRS_III_0.001_ranking_PD_GENPD_' \
                 'REGPD_0_to_0.33_timeframe'

    # X = [["TIME_PASSED", "SYSSUP", "DIASTND",  "AGE",
    #       "DIASUP", "UPDRS_I", "TIME_SINCE_DIAGNOSIS", "HRSUP",
    #       "TOTAL", "UPDRS_III", "EDUCYRS", "SYSSTND",
    #       "UPDRS_II", "HRSTND", "UPDRS_II_AND_III", "TIME_SINCE_FIRST_SYMPTOM"]]

    X = [[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]]

    loaded_model = pickle.load(open(model_name, 'rb'))

    pred = loaded_model.predict(X)

    print(pred)

    app.run(host='0.0.0.0', port=5001)
