class Country:
    def __init__(self, name, flag, leagues, id = None):
        self.name = name
        self.flag = flag
        self.leagues = leagues or []
        self.id = id