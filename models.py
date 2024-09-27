from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config import engine, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()