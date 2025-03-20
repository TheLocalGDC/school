from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inschrijven", methods=["POST"])
def inschrijven():
    naam = request.form["naam"]
    email = request.form["email"]
    opleiding = request.form["opleiding"]
    
    # Hier kun je de gegevens opslaan in een database of naar een e-mail verzenden
    print(f"Naam: {naam}, Email: {email}, Opleiding: {opleiding}")
    
    return redirect(url_for("bedankt"))

@app.route("/bedankt")
def bedankt():
    return render_template("bedankt.html")

if __name__ == "__main__":
    app.run(debug=True)