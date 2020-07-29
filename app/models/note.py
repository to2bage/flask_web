"""
Project name: flask_web
Description:
Create Time: 2020/7/29 14:06
Author: to2bage
Email: to2bage@hotmail.com
Version: 0.1
"""
from sqlalchemy import Column, Integer, Text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Note(db.Model):
    id = Column(Integer, primary_key=True)
    body = Column(Text)
