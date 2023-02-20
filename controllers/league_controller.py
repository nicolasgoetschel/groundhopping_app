
from flask import Blueprint, render_template, request, redirect
from repositories import league_repository, country_repository
from models.league import League


leagues_blueprint = Blueprint("leagues", __name__)

# View all
@leagues_blueprint.route("/leagues")
def show_all():
    leagues = league_repository.select_all()
    return render_template("leagues/index.html", leagues=leagues)


# View One
@leagues_blueprint.route("/leagues/<league_id>/leagues/<id>")
def show(league_id, id):
    league = league_repository.select(id)
    country = country_repository.select(league.country_id)
    return render_template("leagues/show.html", league=league, country=country)