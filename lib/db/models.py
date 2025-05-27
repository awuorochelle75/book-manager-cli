from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

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

    # Relationship to BorrowRecord
    borrow_records = relationship("BorrowRecord", back_populates="book")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', status='{self.status}')>"


# -----------------------
# User Model
# -----------------------
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Relationship to BorrowRecord
    borrow_records = relationship("BorrowRecord", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"


# -----------------------
# Borrow Record Model
# -----------------------
class BorrowRecord(Base):
    __tablename__ = 'borrow_records'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    borrow_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime, nullable=True)  # when returned

    user = relationship("User", back_populates="borrow_records")
    book = relationship("Book", back_populates="borrow_records")

    def __repr__(self):
        return f"<BorrowRecord(user_id={self.user_id}, book_id={self.book_id}, borrow_date={self.borrow_date}, return_date={self.return_date})>"
