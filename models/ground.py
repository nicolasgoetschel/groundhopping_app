class Ground:
    def __init__(self, name, team, location, league, capacity, visited=False, id = None):
        self.name = name
        self.team = team
        self.location = location
        self.league = league
        self.capacity = capacity
        self.visited = visited
        self.id = id


    def toggle_visited(self, visited):
        self.visited = visited

    def change_name(self, name):
        self.name = name
   
    def change_capacity(self, capacity):
        self.capacity = capacity
   
    def change_league(self, league):
        self.league = league