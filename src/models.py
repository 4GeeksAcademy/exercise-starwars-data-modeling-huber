import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    
    favorites = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terraine = Column(String(250), nullable=False)

    favorite_planets = relationship("Favorite_planet", back_populates="planet")

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)

    favorite_characters = relationship("Favorite_character", back_populates="character")

class Species(Base):
    __tablename__ = "species"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    language = Column(String(250), nullable=False)
    skin_colors = Column(String(250), nullable=False)
    
    favorites_species = relationship("Favorite_species", back_populates="species")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    species_id = Column(Integer, ForeignKey("species.id"), nullable=True)
   

    user = relationship(User, back_populates='favorites')
    planet = relationship(Planet, back_populates='favorites')
    character = relationship(Character, back_populates='favorites')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')