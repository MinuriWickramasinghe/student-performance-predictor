from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)


# Load trained ML model
with open("model/student_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        # Get student information
        studytime = float(request.form["studytime"])
        failures = int(request.form["failures"])
        absences = int(request.form["absences"])
        G1 = float(request.form["G1"])
        G2 = float(request.form["G2"])


        # Create student data
        student = pd.DataFrame(
            [[
                studytime,
                failures,
                absences,
                G1,
                G2
            ]],
            columns=[
                "studytime",
                "failures",
                "absences",
                "G1",
                "G2"
            ]
        )


        # Make prediction
        prediction = model.predict(student)[0]


    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)