
class Book:
    def __init__(self, title, author, genre, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def get_info(self):
        return f"{self.title} — {self.author}, {self.genre}, {self.price} руб."
    
    def apply_discount(self, percent):
        return self.price * (1 - percent / 100)
