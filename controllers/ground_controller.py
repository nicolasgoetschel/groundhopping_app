from flask import Blueprint, render_template, request, redirect
from repositories import ground_repository, league_repository, country_repository
from models.league import League
from models.ground import Ground


grounds_blueprint = Blueprint("grounds", __name__)

# View all
@grounds_blueprint.route("/grounds")
def show_all():
    grounds = ground_repository.select_all()
    grounds = sorted(grounds, key=lambda c: c.name)  # Sort the grounds by name
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
    # league_id = request.form["league_id"]
    # league = league_repository.select(league_id)
    # update_ground.change_league(league)
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

# Promotion Update
@grounds_blueprint.route("/grounds/promotion/<id>", methods = ["POST"])
def promotion(id):
    # Grab the ground we want to update
    ground_to_update = ground_repository.select(int(id))
    # Grab all the leagues from the league repository
    leagues = league_repository.select_all()
    # Create a variable called new_league that will first be assigned the original grounds league (but this will be reasigned if it can be promoted)
    new_league = ground_to_update.league
    # Create a variable called promoted_tier that will hold the new tier number after promotion
    promoted_tier = ground_to_update.league.tier - 1
    # If the ground can be promoted, i.e. if the grounds league tier is greater than 1 then continue with the rest of this code
    if ground_to_update.league.tier > 1:
        # loop through the list of all leagues
        for league in leagues:
            # For each league in the list of leagues, if the leagues tier matches the promoted_tier and the leagues country id matches 
            # the ground we want to updates country id then reasign the new_league variable to be that league 
            if league.tier == promoted_tier and league.country.id == ground_to_update.league.country.id:
                new_league = league

    # update the ground we want to update with the change league method we have in our ground model with the new_league
    ground_to_update.change_league(new_league)
    # update the ground in our database with the repositorties update method.
    ground_repository.update(ground_to_update)
    return redirect("/grounds/"+id)      

# Relegation Update
@grounds_blueprint.route("/grounds/relegation/<id>", methods = ["POST"])
def relegation(id):
    # Grab the ground we want to update
    ground_to_update = ground_repository.select(int(id))
    # Grab all the leagues from the league repository
    leagues = league_repository.select_all()
    # Create a variable called new_league that will first be assigned the original gorunds league (but this will be reasigned if it can be relegated)
    new_league = ground_to_update.league
    # Create a variable called promoted_tier that will hold the new teir number after promotion
    relegated_tier = ground_to_update.league.tier + 1
    # loop through the list of all leagues
    for league in leagues:
        # For each league in the list of leagues, if the leagues tier matches the relegated_tier and the leagues country id matches the ground we want to updates country id then reasign the new_league variable to be that league 
        if league.tier == relegated_tier and league.country.id == ground_to_update.league.country.id:
            new_league = league
    # update the ground we want to update with the change league method we have in our ground model with the new_league
    ground_to_update.change_league(new_league)
    # update the ground in our database with the repositorties update method.
    ground_repository.update(ground_to_update)
    return redirect("/grounds/"+id)    

# Edit
@grounds_blueprint.route("/grounds/<id>/edit", methods = ["GET"])
def edit_ground(id):
    ground = ground_repository.select(int(id))
    leagues = league_repository.select_all()
    return render_template("/grounds/edit.html", ground=ground, leagues=leagues)