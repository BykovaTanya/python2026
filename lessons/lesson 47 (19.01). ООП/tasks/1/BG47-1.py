class Book:
      
    def __init__(self, title, auvtor, pages):
        self.title = title
        self.auvtor = auvtor
        self.pages = pages

    def open(self):
        print(f"книга '{self.title}' открыта на первой странице.")

    def read(self):
        print(f"Читаем книгу '{self.title}' автора {self.auvtor}.")

    def close(self):
        print(f"Книга '{self.title}' закрыта.")

    def info(self):
        print(f"'{self.title}' - {self.auvtor}, {self.pages} стр.")    

my_book = Book("1984", "Джордж Оруэлл", 328)
my_book.open()
my_book.read()
my_book.close()
my_book.info()
