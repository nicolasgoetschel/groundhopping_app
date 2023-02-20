from db.run_sql import run_sql
from models.ground import Ground
from models.league import League
from models.country import Country
import repositories.country_repository as country_repository
import repositories.league_repository as league_repository

# Create
def save(ground):
    sql = "INSERT INTO grounds (name, team, location, league_id, capacity, visited) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [ground.name, ground.team, ground.location, ground.league.id, ground.capacity, ground.visited]
    results = run_sql(sql, values)
    ground.id = results[0]['id']
    return ground


def select_all():
    grounds = []
    
    sql = "SELECT * FROM grounds"
    results = run_sql(sql)
    
    for row in results:
        league = league_repository.select(row['league_id'])
        ground = Ground(row['name'], row['team'], row['location'], league, row['visited'], row['id'])
        grounds.append(ground)
    return grounds

def select(id):
    ground = None
    sql = "SELECT * FROM grounds WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        league = league_repository.select(result['league_id'])
        ground = Ground(result['name'], result['team'], result['location'], league, result['visited'], result['id'])
    return ground

def delete_all():
    sql = "DELETE  FROM grounds"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM grounds WHERE id = %s"
    values = [id]
    run_sql(sql, values)