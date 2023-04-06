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

# Scottish 1st
league_1 = League("Scottish Premiership", "logo", country_1, 1)
league_repository.save(league_1)

# Scottish 2nd
league_2 = League("Scottish Championship", "logo", country_1, 2)
league_repository.save(league_2)

# Scottish 3rd
league_16 = League("Scottish League One", "logo", country_1, 3)
league_repository.save(league_16)

# Scottish 4th
league_17 = League("Scottish League Two", "logo", country_1, 4)
league_repository.save(league_17)

# Scottish Premiership
ground_1 = Ground('Celtic Park', 'Celtic F.C.', 'Glasgow', league_1, 60411, False)
ground_repository.save(ground_1)
ground_2 = Ground('Ibrox Stadium', 'Rangers F.C.', 'Glasgow', league_1, 50817, False)
ground_repository.save(ground_2)
ground_3 = Ground('Pittodrie Stadium', 'Aberdeen F.C.', 'Aberdeen', league_1, 20866, False)
ground_repository.save(ground_3)
ground_4 = Ground('Easter Road', 'Hibernian F.C.', 'Edinburgh', league_1, 20421,  False)
ground_repository.save(ground_4)
ground_5 = Ground('Tynecastle Park', 'Heart of Midlothian F.C.', 'Edinburgh', league_1, 19852, False)
ground_repository.save(ground_5)
ground_6 = Ground('Rugby Park', 'Kilmarnock F.C.', 'Kilmarnock', league_1, 17889, False)
ground_repository.save(ground_6)
ground_7 = Ground('Tannadice Park', 'Dundee United F.C.', 'Dundee', league_1, 14223, False)
ground_repository.save(ground_7)
ground_8 = Ground('Fir Park', 'Motherwell F.C.', 'Motherwell', league_1, 13677, False)
ground_repository.save(ground_8)
ground_9 = Ground('McDiarmid Park', 'St Johnstone F.C.', 'Perth', league_1, 10696, False)
ground_repository.save(ground_9)
ground_10 = Ground('Almondvale Stadium', 'Livingston F.C.', 'Livingston', league_1, 8716, False)
ground_repository.save(ground_10)
ground_11 = Ground('St Mirren Park', 'St Mirren F.C.', 'Paisley', league_1, 8023, False)
ground_repository.save(ground_11)
ground_12 = Ground('Victoria Park', 'Ross County F.C.', 'Dingwall', league_1, 6541, False)
ground_repository.save(ground_12)


# Scottish Championship
ground_13 = Ground('Dens Park', 'Dundee F.C.', 'Dundee', league_2, 11775, False)
ground_repository.save(ground_13)
ground_14 = Ground('Cappielow Park', 'Greenock Morton F.C.', 'Greenock', league_2, 11589, False)
ground_repository.save(ground_14)
ground_15 = Ground('Somerset Park', 'Ayr United F.C.', 'Ayr', league_2, 10185, False)
ground_repository.save(ground_15)
ground_16 = Ground('Firhill Stadium', 'Patrick Thistle', 'Glasgow', league_2, 10102, False)
ground_repository.save(ground_16)
ground_17 = Ground("Starks' Park", 'Raith Rovers F.C.', 'Kirkcaldy', league_2, 8867, False)
ground_repository.save(ground_17)
ground_18 = Ground('Caledonian Stadium', 'Inverness Caledonian Thistle F.C.', 'Inverness', league_2, 7512, False)
ground_repository.save(ground_18)
ground_19 = Ground('Gayfield Park', 'Arbroath F.C.', 'Arbroath', league_2, 6600, False)
ground_repository.save(ground_19)
ground_20 = Ground('New Douglas Park', 'Hamilton Academical F.C.', 'Hamilton', league_2, 6018, False)
ground_repository.save(ground_20)
ground_21 = Ground('Ochilview Park', "Queens's Park F.C.", 'Glasgow', league_2, 3746, False)
ground_repository.save(ground_21)
ground_22 = Ground('Balmoral Stadium', 'Cove Rangers F.C.', 'Aberdeen', league_2, 2602, False)
ground_repository.save(ground_22)

# Scottish 3rd
ground_124 = Ground('Excelsior Stadium', 'Airdrieonians F.C.', 'Airdrie', league_16, 10101, False)
ground_repository.save(ground_124)
ground_125 = Ground('Recreation Park', 'Alloa Athletic F.C.', 'Alloa', league_16, 3100, False)
ground_repository.save(ground_125)
ground_126 = Ground('New Douglas Park', 'Clyde F.C.', 'Glasgow', league_16, 6018, False)
ground_repository.save(ground_126)
ground_127 = Ground('East End Park', 'Dunfermline Athletic F.C.', 'Dunfermline', league_16, 11480,  False)
ground_repository.save(ground_127)
ground_128 = Ground('Falkirk Stadium', 'Falkirk F.C.', 'Falkirk', league_16, 7937, False)
ground_repository.save(ground_128)
ground_129 = Ground('Meadowbank Stadium', 'F.C. Edinburgh', 'Edinburgh', league_16, 1280, False)
ground_repository.save(ground_129)
ground_130 = Ground('New Central Park', 'Kelty Hearts F.C.', 'Kelty', league_16, 2181, False)
ground_repository.save(ground_130)
ground_131 = Ground('Links Park', 'Montrose F.C.', 'Montrose', league_16, 4936, False)
ground_repository.save(ground_131)
ground_132 = Ground('Balmoor', 'Peterhead F.C.', 'Peterhead', league_16, 3150, False)
ground_repository.save(ground_132)
ground_133 = Ground('Palmerston Park', 'Queen of the South F.C.', 'Dumfries', league_16, 8690, False)
ground_repository.save(ground_133)

