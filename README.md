# Book Management System
- A Command-Line Book Manager for Libraries and Bookshops.

## Problem Statement

- Libraries,readers,and small bookshops often struggle to keep track of books,users and borrow records.Without a dedicated system,it becomes easy to lose records or forget who borrowed a book.


***

## Features

### Book Management
- List all books.
- Find book by title or ID.
- Add new books with details like title and author.
- Update existing book information.
- Delete a book.
- Check which books are currently available or borrowed.

### User Management
- List all users.
- Find users by name or ID
- Create new users
- Update user information.
- Delete users.
- View which books each user has borrowed.

### Borrowing and returning
- Borrow a book(create a borrow record)
- Return a book(delete borrow record)
- View all borrow records
- List books borrowed by a specific user



## Menu Options
- When you run the CLI, you'll be presented with the following options:
 - Please select an option:

   0. Exit

   1.List all users

   2.Find user by name

   3.Find user by id

   4.Create user

   5.Update user

   6.Delete user

   7.List all books

   8.Find book by title

   9.Find book by id

   10.Create book

   11.Update book

   12.Delete book

   13.List all borrow records

   14.Borrow a book (create borrow record)

   15.Return a book (delete borrow record)

   16.List books borrowed by a user


## Technologies used
- Python 3
- SQLAlchemy ORM
- SQLite


## `cli.py`
The main interactive script.Presents the user menu and calls the appropriate functions based on user input.Handles the control flow of the entire application.

### `models.py`
Defines the SQLAlchemy models:
- `User` : stores user information.
- `Book` : stores book information.
- `Borrow` : tracks which user borrowed which book.


### `database.py`
Initilizes the database,creates tables and establishes a session for database transactions.

### `helpers.py`
Contains helper functions for each operation:
- `list_users()`, `create_user()`, `update_user()` etc.
- `list_books()`, `create_book()`, `find_book_by_title()`, etc
- `borrow_book()`, `return_book()`, `list_borrow_records()`, etc.

## How to Run
### Getting Started 
1. **Clone the repository**   
Open your terminal and run the following command:
    ```sh
    $git clone https://github.com/awuorochelle75/book-manager-cli.git

2. **Navigate to the project folder**
    ```sh
        $cd book-manager-cli

3. **Set up and activate a virtual environment with pipenv**
    ```sh
        $pipenv install
        $pipenv shell

4. **Set up the database**
    ```sh
        $pipenv install sqlalchemy alembic
        $alembic init migrations


5.  **Seed the database**
    ```sh
        $python seed.py

## **Run the application**
1. You can run the CLI using:
     ```sh
        $python cli.py

## Contact Information
 Email: awuorochelle@gmail.com


## License
 MIT License @2025 Rochelle Awuor










