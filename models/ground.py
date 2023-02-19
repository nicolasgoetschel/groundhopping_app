class Ground:
    def __init__(self, name, team, location, capacity, visited=False, id = None):
        self.name = name
        self.team = team
        self.location = location
        self.capacity = capacity
        self.visited = visited
        self.id = id