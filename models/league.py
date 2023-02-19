class League:
    def __init__(self, name, logo, grounds, id = None):
        self.name = name
        self.logo = logo
        self.grounds = grounds or []
        self.id = id