# Technical-Interview
# 🚗 Car Sales API - Backend Developer Technical Challenge

Este proyecto fue desarrollado como parte de una prueba técnica para el puesto de Backend Developer Junior. El objetivo fue construir una API RESTful usando **FastAPI** que permita gestionar publicaciones de autos, incluyendo entidades relacionadas como marcas, usuarios y transacciones de venta.

---

## ✅ Funcionalidades principales

- CRUD completo para `CarPost`, `Brand`, `User` y `Transaction`
- Transformación de datos en la capa de servicio (`CarPostOut` usa `full_title`)
- Arquitectura en capas: Routes / Services / Schemas / Models
- Uso de ORM (SQLAlchemy) con SQLite
- Validación con Pydantic + Type Hints en todo el código
- Endpoints `/health` y `/version`
- Documentación automática con Swagger (FastAPI)
- Test automatizado con Pytest

---

## ⚙️ Cómo correr el proyecto

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
uvicorn app.main:app --reload

# Visitar Swagger
http://127.0.0.1:8000/docs

