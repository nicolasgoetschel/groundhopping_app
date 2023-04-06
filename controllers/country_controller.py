from flask import Blueprint, render_template, request, redirect
from repositories import country_repository, league_repository
from models.country import Country

countries_blueprint = Blueprint("countries", __name__)

# # View all
# @countries_blueprint.route("/countries")
# def show_all():
#     countries = country_repository.select_all()
#     return render_template("countries/index.html", countries=countries)

# View all
@countries_blueprint.route("/countries")
def show_all():
    countries = country_repository.select_all()
    countries = sorted(countries, key=lambda c: c.name)  # Sort the countries by name
    return render_template("countries/index.html", countries=countries)

# View One
@countries_blueprint.route("/countries/<id>")
def show(id):
    leagues = league_repository.select_all()
    country = country_repository.select(int(id))
    print( country.name )
    return render_template("countries/show.html", country=country, leagues=leagues)

# Delete One
@countries_blueprint.route("/countries/<id>/delete", methods = ['POST'])
def delete_country(id):
    country_repository.delete(int(id))
    return redirect ('/countries')

# New
@countries_blueprint.route("/countries/new")
def new_country():
    return render_template("countries/new.html")

# Create
@countries_blueprint.route("/countries", methods=["POST"])
def create():
    name = request.form["name"]
    flag = request.form["flag"]
    new_country = Country(name, flag)
    country_repository.save(new_country)
    return redirect("/countries")




