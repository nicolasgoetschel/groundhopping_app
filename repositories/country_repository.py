from db.run_sql import run_sql
from models.country import Country
import repositories.league_repository as league_repository

# Create
def save(country):
    sql = "INSERT INTO countries (name, flag, leagues) VALUES (%s, %s, %s) RETURNING *"
    values = [country.name, country.flag, country.leagues]
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
        country = Country(row['name'], row['flag'], row['leagues'], row['id'] )
        countries.append(country)
    return countries

    