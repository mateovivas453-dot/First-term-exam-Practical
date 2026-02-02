from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI()


class Usuario(SQLModel):
    id: int | None = None  
    nombre: str            
    password: str
    correo: str | None = None  
    esta_activo: bool = True   

class SolicitudLogin(SQLModel):
    nombre: str
    password: str



usuarios = [
    Usuario(id=1, nombre="Juan", password="Mta", correo="juan@correo.com", esta_activo=True)
]


@app.get("/")
def inicio():
    return {"message": "API de Usuarios activa"}

@app.get("/users")
def obtener_usuarios():
    return usuarios

@app.get("/users/{usuario_id}")
def obtener_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    return {"message": "Usuario no encontrado"}

@app.post("/users")
def crear_usuario(usuario: Usuario):
    for u in usuarios:
        if u.nombre == usuario.nombre:
            return {"message": "Error: El nombre de usuario ya existe"}

    nuevo_id = len(usuarios) + 1
    usuario.id = nuevo_id
    usuarios.append(usuario)
    
    return {
        "message": "Usuario creado exitosamente",
        "usuario": usuario
    }

@app.put("/users/{usuario_id}")
def actualizar_usuario(usuario_id: int, datos_usuario: Usuario):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            
            usuario.nombre = datos_usuario.nombre
            usuario.correo = datos_usuario.correo
            usuario.esta_activo = datos_usuario.esta_activo
            return {"message": "Usuario actualizado", "usuario": usuario}
    return {"message": "Usuario no encontrado"}

@app.delete("/users/{usuario_id}")
def borrar_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuarios.remove(usuario)
            return {"message": "Usuario eliminado", "usuario": usuario}
    return {"message": f"Usuario con id {usuario_id} no existe"}

@app.post("/login")
def login(credenciales: SolicitudLogin):
    for usuario in usuarios:
        if usuario.nombre == credenciales.nombre and usuario.password == credenciales.password:
            return {"message": "login exitoso"}
    return {"message": "login fallido"}