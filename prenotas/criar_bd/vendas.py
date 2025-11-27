import streamlit as st
import pandas as pd


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///prenotas.db')

base = declarative_base()

Session = sessionmaker(bind=engine)

class Vendas(base):
    __tablename__ = 'vendas'

    id = Column(Integer, primary_key=True, autoincrement=True) 

    prenota = Column(Integer, nullable=False, unique=True)
    volumes = Column(Integer, nullable=True)
    data_prenota = Column(String, nullable=True)
    status = Column(String, nullable=True)
    notas = Column(Integer, nullable=True)
    boleto = Column(String, nullable=True )
    observacao = Column(String, nullable=True)







base.metadata.create_all(bind=engine)