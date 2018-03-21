from flask import Flask, flash, redirect, render_template, request, session, abort
import pickle
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        'index.html')


if __name__ == "__main__":
    model_name = 'saved_models/'
    X = []

    loaded_model = pickle.load(open(model_name, 'rb'))

    pred = loaded_model.predict(X)

    print(pred)

    app.run(host='0.0.0.0', port=5000)
