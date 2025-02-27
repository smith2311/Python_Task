from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}
        self.reserved_books = {}
        self.borrowing_history = {}
        self.penalties = {}

    def add_book(self, title, author, quantity):
        if title in self.books:
            self.books[title] = (author, self.books[title][1] + quantity)
        else:
            self.books[title] = (author, quantity)
        print(f'Book "{title}" added successfully!')

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f'Book "{title}" removed successfully!')
        else:
            print("Error: Book not found in the library.")

    def update_book(self, title, author=None, quantity=None):
        if title in self.books:
            current_author, current_quantity = self.books[title]
            self.books[title] = (author if author else current_author,
                                 quantity if quantity is not None else current_quantity)
            print(f'Book "{title}" updated successfully!')
        else:
            print("Error: Book not found in the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("\nAvailable Books:")
        for title, (author, quantity) in self.books.items():
            print(f'Title: {title}, Author: {author}, Quantity: {quantity}')

    def search_book(self, title):
        if title in self.books:
            author, quantity = self.books[title]
            print(f'Book Found - Title: {title}, Author: {author}, Quantity: {quantity}')
        else:
            print("Error: Book not found in the library.")

    def borrow_book(self, user_name, title):
        if user_name not in self.borrowed_books:
            self.borrowed_books[user_name] = {}

        if len(self.borrowed_books[user_name]) >= 3:
            print("You can only borrow a maximum of 3 books at a time.")
            return

        if title in self.books and self.books[title][1] > 0:
            borrow_date = datetime.now()
            due_date = borrow_date + timedelta(days=14)
            self.borrowed_books[user_name][title] = {'borrow_date': borrow_date, 'due_date': due_date}
            self.books[title] = (self.books[title][0], self.books[title][1] - 1)
            self.borrowing_history.setdefault(user_name, []).append(title)
            print(f'Book "{title}" borrowed successfully by {user_name}! Due date: {due_date.strftime("%Y-%m-%d")}')
        else:
            print("Book not available for borrowing.")
            self.reserve_book(user_name, title)

    def return_book(self, user_name, title):
        if user_name in self.borrowed_books and title in self.borrowed_books[user_name]:
            borrow_info = self.borrowed_books[user_name].pop(title)
            return_date = datetime.now()

            if return_date > borrow_info['due_date']:
                penalty_days = (return_date - borrow_info['due_date']).days
                self.penalties[user_name] = self.penalties.get(user_name, 0) + penalty_days * 5
                print(f'Late return! Penalty applied: {penalty_days * 5} units.')

            if not self.borrowed_books[user_name]:
                del self.borrowed_books[user_name]

            self.books[title] = (self.books[title][0], self.books[title][1] + 1)
            print(f'Book "{title}" returned successfully by {user_name}!')
            self.notify_reserved_users(title)
        else:
            print("Book not borrowed or incorrect user.")

    def reserve_book(self, user_name, title):
        if title not in self.reserved_books:
            self.reserved_books[title] = []
        if user_name not in self.reserved_books[title]:
            self.reserved_books[title].append(user_name)
            print(f'Book "{title}" is out of stock. {user_name} has been added to the reservation queue.')

    def notify_reserved_users(self, title):
        if title in self.reserved_books and self.reserved_books[title]:
            next_user = self.reserved_books[title].pop(0)
            print(f'Notification: {next_user}, the book "{title}" is now available for borrowing!')

    def view_borrowed_books(self, user_name):
        if user_name in self.borrowed_books:
            print(f'Books borrowed by {user_name}:')
            for title, details in self.borrowed_books[user_name].items():
                print(f'Title: {title}, Borrowed on: {details["borrow_date"].strftime("%Y-%m-%d")}, Due on: {details["due_date"].strftime("%Y-%m-%d")}')
        else:
            print(f'No books borrowed by {user_name}.')

    def view_borrowing_history(self, user_name):
        if user_name in self.borrowing_history:
            print(f'Borrowing history of {user_name}: {self.borrowing_history[user_name]}')
        else:
            print("No borrowing history found.")


library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Update Book")
    print("4. Display Books")
    print("5. Search Book")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. View Borrowed Books")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        quantity = int(input("Enter book quantity: "))
        library.add_book(title, author, quantity)
    elif choice == "2":
        title = input("Enter book title to remove: ")
        library.remove_book(title)
    elif choice == "3":
        title = input("Enter book title to update: ")
        author = input("Enter new author (or press enter to keep the same): ") or None
        quantity = input("Enter new quantity (or press enter to keep the same): ")
        quantity = int(quantity) if quantity else None
        library.update_book(title, author, quantity)
    elif choice == "4":
        library.display_books()
    elif choice == "5":
        title = input("Enter book title to search: ")
        library.search_book(title)
    elif choice == "6":
        user_name = input("Enter your name: ")
        title = input("Enter book title to borrow: ")
        library.borrow_book(user_name, title)
    elif choice == "7":
        user_name = input("Enter your name: ")
        title = input("Enter book title to return: ")
        library.return_book(user_name, title)
    elif choice == "8":
        user_name = input("Enter your name: ")
        library.view_borrowed_books(user_name)
    elif choice == "9":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 9.")