# Scottish 4th
ground_134 = Ground('Cliftonhill', 'Albion Rovers F.C.', 'Coatbridge', league_17, 1238, False)
ground_repository.save(ground_134)
ground_135 = Ground('Galabank', 'Annan Athletic F.C.', 'Annan', league_17, 2504, False)
ground_repository.save(ground_135)
ground_136 = Ground('New Dundas Park', 'Bonnyrigg Rose Athletic F.C.', 'Bonnyrigg', league_17, 2200, False)
ground_repository.save(ground_136)
ground_137 = Ground('Dumbarton Football Stadium', 'Dumbarton F.C.', 'Dumbarton', league_17, 2020,  False)
ground_repository.save(ground_137)
ground_138 = Ground('Bayview Stadium', 'East Fife F.C.', 'Methil', league_17, 1980, False)
ground_repository.save(ground_138)
ground_139 = Ground('Borough Briggs', 'Elgin City F.C.', 'Elgin', league_17, 4520, False)
ground_repository.save(ground_139)
ground_140 = Ground('Station Park', 'Forfar Athletic F.C.', 'Forfar', league_17, 6777, False)
ground_repository.save(ground_140)
ground_141 = Ground('Ochilview', 'Stenhousemuir F.C.', 'Stenhousemuir', league_17, 3746, False)
ground_repository.save(ground_141)
ground_142 = Ground('Forthbank Stadium', 'Stirling Albion F.C.', 'Stirling', league_17, 3808, False)
ground_repository.save(ground_142)
ground_143 = Ground('Stair Park', 'Stranraer F.C.', 'Stranraer', league_17, 4178, False)
ground_repository.save(ground_143)


# England
country_2 = Country('England', "flag")
country_repository.save(country_2)

# English 1st
league_4 = League("Premier League", "logo", country_2, 1)
league_repository.save(league_4)

# English 2nd
league_5 = League("EFL Championship", "logo", country_2, 2)
league_repository.save(league_5)

# English 3rd
league_6 = League("EFL League One", "logo", country_2, 3)
league_repository.save(league_6)

# English 4th
league_7 = League("EFL League Two", "logo", country_2, 4)
league_repository.save(league_7)

# English 5th
league_18 = League("National League", "logo", country_2, 5)
league_repository.save(league_18)

# English 1st
ground_23 = Ground('Old Trafford', 'Manchester United F.C.', 'Manchester', league_4, 74310, False)
ground_repository.save(ground_23)
ground_24 = Ground('Tottenham Hotspur Stadium', "Tottenham Hotspur F.C.", 'London', league_4, 62850, False)
ground_repository.save(ground_24)
ground_25 = Ground('London Stadium', 'West Ham United F.C.', 'London', league_4, 62500, False)
ground_repository.save(ground_25)
ground_26 = Ground('Emirates Stadium', 'Arsenal F.C.', 'London', league_4, 60704, False)
ground_repository.save(ground_26)
ground_27 = Ground('Etihad Stadium', 'Manchester City F.C.', 'Manchester', league_4, 53400, False)
ground_repository.save(ground_27)
ground_28 = Ground('Anfield', 'Liverpool F.C.', 'Liverpool', league_4, 53394, False)
ground_repository.save(ground_28)
ground_29 = Ground("St James' Park", 'Newcastle United F.C.', 'Newcastle', league_4, 52305, False)
ground_repository.save(ground_29)
ground_30 = Ground("Villa Park", 'Aston Villa F.C.', 'Birmingham', league_4, 42749, False)
ground_repository.save(ground_30)
ground_31 = Ground('Stamford Bridge', 'Chelsea F.C.', 'London', league_4, 40341, False)
ground_repository.save(ground_31)
ground_32 = Ground('Goodison Park', "Everton F.C.", 'Liverpool', league_4, 39572, False)
ground_repository.save(ground_32)
ground_33 = Ground('Elland Road', 'Leeds United F.C.', 'Leeds', league_4, 37792, False)
ground_repository.save(ground_33)
ground_34 = Ground("St Mary's Stadium", 'Southampton F.C.', 'Southampton', league_4, 32383, False)
ground_repository.save(ground_34)
ground_35 = Ground("King Power Stadium", 'Leicester City F.C.', 'Leicester', league_4, 32261, False)
ground_repository.save(ground_35)
ground_36 = Ground('Molineux Stadium', 'Wolverhampton Wanderers F.C.', 'Wolverhampton', league_4, 32050, False)
ground_repository.save(ground_36)
ground_37 = Ground('Falmer Stadium', 'Brighton & Hove Albion F.C.', 'Brighton and Hove', league_4, 31800, False)
ground_repository.save(ground_37)
ground_38 = Ground('City Ground', 'Nottingham Forest F.C.', 'Nottingham', league_4, 30445, False)
ground_repository.save(ground_38)
ground_39 = Ground('Craven Cottage', 'Fulham F.C.', 'London', league_4, 25700, False)
ground_repository.save(ground_39)
ground_40 = Ground('Selhurst Park', 'Crystal Palace F.C.', 'London', league_4, 25486, False)
ground_repository.save(ground_40)
ground_41 = Ground('Brentford Community Stadium', 'Brentford F.C.', 'London', league_4, 17250, False)
ground_repository.save(ground_41)
ground_42 = Ground('Vitality Stadium', 'AFC Bournemouth', 'Bournemouth', league_4, 11364, False)
ground_repository.save(ground_42)


