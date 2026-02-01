class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def issue(self):
        if self.copies > 0:
            self.copies -= 1
            print("Book issued!")
        else:
            print("Book not available!")

    def return_book(self):
        self.copies += 1
        print("Book returned!")

    def check(self):
        return self.copies > 0


b1 = Book("Python", "Guido", 1234, 2)

print("Before Issue:", b1.copies)
b1.issue()
print("After Issue:", b1.copies)

b1.return_book()
print("After Return:", b1.copies)
