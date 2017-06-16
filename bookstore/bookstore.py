class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def get_books(self):
        return self.books
    
    def add_book(self, book):
        self.books.append(book)
        
        
    def search_books(self, title=None, author=None):
        results = []
        if title and author:
            for book in self.books:
                if str.lower(title) in str.lower(book.title) and author == book.author: #thanks Jason! :D
                    results.append(book)
        elif title:
            for book in self.books:
                if str.lower(title) in str.lower(book.title):
                    results.append(book)
        elif author:
            for book in self.books:
                if author == book.author:
                    results.append(book)
        else:
            return 'Error. No search parameters provided.'
        return results
        
        
       
       
        #for book in self.books:
          #  if title in book.title:
              #  results.add(book)
       # for book in self.books:
          #  if title in book.title or author == book.author:
             #   results.add(book)
      #  for book in self.books:
           # if author == book.author:
             #   results.add(book)
       # return results 





class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    
    def get_books(self):
        return self.books



class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