# English 2nd
ground_43 = Ground('Stadium of Light', 'Sunderland A.F.C.', 'Sunderland', league_5, 48707, False)
ground_repository.save(ground_43)
ground_44 = Ground('Riverside Stadium', "Middlesbrough F.C.", 'Middlesbrough', league_5, 33746, False)
ground_repository.save(ground_44)
ground_45 = Ground('Cardiff City Stadium', 'Cardiff City F.C.', 'Cardiff', league_5, 33280, False)
ground_repository.save(ground_45)
ground_46 = Ground('Bramall Lane', 'Sheffield United F.C.', 'Sheffield', league_5, 32702, False)
ground_repository.save(ground_46)
ground_47 = Ground('Coventry Building Society Arena', 'Coventry City F.C.', 'Coventry', league_5, 32609, False)
ground_repository.save(ground_47)
ground_48 = Ground('Ewood Park', 'Blackburn Rovers F.C.', 'Blackburn', league_5, 31367, False)
ground_repository.save(ground_48)
ground_49 = Ground("Britannia Stadium", 'Stoke City F.C.', 'Stoke-on-Trent', league_5, 30089, False)
ground_repository.save(ground_49)
ground_50 = Ground("St Andrew's", 'Birmingham City F.C.', 'Birmingham', league_5, 30016, False)
ground_repository.save(ground_50)
ground_51 = Ground('Carrow Road', 'Norwich City F.C.', 'Norwich', league_5, 27244, False)
ground_repository.save(ground_51)
ground_52 = Ground('Ashton Gate', "Bristol City F.C.", 'Bristol', league_5, 27000, False)
ground_repository.save(ground_52)
ground_53 = Ground('The Hawthorns', 'West Bromwich Albion F.C.', 'West Bromwich', league_5, 26850, False)
ground_repository.save(ground_53)
ground_54 = Ground("MKM Stadium", 'Hull City A.F.C.', 'Hull', league_5, 25400, False)
ground_repository.save(ground_54)
ground_55 = Ground("DW Stadium", 'Wigan Athletic F.C.', 'Wigan', league_5, 25138, False)
ground_repository.save(ground_55)
ground_56 = Ground("The John Smith's Stadium", 'Huddersfield Town A.F.C.', 'Huddersfield', league_5, 24500, False)
ground_repository.save(ground_56)
ground_57 = Ground('The Madejski Stadium', 'Reading F.C.', 'Reading', league_5, 24161, False)
ground_repository.save(ground_57)
ground_58 = Ground('Vicarage Road', 'Watford F.C.', 'Watford', league_5, 23700, False)
ground_repository.save(ground_58)
ground_59 = Ground('Deepdale', 'Preston North End F.C.', 'Preston', league_5, 23404, False)
ground_repository.save(ground_59)
ground_60 = Ground('Turf Moor', 'Burnley F.C.', 'Burnley', league_5, 21401, False)
ground_repository.save(ground_60)
ground_61 = Ground('Swansea.com Stadium', 'Swansea City A.F.C.', 'Swansea', league_5, 21088, False)
ground_repository.save(ground_61)
ground_62 = Ground('The Den', 'Millwall F.C.', 'London', league_5, 20146, False)
ground_repository.save(ground_62)
ground_63 = Ground('Loftus Road', 'Queens Park Rangers F.C.', 'London', league_5, 18439, False)
ground_repository.save(ground_63)
ground_64 = Ground('Bloomfield Road', 'Blackpool F.C.', 'Blackpool', league_5, 17338, False)
ground_repository.save(ground_64)
ground_65 = Ground('New York Stadium', 'Rotherham United F.C.', 'Rotherham', league_5, 12021, False)
ground_repository.save(ground_65)
ground_66 = Ground('Kenilworth Road', 'Luton Town F.C.', 'Luton', league_5, 10356, False)
ground_repository.save(ground_66)

