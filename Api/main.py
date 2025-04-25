from fastapi import FastAPI 
from Api.Controller.router import router as centros_router

app = FastAPI()

print("Registrando router...")
app.include_router(centros_router, prefix="/api", tags=["Centros"])
print("Router registrado.")


if __name__ == "__main__":
    import uvicorn
    print("Iniciando servidor...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
    print("Servidor iniciado.")