import pdb
import repositories.country_repository as country_repository
import repositories.league_repository as league_repository
import repositories.ground_repository as ground_repository
from models.country import Country
from models.league import League
from models.ground import Ground

ground_repository.delete_all()
league_repository.delete_all()
country_repository.delete_all()

# Scotland
country_1 = Country('Scotland', "flag")
country_repository.save(country_1)

# England
country_2 = Country('England', "flag")
country_repository.save(country_2)


# Scottish Premiership
league_1 = League("Scottish Premiership", "logo", country_1)
league_repository.save(league_1)

# Scottish Championship
league_2 = League("Scottish Premiership", "logo", country_1)
league_repository.save(league_2)


# English Premier League
league_3 = League("Premier League", "logo", country_2)
league_repository.save(league_3)


# Scottish Premiership
ground_1 = Ground('Pittodrie Stadium', 'Aberdeen F.C.', 'Aberdeen', league_1, 20866, False)
ground_repository.save(ground_1)
ground_2 = Ground('Celtic Park', 'Celtic F.C.', 'GHlasgow', league_1, 60411, False)
ground_repository.save(ground_2)
ground_3 = Ground('Tannadice Park', 'Dundee United F.C.', 'Dundee', league_1, 14223, False)
ground_repository.save(ground_3)


# Scottish Championship
ground_13 = Ground('Gayfield Park', 'Arbroath F.C.', 'Arbroath', league_2, 6600, False)
ground_repository.save(ground_13)
ground_14 = Ground('Somerset Park', 'Ayr United F.C.', 'Ayr', league_2, 10185, False)
ground_repository.save(ground_14)
ground_15 = Ground('Balmoral Stadium', 'Cove Rangers F.C,', 'Aberdeen', league_2, 2602, False)
ground_repository.save(ground_15)


# # English Premier League
ground_23 = Ground('Anfield', 'Liverpool F.C..', 'Liverpool', league_3, 53394, False)
ground_repository.save(ground_23)
ground_24 = Ground('Brentford Community Stadium', 'Brentford F.C.', 'London', league_3, 17250, False)
ground_repository.save(ground_24)
ground_25 = Ground('Craven Cottage', 'Fulham F.C.,', 'London', league_3, 25700, False)
ground_repository.save(ground_25)


pdb.set_trace()