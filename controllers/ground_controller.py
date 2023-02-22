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
    # Grab a Ground we want to update
    update_ground = ground_repository.select(int(id))
    # If there is a form input named "Visited" in the update form then store True in this visited variable/ otherwise store false.

    # Grab name from the update form and then use a method from the ground model to update the Ground object that we grabbed from the ground repository on line 51
    name = request.form["name"]
    update_ground.change_name(name)
    # Grab capacity from the update form and then use a method from the ground model to update the Ground object that we grabbed from the ground repository on line 51
    capacity = request.form["capacity"]
    update_ground.change_capacity(capacity)
    # Grab league id from the update form and then using the id to get a league object from the league repository.
    # and then use a method from the ground model to update the Ground object that we grabbed from the ground repository on line 51
    league_id = request.form["league_id"]
    league = league_repository.select(league_id)
    update_ground.change_league(league)
    # Using the ground repositorys update method to update the modified ground object in the database. 
    ground_repository.update(update_ground)
    # Redirecting back to the ground show page. 
    return redirect("/grounds/"+id)

# Update Visited
@grounds_blueprint.route("/groundss/visited/<id>", methods = ["POST"])
def update_visited(id):
        # Grab a Ground we want to update
        update_ground = ground_repository.select(int(id))
        # If there is a form input named "Visited" in the update form then store True in this visited variable/ otherwise store false.
        visited = "visited" in request.form 
        # Using the method on the Ground Model to update the visited property
        update_ground.toggle_visited(visited)
        # Using the ground repositorys update method to update the modified ground object in the database. 
        ground_repository.update(update_ground)
        # Redirecting back to the ground show page. 
        return redirect("/grounds/"+id)

# Update Tier
@grounds_blueprint.route("/groundds/tier/<id>", methods = ["Post"])
def update_tier(id):
    # Grab a Ground we want to update
    update_ground = ground_repository.select(int(id))
    # Grab league id from the update form and then using the id to get a league object from the league repository.
    # and then use a method from the ground model to update the Ground object that we grabbed from the ground repository on line 51
    league_id = request.form["league_id"]
    league = league_repository.select(league_id)
    update_ground.change_league(league)
    # Using the ground repositorys update method to update the modified ground object in the database. 
    ground_repository.update(update_ground)
    # Redirecting back to the ground show page. 
    return redirect("/grounds/"+id)        

# Edit
@grounds_blueprint.route("/grounds/<id>/edit", methods = ["GET"])
def edit_ground(id):
    ground = ground_repository.select(int(id))
    leagues = league_repository.select_all()
    return render_template("/grounds/edit.html", ground=ground, leagues=leagues)