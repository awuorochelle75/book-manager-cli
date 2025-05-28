from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime
from sqlalchemy import create_engine

Base = declarative_base()

# -----------------------
# Book Model
# -----------------------
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    status = Column(String, default="available")  # available or borrowed

    borrow_records = relationship("BorrowRecord", back_populates="book")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', status='{self.status}')>"

    # ORM methods
    @classmethod
    def create(cls, session, title, author):
        book = cls(title=title, author=author)
        session.add(book)
        session.commit()
        return book

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, book_id):
        return session.query(cls).filter_by(id=book_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()

    # Property example: ensure book is available
    @property
    def is_available(self):
        return self.status == "available"

# -----------------------
# User Model
# -----------------------
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    borrow_records = relationship("BorrowRecord", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

    # ORM methods
    @classmethod
    def create(cls, session, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, user_id):
        return session.query(cls).filter_by(id=user_id).first()

    def delete(self, session):
        session.delete(self)
        session.commit()

    # Property example: borrowed book count
    @property
    def borrowed_books_count(self):
        return len(self.borrow_records)


# -----------------------
# Borrow Record Model
# -----------------------
class BorrowRecord(Base):
    __tablename__ = 'borrow_records'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="borrow_records")
    book = relationship("Book", back_populates="borrow_records")

    def __repr__(self):
        return f"<BorrowRecord(user_id={self.user_id}, book_id={self.book_id}, borrow_date={self.borrow_date}, return_date={self.return_date})>"

    # ORM methods
    @classmethod
    def create(cls, session, user, book):
        if not book.is_available:
            raise ValueError("Book is currently borrowed.")
        record = cls(user=user, book=book)
        book.status = "borrowed"
        session.add(record)
        session.commit()
        return record

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, record_id):
        return session.query(cls).filter_by(id=record_id).first()

    def delete(self, session):
        # Return book to available when record is deleted
        self.book.status = "available"
        session.delete(self)
        session.commit()

    # Property example: is returned
    @property
    def is_returned(self):
        return self.return_date is not None


# -----------------------
# DB Setup
# -----------------------
engine = create_engine("sqlite:///app.db")
Base.metadata.create_all(engine)
