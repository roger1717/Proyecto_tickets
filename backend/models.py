from sqlalchemy import Column, Integer, String, DateTime
from database import Base,engine
import datetime

# Estructura Sqlalchemy para las tablas. 

class Ticket(Base):
    __tablename__ = "tickets" 

    # definimos nuestros atributos o columnas 
    id = Column(Integer(),primary_key=True, index=True)
    titulo = Column(String(100),nullable=False)
    descripcion = Column(String(100),nullable=False)
    prioridad = Column(String(20),nullable=True)
    categoria = Column(String(50),nullable=True)
    estado = Column(String(50),nullable=False,default="abierto")
    fecha_creacion = Column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone.utc))
    

    def __str__(self):
        return f"Ticket #{self.id} - {self.titulo}"
    
if __name__ == '__main__':
    Base.metadata.drop_all(engine)   # borra la tabla vieja
    Base.metadata.create_all(engine) # crea la tabla nueva
    print("Tabla recreada exitosamente ✓")