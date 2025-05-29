from lib.db.models import Base  # your declarative Base with models
from sqlalchemy import create_engine

# Creates the engine with the same path you use in Alembic and your app
engine = create_engine('sqlite:///lib/db/app.db')

# Creates all tables in the database (if they don't already exist)
Base.metadata.create_all(engine)

print("Database file and tables created successfully!")
