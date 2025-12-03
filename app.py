from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

workouts = []  # each item: {"date": ..., "type": ..., "minutes": ...}


@app.route("/")
def index():
    total_minutes = sum(w["minutes"] for w in workouts)
    workout_count = len(workouts)
    return render_template(
        "index.html",
        total_minutes=total_minutes,
        workout_count=workout_count
    )


@app.route("/add", methods=["GET", "POST"])
def add_workout():
    if request.method == "POST":
        date = request.form.get("date")
        wtype = request.form.get("type")
        minutes_str = request.form.get("minutes", "0")

        try:
            minutes = int(minutes_str)
        except ValueError:
            minutes = 0

        workouts.append({"date": date, "type": wtype, "minutes": minutes})
        return redirect(url_for("summary"))

    return render_template("page1.html")  # Add Workout page


@app.route("/summary")
def summary():
    total_minutes = sum(w["minutes"] for w in workouts)
    return render_template(
        "page2.html",
        workouts=workouts,
        total_minutes=total_minutes
    )


if __name__ == "__main__":
    app.run(debug=True)
