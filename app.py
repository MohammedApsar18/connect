from flask import Flask, render_template, request
from analyzer import analyze_incident

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    incident = ""
    if request.method == "POST":
        incident = request.form.get("incident", "").strip()
        if incident:
            result = analyze_incident(incident)
    return render_template("index.html", result=result, incident=incident)

if __name__ == "__main__":
    app.run(debug=True)
