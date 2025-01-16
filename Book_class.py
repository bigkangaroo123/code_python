class Books:
    def __init__(self, title, author, pages, year, genre):
        self.__title = title
        self.__author = author
        self.__pages = pages
        self.__year = year
        self.__genre = genre
    
    @property
    def get_title(self):
        return self.__title
    
    @property
    def get_author(self):
        return self.__author
        
    @property
    def get_pages(self):
        return self.__pages
        
    @property
    def get_year(self):
        return self.__year
        
    @property
    def get_genre(self):
        return self.__genre
        
    def get_info(self):
        book = {
            1 : self.__title,
            2 : self.__author,
            3 : self.__pages,
            4 : self.__year,
            5 : self.__genre
        }
        return book

book1 = Books("Never Let Me Go", "Kazuo Ishiguro", 288, "4/5/2005", 'SciFi')
book_info = book1.get_info()
for key in list(book_info):
    print(book_info[key])
