import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text


engine = create_engine("sqlite:///prenotas.db")


#===========TABELA VISIVEL=======#
tabela = "vendas"


df = pd.read_sql(f"SELECT * FROM {tabela}", engine)


st.title("Tabela Vendas")  
st.dataframe(df)


#===========APARECER TABELA=========#
def carregar_tabela():
    return pd.read_sql("SELECT * FROM vendas ORDER BY id ASC", engine)




#============ NOVA PRENOTA=============#
nova_prenota = st.text_input("Inserir:")

if nova_prenota:
    with engine.begin() as conn: 
        conn.execute(
            text("""
                INSERT OR IGNORE INTO vendas (prenota)
                VALUES (:a)
            """),
            {"a": nova_prenota}
        )

    st.session_state.df = carregar_tabela()

    st.rerun()


#============== BOTAO APAGAR============#

apagar_prenota = st.text_input("Apagar")

if apagar_prenota:
    with engine.begin() as conn:
        conn.execute(
            text("""DELETE FROM estoque
                WHERE prenota = :a
                """),
                {"a": apagar_prenota}
        )
    st.success(f"Prenota {apagar_prenota} apagada!")
    st.rerun()
else:
    st.error("Digite uma prenota para apagar.") 