# English 3rd
ground_67 = Ground('Hillsborough', 'Sheffield Wednesday F.C.', 'Sheffield', league_6, 39732, False)
ground_repository.save(ground_67)
ground_68 = Ground('Pride Park', "Derby County F.C.", 'Derby', league_6, 33597, False)
ground_repository.save(ground_68)
ground_69 = Ground('Stadium MK', 'Milton Keynes Dons F.C.', 'Milton Keynes', league_6, 30500, False)
ground_repository.save(ground_69)
ground_70 = Ground('Portman Road', 'Ipswich Town F.C.', 'Ipswich', league_6, 29673, False)
ground_repository.save(ground_70)
ground_71 = Ground('University of Bolton Stadium', 'Bolton Wanderers F.C.', 'Bolton', league_6, 28723, False)
ground_repository.save(ground_71)
ground_72 = Ground('The Valley', 'Charlton Athletic F.C.', 'London', league_6, 27111, False)
ground_repository.save(ground_72)
ground_73 = Ground("Oakwell", 'Barnsley F.C.', 'Barnsley', league_6, 23287, False)
ground_repository.save(ground_73)
ground_74 = Ground("Fratton Park", 'Portsmouth F.C.', 'Portsmouth', league_6, 20899, False)
ground_repository.save(ground_74)
ground_75 = Ground('Vale Park', 'Port Vale F.C.', 'Stoke-on-Trent', league_6, 15036, False)
ground_repository.save(ground_75)
ground_76 = Ground('Home Park', "Plymouth Argyle F.C.", 'Plymouth', league_6, 17900, False)
ground_repository.save(ground_76)
ground_77 = Ground('London Road Stadium', 'Peterborough United F.C.', 'Peterborough', league_6, 15314, False)
ground_repository.save(ground_77)
ground_78 = Ground("Kassam Stadium", 'Oxford United F.C.', 'Oxford', league_6, 12500, False)
ground_repository.save(ground_78)
ground_79 = Ground("Memorial Stadium", 'Bristol Rovers F.C.', 'Bristol', league_6, 11000, False)
ground_repository.save(ground_79)
ground_80 = Ground("Adams Park", 'Wycombe Wanderers F.C.', 'High Wycombe', league_6, 9558, False)
ground_repository.save(ground_80)
ground_81 = Ground('Sincil Bank', 'Lincoln Town F.C.', 'Lincoln', league_6, 10780, False)
ground_repository.save(ground_81)
ground_82 = Ground('The New Meadow', 'Shrewsbury Town F.C.', 'Shrewsbury', league_6, 9875, False)
ground_repository.save(ground_82)
ground_83 = Ground('St James Park', 'Exeter City F.C.', 'Exeter', league_6, 8219, False)
ground_repository.save(ground_83)
ground_84 = Ground('Abbey Stadium', 'Cambridge United F.C.', 'Cambridge', league_6, 8127, False)
ground_repository.save(ground_84)
ground_85 = Ground('Whaddon Road', 'Cheltenham Town F.C.', 'Cheltenham', league_6, 7066, False)
ground_repository.save(ground_85)
ground_86 = Ground('Pirelli Stadium', 'Burton Albion F.C.', 'Burton', league_6, 6912, False)
ground_repository.save(ground_86)
ground_87 = Ground('Mazuma Stadium', 'Morecambe F.C.', 'Morecambe', league_6, 6476, False)
ground_repository.save(ground_87)
ground_88 = Ground('Highbury Stadium', 'Fleetwood Town F.C.', 'Fleetwood', league_6, 5327, False)
ground_repository.save(ground_88)
ground_89 = Ground('The New Lawn', 'Forest Green Rovers F.C.', 'Nailsworth', league_6, 5141, False)
ground_repository.save(ground_89)
ground_90 = Ground('Crown Ground', 'Accrington Stanley F.C.', 'Accrington', league_6, 5450, False)
ground_repository.save(ground_90)

# English 4th
ground_91 = Ground('Valley Parade', 'Bradford City', 'Bradford', league_7, 25136, False)
ground_repository.save(ground_91)
ground_92 = Ground('Brunton Park', "Carlisle United F.C.", 'Carlisle', league_7, 17949, False)
ground_repository.save(ground_92)
ground_93 = Ground('Prenton Park', 'Tranmere Rovers F.C.', 'Birkenhead', league_7, 16567, False)
ground_repository.save(ground_93)
ground_94 = Ground('County Ground', 'Swindon Town F.C.', 'Swindon', league_7, 15547, False)
ground_repository.save(ground_94)
ground_95 = Ground('Eco-Power Stadium', 'Doncaster Rover F.C.', 'Doncaster', league_7, 15231, False)
ground_repository.save(ground_95)
ground_96 = Ground('Priestfield Stadium', 'Gillingham F.C.', 'Gillingham', league_7, 11582, False)
ground_repository.save(ground_96)
ground_97 = Ground("Bescot Stadium", 'Walsall F.C.', 'Walsall', league_7, 11300, False)
ground_repository.save(ground_97)
ground_98 = Ground("Edgeley Park", 'Stockport County F.C.', 'Stockport', league_7, 10852, False)
ground_repository.save(ground_98)
ground_99 = Ground('Spotland', 'Rochdale A.F.C.', 'Rochdale', league_7, 10249, False)
ground_repository.save(ground_99)
ground_100 = Ground('Gresty Road', "Crewe Alexandra F.C.", 'Crewe', league_7, 10153, False)
ground_repository.save(ground_100)
ground_101 = Ground('Colchester Community Stadium', 'Colchester United F.C.', 'Colchester', league_7, 10105, False)
ground_repository.save(ground_101)
ground_102 = Ground("Field Mill", 'Mansfield Town F.C.', 'Mansfield', league_7, 9186, False)
ground_repository.save(ground_102)
ground_103 = Ground("Plough Lane", 'AFC Wimbledon', 'London', league_7, 9215, False)
ground_repository.save(ground_103)
ground_104 = Ground("Brisbane Road", 'Leyton Orient F.C.', 'London', league_7, 9271, False)
ground_repository.save(ground_104)
ground_105 = Ground('Blundell Park', 'Grimsby Town F.C.', 'Cleethorpes', league_7, 9002, False)
ground_repository.save(ground_105)
ground_106 = Ground('Suit Direct Stadium', 'Hartlepool United F.C.', 'Hartlepool', league_7, 7858, False)
ground_repository.save(ground_106)
ground_107 = Ground('Rodney Parade', 'Newport County A.F.C.', 'Newport', league_7, 7850, False)
ground_repository.save(ground_107)
ground_108 = Ground('Sixfields Stadium', 'Northampton Town F.C.', 'Northampton', league_7, 7798, False)
ground_repository.save(ground_108)
ground_109 = Ground('VBS Stadium', 'Sutton United F.C.', 'London', league_7, 5013, False)
ground_repository.save(ground_109)
ground_110 = Ground('Broadhall Way', 'Stevenage F.C.', 'Stevenage', league_7, 7800, False)
ground_repository.save(ground_110)
ground_111 = Ground('Broadfield Stadium', 'Crawley Town F.C.', 'Crawley', league_7, 6134, False)
ground_repository.save(ground_111)
ground_112 = Ground('The Peninsula Stadium', 'Salford City F.C.', 'Salford', league_7, 5106, False)
ground_repository.save(ground_112)
ground_113 = Ground('Holker Street', 'Barrow F.C.', 'Barrow-in-Furness', league_7,5400, False)
ground_repository.save(ground_113)
ground_114 = Ground('Wetherby Stadium', 'Harrogate Town A.F.C.', 'Harrogate', league_7, 5000, False)
ground_repository.save(ground_114)

