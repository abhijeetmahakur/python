class Ticket:
    def __init__(self, movie, showtime, seat, price):
        self.movie = movie
        self.showtime = showtime
        self.seat = seat
        self.price = price

    def display(self):
        print(f"Movie: {self.movie}, Show: {self.showtime}, Seat: {self.seat}, Price: {self.price}")

    def total(self, qty):
        return self.price * qty


t1 = Ticket("Avengers", "7:00 PM", "A12", 250)
t2 = Ticket("Avengers", "7:00 PM", "A13", 250)

t1.display()
t2.display()

total_amount = t1.price + t2.price
print("Total Amount to Pay:", total_amount)
