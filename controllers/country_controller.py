from flask import Blueprint, render_template, request, redirect
from repositories import country_repository, league_repository
from models.country import Country

countries_blueprint = Blueprint("countries", __name__)

# View all
@countries_blueprint.route("/countries")
def show_all():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries=countries)

# View One
@countries_blueprint.route("/countries/<id>")
def show(id):
    leagues = league_repository.select_all()
    country = country_repository.select(int(id))
    print( country.name )
    return render_template("countries/show.html", country=country, leagues=leagues)

