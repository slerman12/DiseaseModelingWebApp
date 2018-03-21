from flask import Flask, flash, redirect, render_template, request, session, abort
import pickle
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        'index.html')


if __name__ == "__main__":
    model_name = 'saved_models/model_future_severity_untreated_off_SCORE_FUTURE_UPDRS_III_0.001_ranking_PD_GENPD_REGPD_0_to_0.33_timeframe'
    X = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

    # loaded_model = pickle.load(open(model_name, 'rb'))
    #
    # pred = loaded_model.predict(X)
    #
    # print(pred)

    app.run(host='0.0.0.0', port=5001)
