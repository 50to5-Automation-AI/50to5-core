import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()


db_url = os.getenv("AP_SERVER_DB_URL").split("///")[1]

# Ensure the directory exists
os.makedirs(os.path.dirname(db_url), exist_ok=True)

# Database setup
DATABASE_URL = os.getenv("AP_SERVER_DB_URL")
Base = declarative_base()

# Define a sample table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    email = Column(String(50))

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Create all tables
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data
new_user = User(username='john_doe', email='john@example.com')
session.add(new_user)
session.commit()

# Query the database
for user in session.query(User).all():
    print(user.username, user.email)

# Close the session
session.close()