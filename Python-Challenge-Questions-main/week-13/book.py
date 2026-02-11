class Book:

    def __init__(self, name, authored, piece, price):
        self.name = name
        self.authored = authored
        self.piece = piece
        self.price = price

    def drop_book(self, numb):
        """This method runs when a book is removed from stock."""
        self.piece -= numb

    def add_book(self, numb):
        """This method runs when a book is added to stock"""
        self.piece += numb

    def change_price(self, new_price):
        """This method updates the price of the book"""
        self.price = new_price

    def display(self):
        """Returns a string containing the name,authored,price and piece."""
        return f"There are {self.piece} of the ${self.price} book, called {self.name} and the publisher is {self.authored}"
