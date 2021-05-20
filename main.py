#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Файл главного окна приложения, здесь объединяется вся логика приложения.
"""

from fastapi import FastAPI
from core.schemas.user import User


app = FastAPI()


@app.get('/')
async def main():
    """
    Главная страница приложения
    :returns: TODO

    """
    return {
        "name" :"Hello world",
    }


@app.get('/{pk}')
def get_lesson(pk: int, name: int = None):
    """
    Функция возвращает json одного мастер-класса

    :pk: первичный ключ
    :returns: json

    """
    return {
        "pk": pk,
    }


@app.post('/create_user')
def create_user(user: User):
    """
    Функция позволяет создавать пользователя

    :user: схема core/schemas/user.py User
    :returns: TODO

    """
    return user


@app.get('/user')
def get_user(name: str):
    """
    Функция возвращает объект пользователя

    :name: TODO
    :returns: TODO

    """
    return User


if __name__ == "__main__":
    pass
