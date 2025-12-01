import streamlit as st
import pandas as pd
from sqlalchemy import text



def validar_campos(prenota, transportadora, vendedor):
    if not prenota:
        return False, "O campo 'prenota' é obrigatório."
    if not transportadora:
        return False, "O campo 'transportadora' é obrigatório."
    if not vendedor:
        return False, "O campo 'vendedor' é obrigatório."

    return True, None


def inserir_campos(engine, prenota, transportadora, vendedor):
    query = text("""
        INSERT INTO vendas (prenota, transportadora, vendedor)
        VALUES(:prenota, :transportadora, :vendedor)
    """)

    with engine.begin() as conn:
        conn.execute(
            query,
            {
                "prenota": prenota,
                "transportadora": transportadora,
                "vendedor": vendedor
            }
        )