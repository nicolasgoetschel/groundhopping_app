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
def delete_ground(id):
    ground_repository.delete(int(id))
    return redirect ('/grounds')

# New
@grounds_blueprint.route("/grounds/new")
def ground():
    leagues = league_repository.select_all()
    return render_template("grounds/new.html", leagues=leagues)

# Create
@grounds_blueprint.route("/grounds", methods=["POST"])
def create():
    name = request.form["name"]
    team = request.form["team"]
    location = request.form["location"]
    id = request.form["league_id"]
    capacity = request.form["capacity"]
    # visited = request.form["visited"]
    new_league = league_repository.select(id)
    new_ground = Ground(name, team, location, new_league, capacity, False)
    ground_repository.save(new_ground)
    return redirect("/grounds")

# Update
@grounds_blueprint.route("/grounds/<id>", methods = ["Post"])
def update(id):
    update_ground = ground_repository.select(int(id))
    visited = "visited" in request.form 
    update_ground.toggle_visited(visited)
    ground_repository.update(update_ground)
    return redirect("/grounds/"+id)