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
league_2 = League("Scottish Championship", "logo", country_1)
league_repository.save(league_2)


# English Premier League
league_3 = League("Premier League", "logo", country_2)
league_repository.save(league_3)


# Scottish Premiership
ground_1 = Ground('Pittodrie Stadium', 'Aberdeen F.C.', 'Aberdeen', league_1, 20866, False)
ground_repository.save(ground_1)
ground_2 = Ground('Celtic Park', 'Celtic F.C.', 'Glasgow', league_1, 60411, False)
ground_repository.save(ground_2)
ground_3 = Ground('Tannadice Park', 'Dundee United F.C.', 'Dundee', league_1, 14223, False)
ground_repository.save(ground_3)
ground_4 = Ground('Tynecastle Park', 'Heart of Midlothian F.C.', 'Edinburgh', league_1, 19852, False)
ground_repository.save(ground_4)
ground_5 = Ground('Easter Road', 'Hibernian F.C.', 'Edinburgh', league_1, 20421,  False)
ground_repository.save(ground_5)
ground_6 = Ground('Rugby Park', 'Kilmarnock F.C.', 'Kilmarnock', league_1, 17889, False)
ground_repository.save(ground_6)
ground_7 = Ground('Almondvale Stadium', 'Livingston F.C.', 'Livingston', league_1, 8716, False)
ground_repository.save(ground_7)
ground_8 = Ground('Fir Park', 'Motherwell F.C.', 'Motherwell',league_1, 13677, False)
ground_repository.save(ground_8)
ground_9 = Ground('Ibrox Stadium', 'Rangers F.C.', 'Glasgow',league_1, 50817, False)
ground_repository.save(ground_9)
ground_10 = Ground('Victoria Park', 'Ross County F.C.', 'Dingwall', league_1, 6541, False)
ground_repository.save(ground_10)
ground_11 = Ground('McDiarmid Park', 'St Johnstone F.C.', 'Perth',league_1, 10696, False)
ground_repository.save(ground_11)
ground_12 = Ground('St Mirren Park', 'St Mirren F.C.', 'Paisley',league_1, 8023, False)
ground_repository.save(ground_12)


# Scottish Championship
ground_13 = Ground('Gayfield Park', 'Arbroath F.C.', 'Arbroath', league_2, 6600, False)
ground_repository.save(ground_13)
ground_14 = Ground('Somerset Park', 'Ayr United F.C.', 'Ayr', league_2, 10185, False)
ground_repository.save(ground_14)
ground_15 = Ground('Balmoral Stadium', 'Cove Rangers F.C,', 'Aberdeen', league_2, 2602, False)
ground_repository.save(ground_15)
ground_16 = Ground('Dens Park', 'Dundee F.C.', 'Dundee', league_2, 11775, False)
ground_repository.save(ground_16)
ground_17 = Ground('Cappielow Park', 'Greenock Morton F.C.', 'Greenock', league_2, 11589, False)
ground_repository.save(ground_17)
ground_18 = Ground('New Douglas Park', 'Hamilton Academical F.C.', 'Hamilton', league_2, 6018, False)
ground_repository.save(ground_18)
ground_19 = Ground('Caledonian Stadium', 'Inverness Caledonian Thistle F.C.', 'Inverness', league_2, 7512, False)
ground_repository.save(ground_19)
ground_20 = Ground('Firhill Stadium', 'Patrick Thistle', 'Glasgow', league_2, 10102, False)
ground_repository.save(ground_20)
ground_21 = Ground('Ochilview Park', "Queens's Park F.C.", 'Glasgow', league_2, 3746, False)
ground_repository.save(ground_21)
ground_22 = Ground("Starks' Park", 'Raith Rovers F.C.', 'Kirkcaldy', league_2, 8867, False)
ground_repository.save(ground_22)


# # English Premier League
ground_23 = Ground('Anfield', 'Liverpool F.C..', 'Liverpool', league_3, 53394, False)
ground_repository.save(ground_23)
ground_24 = Ground('Brentford Community Stadium', 'Brentford F.C.', 'London', league_3, 17250, False)
ground_repository.save(ground_24)
ground_25 = Ground('Craven Cottage', 'Fulham F.C.,', 'London', league_3, 25700, False)
ground_repository.save(ground_25)
ground_26 = Ground('Elland Road', 'Leeds United F.C.', 'Leeds', league_3, 37792, False)
ground_repository.save(ground_26)
ground_27 = Ground('Emirates Stadium', 'Arsenal F.C.', 'London', league_3, 60704, False)
ground_repository.save(ground_27)
ground_28 = Ground('Etihad Stadium', 'Manchester City F.C.', 'Manchester', league_3, 53400, False)
ground_repository.save(ground_28)
ground_29 = Ground('Falmer Stadium', 'Brighton & Hove Albion F.C.', 'Brighton and Hove', league_3, 31800, False)
ground_repository.save(ground_29)
ground_30 = Ground('Goodison Park', "Everton F.C.", 'Liverpool', league_3, 39572, False)
ground_repository.save(ground_30)
ground_31 = Ground("King Power Stadium", 'Leicester City F.C.', 'Leicester', league_3, 32261, False)
ground_repository.save(ground_31)
ground_32 = Ground('London Stadium', 'West Ham United F.C.', 'London', league_3, 62500, False)
ground_repository.save(ground_32)
ground_33 = Ground('Molineux Stadium', 'Wolverhampton Wanderers F.C.', 'Wolverhampton', league_3, 32050, False)
ground_repository.save(ground_33)
ground_34 = Ground('Old Trafford', 'Manchester United F.C,', 'Manchester', league_3, 74310, False)
ground_repository.save(ground_34)
ground_35 = Ground('Selhurst Park', 'Crystal Palace F.C.', 'London', league_3, 25486, False)
ground_repository.save(ground_35)
ground_36 = Ground("St James' Park", 'Newcastle United F.C.', 'Newcastle', league_3, 52305, False)
ground_repository.save(ground_36)
ground_37 = Ground("St Mary's Stadium", 'Southampton F.C.', 'Southampton', league_3, 32383, False)
ground_repository.save(ground_37)
ground_38 = Ground('Stamford Bridge', 'Chelsea F.C.', 'London', league_3, 40341, False)
ground_repository.save(ground_38)
ground_39 = Ground('City Ground', 'Nottingham Forest F.C.', 'Nottingham', league_3, 30445, False)
ground_repository.save(ground_39)
ground_40 = Ground('Tottenham Hotspur Stadium', "Tottenham Hotspur F.C.", 'London', league_3, 62850, False)
ground_repository.save(ground_40)
ground_41 = Ground("Villa Park", 'Aston Villa F.C.', 'Birmingham', league_3, 42749, False)
ground_repository.save(ground_41)
ground_42 = Ground('Vitality Stadium', 'AFC Bournemouth', 'Bournemouth', league_3, 11364, False)
ground_repository.save(ground_42)

pdb.set_trace()