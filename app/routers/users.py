from fastapi import APIRouter,HTTPException
from app.services.user import createUser,getUserByGmail,getUserById,deleteUserbyId
from app.security.encrypt_passwords import verify_password



app = APIRouter(tags=['Users'])

@app.post("/usuarios/registrar")
async def register_User(username:str,password:str,gmail:str):
    try:
        createUser(username,password,gmail)
        return {"status": "ok", "message": "Usuario creado correctamente"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@app.get("/usuario/get")
async def get_info_user_by_id(id:int):
    try:
        
        resultado = getUserById(id)
        
        return resultado
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@app.post("/usuarios/login")
async def loginUser(gmail:str,password:str):

    user = getUserByGmail(gmail)

    if user is None:
        raise HTTPException(status_code=404, detail="El correo no está registrado")


    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")


    return {
        "status": "ok",
        "message": "Login correcto",
        "user": {
            "id": user["id"],
            "username": user["username"],
            "gmail": user["gmail"]
        }
    }

@app.delete("/usuarios/delete")
async def deleteUser(gmail:str,password:str):



    if not gmail or not password:
        raise HTTPException(status_code=400, detail="gmail y password son obligatorios")

    # 1. Buscar usuario
    user = getUserByGmail(gmail)
    print(user)
    if user is None:
        raise HTTPException(status_code=404, detail="El correo no está registrado")
    
    # 2. Verificar contraseña
    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    # 3. Eliminar usuario
    deleted = deleteUserbyId(gmail)

    if deleted == 0:
        raise HTTPException(status_code=500, detail="No se pudo eliminar el usuario")

    return {
        "status": "ok",
        "message": f"Usuario '{gmail}' eliminado correctamente"
    }