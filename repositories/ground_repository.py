from db.run_sql import run_sql
from models.ground import Ground
from models.league import League
from models.country import Country
import repositories.country_repository as country_repository
import repositories.league_repository as league_repository

# Create
def save(ground):
    sql = "INSERT INTO grounds (name, team, location, capacity, visited) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [ground.name, ground.team, ground.location, ground.capacity, ground.visited]
    results = run_sql(sql, values)
    ground.id = results[0]['id']

def select_all():
    grounds = []

    sql = "SELECT * FROM grounds"
    results = run_sql(sql)

    for row in results:
        league = country_repository.select(row['country_id'])
        ground = League(row['name'], row['team'], row['location'], row['capacity'], row['visited'], row['id'] )
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
        ground = Ground(result['name'], result['team'], result['location'], result['visited'], result['id'])
    return ground