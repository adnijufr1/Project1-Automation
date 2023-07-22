from modules.LibraryItem import LibraryItem


class Magazine(LibraryItem):
    def __init__(self, title, subject,upc,volume, issue):
        LibraryItem.__init__(self,title,upc,subject)
        self.volume = volume
        self.issue = issue