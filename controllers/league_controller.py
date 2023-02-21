
from flask import Blueprint, render_template, request, redirect
from repositories import league_repository, ground_repository, country_repository
from models.ground import Ground
from models.league import League


leagues_blueprint = Blueprint("leagues", __name__)

# View all
@leagues_blueprint.route("/leagues")
def show_all():
    leagues = league_repository.select_all()
    return render_template("leagues/index.html", leagues=leagues)

# View One
@leagues_blueprint.route("/leagues/<id>")
def show(id):
    grounds = ground_repository.select_all()
    league = league_repository.select(int(id))
    return render_template("leagues/show.html", league=league, grounds=grounds)

# Delete One
@leagues_blueprint.route("/leagues/<id>/delete", methods = ['POST'])
def delete_league(id):
    league_repository.delete(int(id))
    return redirect ('/leagues')

# New
@leagues_blueprint.route("/leagues/new")
def league():
    countries = country_repository.select_all()
    return render_template("leagues/new.html", countries=countries)

# Create
@leagues_blueprint.route("/leagues", methods=["POST"])
def create():
    name = request.form["name"]
    logo = request.form["logo"]
    id = request.form["country_id"]
    country = country_repository.select(id)
    new_league = League(name, logo, country)
    league_repository.save(new_league)
    return redirect("/leagues")