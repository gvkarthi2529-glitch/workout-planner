from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        goal = request.form["goal"]

        if goal == "Weight Loss":
            result = "🏃 Cardio, Running, Cycling"

        elif goal == "Muscle Gain":
            result = "💪 Pushups, Squats, Weight Training"

        else:
            result = "🧘 Yoga, Walking, Stretching"

    return f"""
    <html>
    <head>
        <title>Workout Planner</title>

        <style>
            body {{
                font-family: Arial;
                background: lightblue;
                text-align: center;
                padding-top: 50px;
            }}

            .box {{
                background: white;
                width: 400px;
                margin: auto;
                padding: 20px;
                border-radius: 10px;
            }}

            input, select, button {{
                margin: 10px;
                padding: 10px;
                width: 80%;
            }}
        </style>

    </head>

    <body>

        <div class="box">

            <h1>Personalized Workout Planner</h1>

            <form method="POST">

                <input type="number" placeholder="Enter Age" required>

                <input type="number" placeholder="Enter Weight" required>

                <select name="goal">
                    <option>Weight Loss</option>
                    <option>Muscle Gain</option>
                    <option>Fitness</option>
                </select>

                <br>

                <button type="submit">Get Plan</button>

            </form>

            <h2>{result}</h2>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
