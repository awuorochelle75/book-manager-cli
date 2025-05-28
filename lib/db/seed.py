import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Book, User, BorrowRecord
from datetime import datetime

# Connect to the database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # This gets the directory where seed.py lives
DB_PATH = os.path.join(BASE_DIR, 'app.db')            # Path to the app.db in the same folder as seed.py

engine = create_engine(f'sqlite:///{DB_PATH}')
Session = sessionmaker(bind=engine)
session = Session()

# Drop all existing data (optional: for resetting)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# --- Sample Users ---
user1 = User(name="Alice Johnson")
user2 = User(name="Bob Smith")
user3 = User(name="Clara Kibet")
user4 = User(name="David Kimani")
user5 = User(name="Eva Mwangi")

# --- Sample Books ---
book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee")
book3 = Book(title="1984", author="George Orwell")
book4 = Book(title="Siku Njema", author="Ken Walibora")
book5 = Book(title="The River and the Source", author="Margaret Ogola")
book6 = Book(title="The Psychology of Money", author="Morgan Housel")
book7 = Book(title="From Zero To Millionaire", author="Nicolas Bérubé")
book8 = Book(title="Versity", author="Coleen Hover")
book9 = Book(title="The Chronicles of Narnia", author="C.S. Lewis")
book10 = Book(title="The Art Of Murder", author="Rick Wood")
book11 = Book(title="Right Behind You", author="Morgan Housel")
book12 = Book(title="What We Forgot To Bury", author="Marin Montgomery")
book13 = Book(title="The Two Towers", author="J.R.R. Tolkien")
book14 = Book(title="Her Final Hour", author="Karla Kovach")
book15 = Book(title="Priest", author="Sierra Simone")
book16 = Book(title="The Sweetest Oblivion", author="Danielle Lori")
book17 = Book(title="The Silver Crow", author="Trif Premade")
book18 = Book(title="The Turning Point", author="Julia Ash")
book19 = Book(title="Incursion", author="Kevin and Elizabeth McLaughlin")
book20 = Book(title="A Parallel Universe", author="Author Name")
book21 = Book(title="The Wife Between Us", author="Greer Hendricks & Sarah Pekkanen")
book22 = Book(title="Every Last Year", author="Alex Finlay")
book23 = Book(title="The Inmate", author="Freida McFadden")
book24 = Book(title="The Housemaid's Wedding", author="Freida McFadden")
book25 = Book(title="The Silent Patient", author="Alex Michaelides")

# --- Sample BorrowRecords ---

# Add all users, books, and borrow records to the session
session.add_all([user1, user2, user3, user4, user5])

session.add_all([
    book1, book2, book3, book4, book5,
    book6, book7, book8, book9, book10,
    book11, book12, book13, book14, book15,
    book16, book17, book18, book19, book20,
    book21, book22, book23, book24, book25
])


# Commit changes
session.commit()

BorrowRecord.create(session, user1, book1)
BorrowRecord.create(session, user2, book3)



print("✅ Seeded the database successfully!")
