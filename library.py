class Library:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.availability_status = True  # True indicates the book is available

    def check_out(self):
        if self.availability_status:
            self.availability_status = False
            print(f"You have successfully checked out '{self.book_name}'.")
        else:
            print(f"Sorry, '{self.book_name}' is currently not available.")

    def return_book(self):
        self.availability_status = True
        print(f"You have successfully returned '{self.book_name}'.")

    def display_available_books(self):
        status = "Available" if self.availability_status else "Checked Out"
        print(f"Book: {self.book_name} | Author: {self.author} | Status: {status}")

def main():
    # Initialize book objects
    book1 = Library("The Alchemist", "Paulo Coelho")
    book2 = Library("Wings Of Fire", "Dr. APJ Abdul Kalam")
    book3 = Library("Death Note", "Tsugumi Ohba")

    print("--- Initial Library Status ---")
    book1.display_available_books()
    book2.display_available_books()
    book3.display_available_books()

    print("\n--- Performing Operations ---")
    book1.check_out()
    book1.check_out()  # Attempt to check out again
    book2.check_out()

    print("\n--- Returning a Book ---")
    book1.return_book()

    print("\n--- Final Library Status ---")
    book1.display_available_books()
    book2.display_available_books()
    book3.display_available_books()

if __name__ == "__main__":
    main()

        
