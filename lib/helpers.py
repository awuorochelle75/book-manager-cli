# lib/helpers.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import User, Book, BorrowRecord
from datetime import datetime

# Setup DB connection and session
engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

# -----------------------
# USER FUNCTIONS
# -----------------------

def list_all_users():
    users = session.query(User).all()
    if not users:
        print("No users found.")
    else:
        for user in users:
            print(f"{user.id}. {user.name}")

def find_user_by_name(name):
    user = session.query(User).filter_by(name=name).first()
    if user:
        print(f"✅ Found: {user.id} - {user.name}")
    else:
        print("❌ No user found with that name.")

def find_user_by_id(user_id):
    user = session.query(User).get(user_id)
    if user:
        print(f"✅ Found: {user.id} - {user.name}")
    else:
        print("❌ No user found with that ID.")

def create_user(name):
    user = User(name=name)
    session.add(user)
    session.commit()
    print(f"✅ User '{name}' created.")

def update_user(user_id, new_name):
    user = session.query(User).get(user_id)
    if user:
        user.name = new_name
        session.commit()
        print("✅ User updated.")
    else:
        print("❌ User not found.")

def delete_user(user_id):
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        print("✅ User deleted.")
    else:
        print("❌ User not found.")

# -----------------------
# BOOK FUNCTIONS
# -----------------------

def list_all_books():
    books = session.query(Book).all()
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"{book.id}. {book.title} by {book.author} - Status: {book.status}")

def find_book_by_title(title):
    book = session.query(Book).filter_by(title=title).first()
    if book:
        print(f"✅ Found: {book.id}. {book.title} by {book.author} - {book.status}")
    else:
        print("❌ No book found with that title.")

def find_book_by_id(book_id):
    book = session.query(Book).get(book_id)
    if book:
        print(f"✅ Found: {book.id}. {book.title} by {book.author} - {book.status}")
    else:
        print("❌ No book found with that ID.")

def create_book(title, author):
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    print(f"✅ Book '{title}' added.")

def update_book(book_id, new_title, new_author):
    book = session.query(Book).get(book_id)
    if book:
        book.title = new_title
        book.author = new_author
        session.commit()
        print("✅ Book updated.")
    else:
        print("❌ Book not found.")

def delete_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        print("✅ Book deleted.")
    else:
        print("❌ Book not found.")

# -----------------------
# BORROWING FUNCTIONS
# -----------------------

def list_all_borrow_records():
    records = session.query(BorrowRecord).all()
    if not records:
        print("No borrow records.")
    else:
        for record in records:
            print(f"Book: '{record.book.title}' | User: {record.user.name} | Date: {record.borrow_date.date()}")

def borrow_book(user_id, book_id):
    user = session.query(User).get(user_id)
    book = session.query(Book).get(book_id)

    if not user or not book:
        print("❌ User or book not found.")
        return
    if book.status == "borrowed":
        print("❌ Book is already borrowed.")
        return

    borrow_record = BorrowRecord(user_id=user.id, book_id=book.id, borrow_date=datetime.now())
    book.status = "borrowed"
    session.add(borrow_record)
    session.commit()
    print(f"✅ '{book.title}' borrowed by {user.name}.")

def return_book(book_id):
    book = session.query(Book).get(book_id)
    if not book:
        print("❌ Book not found.")
        return

    record = session.query(BorrowRecord).filter_by(book_id=book_id).first()
    if not record:
        print("❌ Borrow record not found.")
        return

    session.delete(record)
    book.status = "available"
    session.commit()
    print(f"✅ '{book.title}' returned.")

def list_books_borrowed_by_user(user_id):
    user = session.query(User).get(user_id)
    if not user:
        print("❌ User not found.")
        return

    records = session.query(BorrowRecord).filter_by(user_id=user_id).all()
    if not records:
        print(f"{user.name} has not borrowed any books.")
    else:
        print(f"📚 Books borrowed by {user.name}:")
        for record in records:
            print(f"- {record.book.title} on {record.borrow_date.date()}")
