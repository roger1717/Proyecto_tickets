from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ticket_routes import router
from database import engine, Base
import models
# Puerta de entrada a la API , Lo ejecuta FastAPI directamente 

app = FastAPI()

# Crear las tablas automaticamente al arrancar
Base.metadata.create_all(bind=engine)

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,   #politica de seguridad de los navegadores
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router) # Ve a routes.py, toma todos los endpoints que definí ahí 