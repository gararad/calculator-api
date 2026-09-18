from fastapi import FastAPI, HTTPException #FastAPI - класс приложения и способ HTTPException - вернуть ошибку с кодом (например, 400).
from pydantic import BaseModel #BaseModel - базовый класс для описания структуры входных данных

app = FastAPI(title="Calculator API", version="1.0")#Создаём объект приложения. Он будет обрабатывать запросы.


class Operands(BaseModel): #Создаем класс, в котором описываем, что ждём 2 числа для арифметики
    a: float
    b: float


@app.get("/health") #Декоратор сообщает, что когда придёт GET-запрос на путь /health, вызываем функцию ниже
async def health(): #
    return {"status": "ok"}


@app.post("/add")#
async def add(data: Operands):#
    return {"result": data.a + data.b}#


@app.post("/subtract")#
async def subtract(data: Operands):#
    return {"result": data.a - data.b}#


@app.post("/multiply")#
async def multiply(data: Operands):#
    return {"result": data.a * data.b}#


@app.post("/divide")#
async def divide(data: Operands):#
    if data.b == 0:#
        raise HTTPException(status_code=400, detail="Division by zero")#
    return {"result": data.a / data.b}#
