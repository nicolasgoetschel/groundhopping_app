from db.run_sql import run_sql

from models.country import Country
from models.league import League
from models.ground import Ground

from flask import Blueprint

leagues_blueprint = Blueprint("leagues", __name__)