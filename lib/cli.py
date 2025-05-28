# cli.py

from helpers import (
    list_all_users, find_user_by_name, find_user_by_id, create_user,
    update_user, delete_user, list_all_books, find_book_by_title,
    find_book_by_id, create_book, update_book, delete_book,
    list_all_borrow_records, borrow_book, return_book,
    list_books_borrowed_by_user
)

class UserCLI:
    def menu(self):
        print("\nUser Menu:")
        print("1. List all users")
        print("2. Find user by name")
        print("3. Find user by id")
        print("4. Create user")
        print("5. Update user")
        print("6. Delete user")
        print("0. Back")

    def run(self):
        while True:
            self.menu()
            choice = input("> ").strip()
            if choice == "0":
                break
            elif choice == "1":
                list_all_users()
            elif choice == "2":
                name = input("Enter user name: ").strip()
                find_user_by_name(name)
            elif choice == "3":
                try:
                    user_id = int(input("Enter user ID: "))
                    find_user_by_id(user_id)
                except ValueError:
                    print("❌ Invalid user ID. Please enter a number.")
            elif choice == "4":
                name = input("Enter new user name: ").strip()
                if name:
                    create_user(name)
                else:
                    print("❌ User name cannot be empty.")
            elif choice == "5":
                try:
                    user_id = int(input("Enter user ID to update: "))
                    new_name = input("Enter new name: ").strip()
                    if new_name:
                        update_user(user_id, new_name)
                    else:
                        print("❌ New name cannot be empty.")
                except ValueError:
                    print("❌ Invalid user ID. Please enter a number.")
            elif choice == "6":
                try:
                    user_id = int(input("Enter user ID to delete: "))
                    confirm = input(f"Are you sure you want to delete user {user_id}? (y/n): ").lower()
                    if confirm == 'y':
                        delete_user(user_id)
                    else:
                        print("Deletion cancelled.")
                except ValueError:
                    print("❌ Invalid user ID. Please enter a number.")
            else:
                print("❌ Invalid option. Please try again.")

class BookCLI:
    def menu(self):
        print("\nBook Menu:")
        print("1. List all books")
        print("2. Find book by title")
        print("3. Find book by id")
        print("4. Create book")
        print("5. Update book")
        print("6. Delete book")
        print("0. Back")

    def run(self):
        while True:
            self.menu()
            choice = input("> ").strip()
            if choice == "0":
                break
            elif choice == "1":
                list_all_books()
            elif choice == "2":
                title = input("Enter book title: ").strip()
                find_book_by_title(title)
            elif choice == "3":
                try:
                    book_id = int(input("Enter book ID: "))
                    find_book_by_id(book_id)
                except ValueError:
                    print("❌ Invalid book ID. Please enter a number.")
            elif choice == "4":
                title = input("Enter book title: ").strip()
                author = input("Enter author name: ").strip()
                if title and author:
                    create_book(title, author)
                else:
                    print("❌ Title and author cannot be empty.")
            elif choice == "5":
                try:
                    book_id = int(input("Enter book ID to update: "))
                    new_title = input("Enter new title: ").strip()
                    new_author = input("Enter new author: ").strip()
                    if new_title and new_author:
                        update_book(book_id, new_title, new_author)
                    else:
                        print("❌ New title and author cannot be empty.")
                except ValueError:
                    print("❌ Invalid book ID. Please enter a number.")
            elif choice == "6":
                try:
                    book_id = int(input("Enter book ID to delete: "))
                    confirm = input(f"Are you sure you want to delete book {book_id}? (y/n): ").lower()
                    if confirm == 'y':
                        delete_book(book_id)
                    else:
                        print("Deletion cancelled.")
                except ValueError:
                    print("❌ Invalid book ID. Please enter a number.")
            else:
                print("❌ Invalid option. Please try again.")

class BorrowCLI:
    def menu(self):
        print("\nBorrow Records Menu:")
        print("1. List all borrow records")
        print("2. Borrow a book (create borrow record)")
        print("3. Return a book (delete borrow record)")
        print("4. List books borrowed by a user")
        print("0. Back")

    def run(self):
        while True:
            self.menu()
            choice = input("> ").strip()
            if choice == "0":
                break
            elif choice == "1":
                list_all_borrow_records()
            elif choice == "2":
                try:
                    user_id = int(input("Enter user ID: "))
                    book_id = int(input("Enter book ID: "))
                    borrow_book(user_id, book_id)
                except ValueError:
                    print("❌ Invalid input. Please enter numeric IDs.")
            elif choice == "3":
                try:
                    book_id = int(input("Enter book ID to return: "))
                    return_book(book_id)
                except ValueError:
                    print("❌ Invalid book ID. Please enter a number.")
            elif choice == "4":
                try:
                    user_id = int(input("Enter user ID: "))
                    list_books_borrowed_by_user(user_id)
                except ValueError:
                    print("❌ Invalid user ID. Please enter a number.")
            else:
                print("❌ Invalid option. Please try again.")

class MainCLI:
    def __init__(self):
        self.user_cli = UserCLI()
        self.book_cli = BookCLI()
        self.borrow_cli = BorrowCLI()

    def menu(self):
        print("\nMain Menu:")
        print("1. Users")
        print("2. Books")
        print("3. Borrow Records")
        print("0. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("> ").strip()
            if choice == "0":
                print("👋 Exiting... Goodbye!")
                break
            elif choice == "1":
                self.user_cli.run()
            elif choice == "2":
                self.book_cli.run()
            elif choice == "3":
                self.borrow_cli.run()
            else:
                print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    MainCLI().run()
