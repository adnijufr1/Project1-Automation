from modules.LibraryItem import LibraryItem


class Cd(LibraryItem):
    def __init__ (self,title, subject, upc, artist):
        LibraryItem.__init__(self,title,upc,subject)
        self.artist = artist
