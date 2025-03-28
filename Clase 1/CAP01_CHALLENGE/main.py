from fastapi import FastAPI, HTTPException, Depends, Query
from typing import List, Optional
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt

# Definición de la "base de datos" ficticia en memoria
fake_db = {"users": {}}

# Configuración para la encriptación y JWT
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "secret_key"  # Se debe cambiar en producción
ALGORITHM = "HS256"

app = FastAPI()

# Modelos de datos
class Payload(BaseModel):
    numbers: List[int]

class BinarySearchPayload(BaseModel):
    numbers: List[int]
    target: int

class UserCredentials(BaseModel):
    username: str
    password: str

# Funciones auxiliares

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, secret_key: str = SECRET_KEY, algorithm: str = ALGORITHM) -> str:
    return jwt.encode(data, secret_key, algorithm=algorithm)


def decode_access_token(token: str, secret_key: str = SECRET_KEY, algorithm: str = ALGORITHM) -> str:
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        return payload.get("sub")  # Retorna el username
    except jwt.PyJWTError:
        return None

# Dependencia para verificar token en cada solicitud protegida

def get_current_user(token: Optional[str] = Query(None)) -> str:
    if not token:
        raise HTTPException(status_code=401, detail="Token missing")

    username = decode_access_token(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    return username

# Endpoints de autenticación
@app.post("/register")
def register(credentials: UserCredentials):
    username = credentials.username
    password = credentials.password

    if username in fake_db["users"]:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    hashed_password = get_password_hash(password)
    fake_db["users"][username] = hashed_password

    return {"message": "User registered successfully"}

@app.post("/login")
def login(credentials: UserCredentials):
    username = credentials.username
    password = credentials.password

    if username not in fake_db["users"]:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    stored_hashed_password = fake_db["users"][username]
    if not verify_password(password, stored_hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    # Crear token JWT
    access_token = create_access_token({"sub": username})
    return {"access_token": access_token}

# Algoritmo de Bubble Sort

def bubble_sort(numbers: List[int]) -> List[int]:
    arr = numbers[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Algoritmo de Búsqueda Binaria

def binary_search(sorted_list: List[int], target: int) -> (bool, int):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return True, mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, -1

# Endpoints protegidos
@app.post("/bubble-sort")
def bubble_sort_endpoint(payload: Payload, current_user: str = Depends(get_current_user)):
    """
    /doc
    Recibe una lista de números y devuelve la lista ordenada utilizando Bubble Sort.
    """
    sorted_numbers = bubble_sort(payload.numbers)
    return {"numbers": sorted_numbers}

@app.post("/filter-even")
def filter_even(payload: Payload, current_user: str = Depends(get_current_user)):
    """
    /doc
    Recibe una lista de números y devuelve únicamente aquellos que son pares.
    """
    even_numbers = [num for num in payload.numbers if num % 2 == 0]
    return {"even_numbers": even_numbers}

@app.post("/sum-elements")
def sum_elements(payload: Payload, current_user: str = Depends(get_current_user)):
    """
    /doc
    Recibe una lista de números y devuelve la suma de sus elementos.
    """
    total = sum(payload.numbers)
    return {"sum": total}

@app.post("/max-value")
def max_value(payload: Payload, current_user: str = Depends(get_current_user)):
    """
    /doc
    Recibe una lista de números y devuelve el valor máximo.
    """
    if not payload.numbers:
        raise HTTPException(status_code=400, detail="La lista está vacía")
    maximum = max(payload.numbers)
    return {"max": maximum}

@app.post("/binary-search")
def binary_search_endpoint(payload: BinarySearchPayload, current_user: str = Depends(get_current_user)):
    """
    /doc
    Recibe un número y una lista de números ordenados. Devuelve true y el índice si el número está en la lista, de lo contrario false y -1.
    """
    found, index = binary_search(payload.numbers, payload.target)
    return {"found": found, "index": index}
