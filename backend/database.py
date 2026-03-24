from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Creacion de la sesion para la db. 
DATABASE_URL = "postgresql://roger:@localhost/ticketsdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()