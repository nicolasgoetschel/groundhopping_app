from db.run_sql import run_sql
from models.league import League
import repositories.ground_repository as ground_repository

# Create
def save(league):
    sql = "INSERT INTO leagues (name, logo, grounds) VALUES (%s, %s, %s) RETURNING *"
    values = [league.name, league.logo, league.grounds]
    results = run_sql(sql, values)
    league.id = results[0]['id']