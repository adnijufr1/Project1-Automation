from modules.LibraryItem import LibraryItem


class Dvd(LibraryItem):
    def __init__ (self, title, subject, upc, actors, director, genre):
        LibraryItem.__init__(self,title,upc,subject)
        self.actors = actors
        self.director = director
        self.genre = genre
