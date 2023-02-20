from flask import Blueprint, render_template, request, redirect
from repositories import ground_repository, league_repository, country_repository
from models.league import League
from models.ground import Ground


grounds_blueprint = Blueprint("grounds", __name__)

# View all
@grounds_blueprint.route("/grounds")
def show_all():
    grounds = ground_repository.select_all()
    return render_template("grounds/index.html", grounds=grounds)


# View One
@grounds_blueprint.route("/grounds/<ground_id>/grounds/<id>")
def show(ground_id, id):
    ground = ground_repository.select(id)
    league = league_repository.select(ground.league_id)
    # country = country_repository.select(league.country_id)
    return render_template("grounds/show.html", ground=ground, league=league)