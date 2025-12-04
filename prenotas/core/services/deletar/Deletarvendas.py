import streamlit as st
import pandas as pd
import psycopg2 
from sqlalchemy import text

def excluir_venda(engine, prenota):
    query = text("""
        DELETE FROM vendas
        WHERE prenota = :prenota
    """)

    with engine.begin() as conn:
        conn.execute(query, {"prenota": prenota})
