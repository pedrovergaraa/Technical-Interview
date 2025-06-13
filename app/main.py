from fastapi import FastAPI
from app.routes import car_post_route
from app.database.connection import Base, engine

app = FastAPI(
    title="Car Sales API",
    version="1.0.0",
    debug=True
)

# Crear tablas
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(car_post_route.router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}