# English 5th
ground_144 = Ground('Recreation Ground', 'Aldershot Town F.C.', 'Aldershot', league_18, 7200, False)
ground_repository.save(ground_144)
ground_145 = Ground('Moss Lane', "Altrincham F.C.", 'Altrincham', league_18, 7700, False)
ground_repository.save(ground_145)
ground_146 = Ground('The Hive Stadium', 'Barnet F.C.', 'London', league_18, 6418, False)
ground_repository.save(ground_146)
ground_147 = Ground('Meadow Park', 'Boreham Wood F.C.', 'Borehamwood', league_18, 4502, False)
ground_repository.save(ground_147)
ground_148 = Ground('Hayes Lane', 'Bromley F.C.', 'London', league_18, 5300, False)
ground_repository.save(ground_148)
ground_149 = Ground('Proact Stadium', 'Chesterfield F.C.', 'Chesterfield', league_18, 10504, False)
ground_repository.save(ground_149)
ground_150 = Ground("Victoria Road", 'Dagenham & Redbridge F.C.', 'London', league_18, 6078, False)
ground_repository.save(ground_150)
ground_151 = Ground("Meadowbank", 'Dorking Wanderers F.C.', 'Dorking', league_18, 3000, False)
ground_repository.save(ground_151)
ground_152 = Ground('Ten Acres', 'Eastleigh F.C.', 'Eastleigh', league_18, 5250, False)
ground_repository.save(ground_152)
ground_153 = Ground('The Shay', "FC Halifax Town", 'Halifax', league_18, 14061, False)
ground_repository.save(ground_153)
ground_154 = Ground('Gateshead International Stadium', 'Gateshead F.C.', 'Gateshead', league_18, 11800, False)
ground_repository.save(ground_154)
ground_155 = Ground("York Road", 'Maidenhead United F.C.', 'Maidenhead', league_18, 4000, False)
ground_repository.save(ground_155)
ground_156 = Ground("Gallagher Stadium", 'Maidstone United F.C.', 'Maidstone', league_18, 4200, False)
ground_repository.save(ground_156)
ground_157 = Ground("Meadow Lane", 'Notts County F.C.', 'Nottingham', league_18, 19588, False)
ground_repository.save(ground_157)
ground_158 = Ground('Boundary Park', 'Oldham Athletic A.F.C.', 'Oldham', league_18, 13513, False)
ground_repository.save(ground_158)
ground_159 = Ground('Damson Park', 'Solihull Moors F.C.', 'Solihull', league_18, 3050, False)
ground_repository.save(ground_159)
ground_160 = Ground('Roots Hall', 'Southend United F.C.', 'Southend-on-Sea', league_18, 12392, False)
ground_repository.save(ground_160)
ground_161 = Ground('Glanford Park', 'Scunthorpe United F.C.', 'Scunthorpe', league_18, 9088, False)
ground_repository.save(ground_161)
ground_162 = Ground('Plainmoor', 'Torquay United F.C.', 'Torquay', league_18, 6500, False)
ground_repository.save(ground_162)
ground_163 = Ground('Grosvenor Vale', 'Wealdstone F.C.', 'London', league_18, 4085, False)
ground_repository.save(ground_163)
ground_164 = Ground('Kingfield Stadium', 'Woking F.C.', 'Woking', league_18, 6036, False)
ground_repository.save(ground_164)
ground_165 = Ground('Racecourse Ground', 'Wrexham A.F.C.', 'Wrexham', league_18, 10771, False)
ground_repository.save(ground_165)
ground_166 = Ground('Huish Park', 'Yeovil Town F.C.', 'Yeovil', league_18, 9566, False)
ground_repository.save(ground_166)
ground_167 = Ground('York Community Stadium', 'York City F.C.', 'York', league_18, 8500, False)
ground_repository.save(ground_167)

# Switzerland
country_3 = Country('Switzerland', "flag")
country_repository.save(country_3)

# Swiss 1st
league_8 = League("Super League", "logo", country_3, 1)
league_repository.save(league_8)

# Swiss 2nd
league_9 = League("Challenge League", "logo", country_3, 2)
league_repository.save(league_9)

# Swiss 3rd
league_10 = League("Promotion League", "logo", country_3, 3)
league_repository.save(league_10)

