from db.run_sql import run_sql
from models.ground import Ground

# Create
def save(ground):
    sql = "INSERT INTO grounds (name, team, location, capacity, visited) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [ground.name, ground.team, ground.location, ground.capacity, ground.visited]
    results = run_sql(sql, values)
    ground.id = results[0]['id']