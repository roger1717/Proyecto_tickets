from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tickets_routes import router

# Puerta de entrada a la API , Lo ejecuta FastAPI directamente 

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,   #politica de seguridad de los navegadores
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router) # Ve a routes.py, toma todos los endpoints que definí ahí 