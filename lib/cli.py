# main.py

from helpers import (
    list_all_users, find_user_by_name, find_user_by_id, create_user,
    update_user, delete_user, list_all_books, find_book_by_title,
    find_book_by_id, create_book, update_book, delete_book,
    list_all_borrow_records, borrow_book, return_book,
    list_books_borrowed_by_user
)

def menu():
    print("\nPlease select an option:")
    print("0. Exit")
    print("1. List all users")
    print("2. Find user by name")
    print("3. Find user by id")
    print("4. Create user")
    print("5. Update user")
    print("6. Delete user")
    print("7. List all books")
    print("8. Find book by title")
    print("9. Find book by id")
    print("10. Create book")
    print("11. Update book")
    print("12. Delete book")
    print("13. List all borrow records")
    print("14. Borrow a book (create borrow record)")
    print("15. Return a book (delete borrow record)")
    print("16. List books borrowed by a user")

def main():
    while True:
        menu()
        choice = input("> ")

        if choice == "0":
            print("👋 Exiting... Goodbye!")
            break

        elif choice == "1":
            list_all_users()

        elif choice == "2":
            name = input("Enter user name: ")
            find_user_by_name(name)

        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            find_user_by_id(user_id)

        elif choice == "4":
            name = input("Enter new user name: ")
            create_user(name)

        elif choice == "5":
            user_id = int(input("Enter user ID to update: "))
            new_name = input("Enter new name: ")
            update_user(user_id, new_name)

        elif choice == "6":
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)

        elif choice == "7":
            list_all_books()

        elif choice == "8":
            title = input("Enter book title: ")
            find_book_by_title(title)

        elif choice == "9":
            book_id = int(input("Enter book ID: "))
            find_book_by_id(book_id)

        elif choice == "10":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            create_book(title, author)

        elif choice == "11":
            book_id = int(input("Enter book ID to update: "))
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            update_book(book_id, new_title, new_author)

        elif choice == "12":
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)

        elif choice == "13":
            list_all_borrow_records()

        elif choice == "14":
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            borrow_book(user_id, book_id)

        elif choice == "15":
            book_id = int(input("Enter book ID to return: "))
            return_book(book_id)

        elif choice == "16":
            user_id = int(input("Enter user ID: "))
            list_books_borrowed_by_user(user_id)

        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
