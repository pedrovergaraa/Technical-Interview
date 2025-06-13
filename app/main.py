from fastapi import FastAPI
from app.routes import car_post_route
from app.database.connection import Base, engine
from app.routes import car_post_route, brand_route, user_route, transaction_route
from app.models import car_post, brand, user, transaction


app = FastAPI(
    title="Car Sales API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(car_post_route.router)
app.include_router(brand_route.router)
app.include_router(user_route.router)
app.include_router(transaction_route.router)

@app.get("/healthcheck")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}