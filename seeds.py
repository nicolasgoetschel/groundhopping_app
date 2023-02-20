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

# Scottish Premiership
ground_1 = Ground('Pittodrie Stadium', 'Aberdeen F.C.', 'Aberdeen', 20866, False)
ground_repository.save(ground_1)

league_1 = League("Scottish Premiership", "logo", ground_1)
league_repository.save(league_1)

country_1 = Country('Scotland', "flag", league_1)
country_repository.save(country_1)

pdb.set_trace()