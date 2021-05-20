#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Здесь будут схемы pydantic, которые относятся к пользователю.
"""

from pydantic import BaseModel, EmailStr
from datetime import datetime


class User(BaseModel):

    """Модель пользователя"""

    pk: int
    nick: str
    email: str
    name: str = None
    surname: str = None
    password: str
    created_by: datetime = datetime.now()
