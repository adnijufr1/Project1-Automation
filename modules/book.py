from modules.LibraryItem import LibraryItem

class Book(LibraryItem):
    def __init__ (self,title,subject,upc,isbn,authors,dds_number):
        LibraryItem.__init__(self,title,upc,subject)
        self.isbn = isbn
        self.authors = authors
        self.dds_number = dds_number
