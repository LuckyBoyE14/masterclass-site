#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Файл главного окна приложения, здесь объединяется вся логика приложения.
"""

from fastapi import FastAPI


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


if __name__ == "__main__":
    pass
