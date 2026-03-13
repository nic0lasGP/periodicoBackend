import re
from pydantic import EmailStr
import dns.resolver

def validatePassword(password: str) -> bool:
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return bool(re.match(pattern, password))


#Hacer funcionar!!
def emailIsValid(email: str) -> bool:
    # 1. Validar formato del email
    try:
        EmailStr(email)
    except:
        return False  # Formato inválido

    # 2. Validar que el dominio existe y tiene MX
    domain = email.split("@")[1]

    try:
        dns.resolver.resolve(domain, "MX")
        return True  # Dominio válido y puede recibir correos
    except:
        return False  # Dominio inexistente o sin MX

