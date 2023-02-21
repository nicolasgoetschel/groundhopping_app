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
@grounds_blueprint.route("/grounds/<id>")
def show(id):
    ground = ground_repository.select(int(id))
    return render_template("grounds/show.html", ground=ground)


# Delete One
@grounds_blueprint.route("/grounds/<id>/delete", methods = ['POST'])
def delete_ground():
    ground_repository.delete(id)
    return redirect ('/grounds')