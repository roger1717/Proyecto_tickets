from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Creacion de la sesion para la db. 
DATABASE_URL = "sqlite:///./tickets.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}) # Argumentos

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()