# Swiss 1st
ground_115 = Ground("St. Jakob-Park", 'FC Basel', 'Basel', league_8, 38512, False)
ground_repository.save(ground_115)
ground_116 = Ground('Wankdorf Stadion', 'BSC Young Boys', 'Bern', league_8, 32000, False)
ground_repository.save(ground_116)
ground_117 = Ground('Stade de Genève', 'Servette FC', 'Geneva', league_8, 30084, False)
ground_repository.save(ground_117)
ground_118 = Ground('Letzigrund', 'FC Zürich / Grasshopper Club Zürich', 'Zürich', league_8, 26104, False)
ground_repository.save(ground_118)
ground_119 = Ground('Kybunpark', 'FC St. Gallen', 'St. Gallen', league_8, 19694, False)
ground_repository.save(ground_119)
ground_120 = Ground('Swissporarena', 'FC Luzern', 'Lucerne', league_8, 17000, False)
ground_repository.save(ground_120)
ground_121 = Ground('Stade Tourbillon', 'FC Sion', 'Sion', league_8, 14500, False)
ground_repository.save(ground_121)
ground_122 = Ground('Schützenwiese', 'FC Winterthur', 'Winterthur', league_8, 8850, False)
ground_repository.save(ground_122)
ground_123 = Ground('Cornaredo Stadium', 'FC Lugano', 'Lugano', league_8, 6330, False)
ground_repository.save(ground_123)

# Swiss 2nd
ground_168 = Ground('Stadion Brügglifeld', 'FC Aarau', 'Aarau', league_9, 8000, False)
ground_repository.save(ground_168)
ground_169 = Ground('Stadio Comunale', "AC Bellinzona", 'Bellinzona', league_9, 5000, False)
ground_repository.save(ground_169)
ground_170 = Ground('Stade Olympique de la Pontaise', 'FC Stade Lausanne Ouchy', 'Lausanne', league_9, 8500, False)
ground_repository.save(ground_170)
ground_171 = Ground('Stade de la Tuilière', 'FC Lausanne-Sport', 'Lausanne', league_9, 12544, False)
ground_repository.save(ground_171)
ground_172 = Ground('Stade de la Maladière', 'Neuchâtel Xamax FCS', 'Neuchâtel', league_9, 12000, False)
ground_repository.save(ground_172)
ground_173 = Ground('LIPO Park Schaffhausen', 'FC Schaffhausen', 'Schaffhausen', league_9, 8085, False)
ground_repository.save(ground_173)
ground_174 = Ground("Stockhorn Arena", 'FC Thun', 'Thun', league_9, 10000, False)
ground_repository.save(ground_174)
ground_175 = Ground("Rheinpark Stadion", 'FC Vaduz', 'Vaduz', league_9, 7584, False)
ground_repository.save(ground_175)
ground_176 = Ground('Sportpark Bergholz', 'FC Wil 1900', 'Wil', league_9, 6010, False)
ground_repository.save(ground_176)
ground_177 = Ground('Stade Municipal', "Yverdon-Sport FC", 'Yverdon-les-Bains', league_9, 6600, False)
ground_repository.save(ground_177)

# Swiss 3rd
ground_178 = Ground('Esp Stadium', 'FC Baden', 'Baden', league_10, 7000, False)
ground_repository.save(ground_178)
ground_179 = Ground('Sportanlage St. Jakob ', "FC Basel II", 'Basel', league_10, 6000, False)
ground_repository.save(ground_179)
ground_180 = Ground('Stade des Peupliers', 'FC Bavois', 'Bavois', league_10, 3000, False)
ground_repository.save(ground_180)
ground_181 = Ground('Tissot Arena', 'FC Biel-Bienne', 'Biel/Bienne', league_10, 5200, False)
ground_repository.save(ground_181)
ground_182 = Ground('Spitalacker', 'Breitenrain', 'Bern', league_10, 1500, False)
ground_repository.save(ground_182)
ground_183 = Ground('Paul-Grüninger-Stadion', 'SC Brühl', 'St. Gallen', league_10, 4200, False)
ground_repository.save(ground_183)
ground_184 = Ground("Stade de Bouleyres", 'SC Bulle', 'Bulle', league_10, 5000, False)
ground_repository.save(ground_184)
ground_185 = Ground("Stadion Eizmoos", 'SC Cham', 'Cham', league_10, 1800, False)
ground_repository.save(ground_185)
ground_186 = Ground('Stadio Comunale', 'FC Chiasso', 'Chiasso', league_10, 11160, False)
ground_repository.save(ground_186)
ground_187 = Ground('Stade de la Fontenette', "Étoile Carouge", 'Carouge', league_10, 3690, False)
ground_repository.save(ground_187)
ground_188 = Ground('Stadion Kleinfeld', 'SC Kriens', 'Kriens', league_10, 5360, False)
ground_repository.save(ground_188)
ground_189 = Ground('Sportanlagen Allmend', 'FC Luzern II', 'Luzern', league_10, 13000, False)
ground_repository.save(ground_189)
ground_190 = Ground('Stadion Grünfeld', 'Rapperswil-Jona', 'Rapperswil', league_10, 2500, False)
ground_repository.save(ground_190)
ground_191 = Ground('Sportanlage Espenmoos', 'FC St. Gallen II', 'St. Gallen', league_10, 5700, False)
ground_repository.save(ground_191)
ground_192 = Ground("Stade de Colovray", 'Stade Nyonnais', 'Nyon', league_10, 7200, False)
ground_repository.save(ground_192)
ground_193 = Ground("	Utogrund", 'YF Juventus', 'Zürich', league_10, 2850, False)
ground_repository.save(ground_193)
ground_194 = Ground('Neufeld', 'BSC Young Boys II', 'Bern', league_10, 14000, False)
ground_repository.save(ground_194)
ground_195 = Ground('Heerenschürli', "FC Zürich II", 'Zürich', league_10, 1120, False)
ground_repository.save(ground_195)



