from db.run_sql import run_sql
from models.country import Country
from models.league import League
import repositories.league_repository as league_repository
import repositories.country_repository as country_repository

# Create
def save(country):
    sql = "INSERT INTO countries (name, flag) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.flag]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

# Read
def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['flag'], row['id'] )
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        country = Country(result['name'], result['flag'], result['id'])
    return country

def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

    
    