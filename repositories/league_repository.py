from db.run_sql import run_sql
from models.league import League
from models.country import Country
import repositories.country_repository as country_repository

# Create
def save(league):
    sql = "INSERT INTO leagues (name, logo, grounds) VALUES (%s, %s, %s) RETURNING *"
    values = [league.name, league.logo, league.grounds]
    results = run_sql(sql, values)
    league.id = results[0]['id']

def select_all():
    leagues = []

    sql = "SELECT * FROM leagues"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        league = League(row['name'], row['logo'], row['grounds'], row['id'] )
        leagues.append(league)
    return leagues

def select(id):
    league = None
    sql = "SELECT * FROM leagues WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        country = country_repository.select(result['country_id'])
        league = League(result['name'], result['logo'], result['grounds'], result['id'])
    return league

def delete_all():
    sql = "DELETE  FROM leagues"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql, values)