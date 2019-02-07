class Oceans():

    # The ocean is a dictionary with keys and values of ships.
    def create_ocean(self):
        self.__ocean = { 1:'O', 2:'O', 3:'O', 4:'O', 5:'O', 6:'O'}
    
    # Initialise the ocean.
    def __init__(self):
        self.create_ocean()

    # Override and print the ocean.
    def __str__(self):
        