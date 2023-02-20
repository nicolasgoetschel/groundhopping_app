from flask import Flask, render_template, request, redirect

from controllers.country_controller import countries_blueprint
from controllers.league_controller import leagues_blueprint
from controllers.ground_controller import grounds_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(leagues_blueprint)
app.register_blueprint(grounds_blueprint)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)