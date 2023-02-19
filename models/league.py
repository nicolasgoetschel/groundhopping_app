class League:
    def __init__(self, name, logo, football_grounds, id = None):
        self.name = name
        self.logo = logo
        self.grounds = football_grounds or []
        self.id = id