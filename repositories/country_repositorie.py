from db.run_sql import run_sql
from models.country import Country
import repositories.league_repository as league_repository

# Create
def save(country):
    sql = "INSERT INTO countries (name, flag, leagues) VALUES (%s, %s, %s) RETURNING *"
    values = [country.name, country.flag, country.leagues]
    results = run_sql(sql, values)
    country.id = results[0]['id']

    