import streamlit as st
import pandas as pd
from sqlalchemy import text

def validar_ecommerce(prenota, cliente, coleta):
    if not prenota:
        return False, "O campo 'prenota' é obrigatório."
    if not cliente:
        return False, "O campo 'cliente' é obrigatório."
    if not coleta:
        return False, "O campo 'coleta' é obrigatório."

    return True, None





def inserir_ecommerce(engine, prenota, cliente, coleta):
    query = text("""
        INSERT INTO ecommerceview (prenota, cliente, coleta)
        VALUES(:prenota, :cliente, :coleta)
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "prenota": prenota,
                "cliente": cliente,
                "coleta": coleta
            }
        )