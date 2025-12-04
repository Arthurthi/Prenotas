import streamlit as st
import pandas as pd
from sqlalchemy import text

def excluir_ecommerce(engine, prenota):
    query = text("""
        DELETE FROM ecommerceview
        WHERE prenota = :prenota
    """)

    with engine.begin() as conn:
        conn.execute(query, {"prenota": prenota})