# Italy
country_4 = Country('Italy', "flag")
country_repository.save(country_4)

# Italian 1st
league_11 = League("Serie A", "logo", country_4, 1)
league_repository.save(league_11)

# Italian 2nd
league_12 = League("Serie B", "logo", country_4, 2)
league_repository.save(league_12)

# Italian 3rd A
league_13 = League("Serie C Group A", "logo", country_4, 3)
league_repository.save(league_13)

# Italian 3rd B
league_14 = League("Serie C Group B", "logo", country_4, 3)
league_repository.save(league_14)

# Italian 3rd C
league_15 = League("Serie C Group C", "logo", country_4, 3)
league_repository.save(league_15)

# Italian 1st
ground_196 = Ground('Gewiss Stadium', 'Atalanta B.C.', 'Bergamo', league_11, 21747, False)
ground_repository.save(ground_196)
ground_197 = Ground("Stadio Renato Dall'Ara", "Bologna F.C. 1909", 'Bologna', league_11, 38279, False)
ground_repository.save(ground_197)
ground_198 = Ground('Stadio Giovanni Zini', 'U.S. Cremonese', 'Cremonese', league_11, 20641, False)
ground_repository.save(ground_198)
ground_199 = Ground('Stadio Carlo Castellani', 'Empoli F.C.', 'Empoli', league_11, 16284, False)
ground_repository.save(ground_199)
ground_200 = Ground('Stadio Artemio Franchi', 'ACF Fiorentina', 'Florence', league_11, 43147, False)
ground_repository.save(ground_200)
ground_201 = Ground('Marcantonio Bentegodi', 'Hellas Verona F.C.', 'Verona', league_11, 39211, False)
ground_repository.save(ground_201)
ground_202 = Ground("San Siro", 'Inter Milan', 'Milan', league_11, 75923, False)
ground_repository.save(ground_202)
ground_235 = Ground("San Siro", 'A.C. Milan', 'Milan', league_11, 75923, False)
ground_repository.save(ground_235)
ground_203 = Ground('Juventus Stadium', 'Juventus F.C.', 'Turin', league_11, 41507, False)
ground_repository.save(ground_203)
ground_204 = Ground('Stadio Olimpico', "S.S. Lazio", 'Rome', league_11, 70634, False)
ground_repository.save(ground_204)
ground_205 = Ground('Stadio Via del mare', 'U.S. Lecce', 'Lecce', league_11, 31533, False)
ground_repository.save(ground_205)
ground_206 = Ground("Stadio Brianteo", 'A.C. Monza', 'Monza', league_11, 15039, False)
ground_repository.save(ground_206)
ground_207 = Ground("Stadio Diego Armando Maradona", 'S.S.C. Napoli', 'Naples', league_11, 54726, False)
ground_repository.save(ground_207)
ground_208 = Ground('Stadio Olimpico', 'A.S. Roma', 'Rome', league_11, 70634, False)
ground_repository.save(ground_208)
ground_209 = Ground('Stadio Arechi[', 'U.S. Salernitana 1919', 'Salernitana', league_11, 37800, False)
ground_repository.save(ground_209)
ground_210 = Ground('Stadio Luigi Ferraris', 'U.C. Sampdoria', 'Genoa', league_11, 36536, False)
ground_repository.save(ground_210)
ground_211 = Ground('Mapei Stadium – Città del Tricolore', 'U.S. Sassuolo Calcio', 'Sassuolo', league_11, 21584, False)
ground_repository.save(ground_211)
ground_212 = Ground('Stadio Alberto Picco', 'Spezia Calcio', 'La Spezia', league_11, 11466, False)
ground_repository.save(ground_212)
ground_213 = Ground('Stadio Olimpico Grande Torino', 'Torino F.C.', 'Turin', league_11, 27958, False)
ground_repository.save(ground_213)
ground_214 = Ground('	Stadio Friuli', 'Udinese Calcio', 'Udine', league_11, 25144, False)
ground_repository.save(ground_214)

