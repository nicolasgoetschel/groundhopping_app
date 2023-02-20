from flask import Blueprint, render_template, request, redirect
from repositories import country_repository
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
    country = country_repository.select(id)
    return render_template("countries/show.html", country=country)

