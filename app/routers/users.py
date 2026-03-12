from fastapi import APIRouter,HTTPException,Depends
from app.services import createUser,getUserByGmail,getUserById,deleteUserbyId,changePassword
from app.security.encrypt_passwords import verifyPassword,hashPassword
from app.security.validates import validatePassword
from fastapi.security import OAuth2PasswordRequestForm
from app.security import createAccessToken,getCurrentUser



app = APIRouter(tags=['Users'])



@app.get("/users/me")
def get_me(current_user: dict = Depends(getCurrentUser)):
    return current_user

@app.post("/users/register")
async def register_User(username:str,password:str,gmail:str):
    try:
        createUser(username,password,gmail)
        return {"status": "ok", "message": "Usuario creado correctamente"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))


@app.get("/users/get-by-id")
async def get_info_user_by_id(id:int):
    try:
        
        resultado = getUserById(id)
        
        return resultado
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
    

@app.get("/users/get-by-gmail")
async def get_info_user_by_gmail(gmail:int):
    try:
        
        resultado = getUserByGmail(gmail)
        
        return resultado
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))



@app.post("/users/login")
async def loginUser(gmail:str,password:str):

  
    
    user = getUserByGmail(gmail)

    if user is None:
        raise HTTPException(status_code=404, detail="El correo no está registrado")


    if not verifyPassword(password , user["password"]):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")


    token_data = {
        "id": user["id"],
        "gmail": user["gmail"],
        "username": user["username"],
        "admin": user["admin"]
    }

    access_token = createAccessToken(token_data)
    return {
        "status": "ok",
        "message": "Login correcto",
        "token":access_token,   
        "user": {
            "id": user["id"],
            "username": user["username"],
            "gmail": user["gmail"]
        }
    }

@app.delete("/users/delete")
async def deleteUser(gmail:str,password:str):



    if not gmail or not password:
        raise HTTPException(status_code=400, detail="gmail y password son obligatorios")

    # 1. Buscar usuario
    user = getUserByGmail(gmail)
    print(user)
    if user is None:
        raise HTTPException(status_code=404, detail="El correo no está registrado")
    
    # 2. Verificar contraseña
    if not verifyPassword(password, user["password"]):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    # 3. Eliminar usuario 
    deleted = deleteUserbyId(user["id"])

    if deleted == 0:
        raise HTTPException(status_code=500, detail="No se pudo eliminar el usuario")

    return {
        "status": "ok",
        "message": f"Usuario '{gmail}' eliminado correctamente"
    }


#expandir en un futuro 
@app.patch("/admin/change-password")
async def change_password(gmail:str,old_password:str,new_password:str):

    if not gmail or not old_password or not new_password:
        raise HTTPException(status_code=400, detail="Faltan campos obligatorios")

    # 1. Obtener usuario por gmail
    user = getUserByGmail(gmail)

    if not user:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    # 2. Verificar contraseña actual
    if not verifyPassword(old_password, user["password"]):
        raise HTTPException(status_code=401, detail="La contraseña actual es incorrecta")

    if not validatePassword(new_password):
        raise HTTPException(status_code=401, detail="La nueva contraseña esta en un formato incorrecto")
    
    hashed_password = hashPassword(new_password)
    if verifyPassword(old_password,hashed_password):
        raise HTTPException(status_code=401, detail="Las contraseña es la misma")
    # 3. Cambiar contraseña usando tu función
    updated = changePassword(user["id"], hashed_password)

    if not updated:
        raise HTTPException(status_code=500, detail="No se pudo actualizar la contraseña")

    return {
        "status": "ok",
        "message": "Contraseña actualizada correctamente"
    }