# Italian 2nd
ground_215 = Ground('Stadio Cino e Lillo Del Duca', 'Ascoli Calcio 1898 F.C.', 'Ascoli Piceno', league_12, 12461, False)
ground_repository.save(ground_215)
ground_216 = Ground('Stadio San Nicola', "S.S.C. Bari", 'Bari', league_12, 58270, False)
ground_repository.save(ground_216)
ground_217 = Ground('Stadio Ciro Vigorito', 'Benevento Calcio', 'Cardiff', league_12, 16867, False)
ground_repository.save(ground_217)
ground_218 = Ground('Stadio Mario Rigamonti', 'Brescia Calcio', 'Brescia', league_12, 19500, False)
ground_repository.save(ground_218)
ground_219 = Ground('Unipol Domus', 'Cagliari Calcio', 'Cagliari', league_12, 16416, False)
ground_repository.save(ground_219)
ground_220 = Ground('Stadio Pier Cesare Tombolato', 'A.S. Cittadella', 'Cittadella', league_12, 7623, False)
ground_repository.save(ground_220)
ground_221 = Ground("Stadio Giuseppe Sinigaglia", 'Como 1907', 'Como', league_12, 13602, False)
ground_repository.save(ground_221)
ground_222 = Ground("Stadio San Vito-Gigi Marulla", 'Cosenza Calcio', 'Cosenza', league_12, 24209, False)
ground_repository.save(ground_222)
ground_223 = Ground('Stadio Benito Stirpe', 'Frosinone Calcio', 'Frosinone', league_12, 16227, False)
ground_repository.save(ground_223)
ground_224 = Ground('Stadio Luigi Ferraris', "Genoa C.F.C.", 'Genoa', league_12, 36599, False)
ground_repository.save(ground_224)
ground_225 = Ground('Stadio Alberto Braglia', 'Modena F.C. 2018', 'Modena', league_12, 21092, False)
ground_repository.save(ground_225)
ground_226 = Ground("Stadio Renzo Barbera", 'Palermo F.C.', 'Palermo', league_12, 36365, False)
ground_repository.save(ground_226)
ground_227 = Ground("Stadio Ennio Tardini", 'Parma Calcio 1913', 'Parma', league_12, 27906, False)
ground_repository.save(ground_227)
ground_228 = Ground("Stadio Renato Curi", 'A.C. Perugia Calcio', 'Perugia', league_12, 23625, False)
ground_repository.save(ground_228)
ground_229 = Ground('Arena Garibaldi', 'Pisa S.C.', 'Pisa', league_12, 25000, False)
ground_repository.save(ground_229)
ground_230 = Ground('Stadio Oreste Granillo', 'Reggina 1914', 'Reggio Calabria', league_12, 27543, False)
ground_repository.save(ground_230)
ground_231 = Ground('Stadio Paolo Mazza', 'S.P.A.L.', 'Ferrara', league_12, 16134, False)
ground_repository.save(ground_231)
ground_232 = Ground('Stadio Druso', 'F.C. Südtirol', 'Bolzano', league_12, 5539, False)
ground_repository.save(ground_232)
ground_233 = Ground('Stadio Libero Liberati', 'Ternana Calcio', 'Terni', league_12, 22000, False)
ground_repository.save(ground_233)
ground_234 = Ground('Stadio Pier Luigi Penzo', 'Venezia F.C.', 'Venice', league_12, 11150, False)
ground_repository.save(ground_234)

# Italian 3rd
ground_236 = Ground('AlbinoLeffe Stadium', 'U.C. AlbinoLeffe', 'Zanica', league_13, 1791, False)
ground_repository.save(ground_236)
ground_237 = Ground('Tommaso Dal Molin Stadium', "F.C. Arzignano Valchiampo", 'Arzignano', league_13, 2000, False)
ground_repository.save(ground_237)
ground_238 = Ground('Stadio Lino Turina', 'Feralpisalò', 'Salò', league_13, 2364, False)
ground_repository.save(ground_238)
ground_239 = Ground('Stadio Giuseppe Moccagatta', 'Juventus Next Gen', 'Alessandria', league_13, 5827, False)
ground_repository.save(ground_239)
ground_240 = Ground('Stadio Rigamonti-Ceppi', 'Calcio Lecco 1912', 'Lecco', league_13, 4997, False)
ground_repository.save(ground_240)
ground_241 = Ground('Stadio Danilo Martelli', 'Mantova 1911', 'Mantua', league_13, 14884, False)
ground_repository.save(ground_241)
ground_242 = Ground("Stadio Silvio Piola", 'Novara F.C.', 'Novara', league_13, 17875, False)
ground_repository.save(ground_242)
ground_243 = Ground("Stadio Euganeo", 'Calcio Padova', 'Padua', league_13, 32420, False)
ground_repository.save(ground_243)
ground_244 = Ground('Stadio Giuseppe Voltini', 'U.S. Pergolettese 1932', 'Crema', league_13, 4095, False)
ground_repository.save(ground_244)
ground_245 = Ground('Stadio Leonardo Garilli', "Piacenza Calcio 1919", 'Piacenza', league_13, 21668, False)
ground_repository.save(ground_245)
ground_246 = Ground('Stadio Guido Teghil', 'Pordenone Calcio', 'Pordenone', league_13, 5000, False)
ground_repository.save(ground_246)
ground_247 = Ground("Stadio Carlo Speroni", 'Aurora Pro Patria 1919', 'Busto Arsizio', league_13, 4627, False)
ground_repository.save(ground_247)
ground_248 = Ground("Stadio Breda", 'Pro Sesto 1913 / F.C. Sangiuliano City', 'Sesto San Giovanni', league_13, 4500, False)
ground_repository.save(ground_248)
ground_249 = Ground("	Stadio Silvio Piola", 'F.C. Pro Vercelli 1892', 'Vercelli', league_13, 5500, False)
ground_repository.save(ground_249)
ground_250 = Ground('Stadio Città di Meda', 'A.C. Renate', 'Meda', league_13, 3000, False)
ground_repository.save(ground_250)
ground_251 = Ground('Stadio Briamasco', 'A.C. Trento 1921', 'Trento', league_13, 4227, False)
ground_repository.save(ground_251)
ground_252 = Ground('Stadio Nereo Rocco', 'U.S. Triestina Calcio 1918', 'Triestina', league_13, 24500, False)
ground_repository.save(ground_252)
ground_253 = Ground('Stadio Romeo Menti', 'L.R. Vicenza', 'Vicenza', league_13, 12000, False)
ground_repository.save(ground_253)
ground_254 = Ground('Stadio Gavagnin Nocini', 'Virtus Verona', 'Verona', league_13, 1200, False)
ground_repository.save(ground_254)



pdb.set_trace()