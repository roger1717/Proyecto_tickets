from fastapi import APIRouter, Depends , HTTPException  
from sqlalchemy.orm import Session
from database import get_db
from models import Ticket
from schemas import TicketCreate,TicketUpdate,TicketResponse
from typing import List

# Endpoints de fastAPI

#GET → Obtener datos (leer)
#POST → Crear datos nuevos
#PUT → Actualizar un recurso completo
#PATCH → Actualizar parcialmente
#DELETE → Eliminar

router = APIRouter()

@router.get("/tickets",response_model=List[TicketResponse]) # OBTENER DATOS.
def get_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()

@router.post("/tickets",response_model=TicketResponse) # CREAR
def post_tickets(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = Ticket(**ticket.model_dump(),estado="abierto")

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@router.patch("/tickets/{id}",response_model=List[TicketUpdate]) # ACTUALIZAR
def patch_tickets(id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == id).first()

    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket no Encontrado")
    
    db_ticket.categoria = ticket.categoria
    db.commit()
    db.refresh(db_ticket)
    return db_ticket