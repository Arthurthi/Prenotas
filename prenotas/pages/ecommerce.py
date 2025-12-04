import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from core.services.inserir.funcaoEcommerce import validar_ecommerce, inserir_ecommerce
from core.services.deletar.deletarEcommerce import excluir_ecommerce


db = st.secrets["db"]

conn_str = (
    f"postgresql+psycopg2://{db['user']}:{db['password']}"
    f"@{db['host']}:{db['port']}/{db['database']}"
)


engine = create_engine(conn_str)
st.title("Ecommerce")

# ================= TABELA
tabela = "ecommerceview"
df = pd.read_sql(f"SELECT * FROM {tabela}", con=engine)
st.dataframe(df)

# ================= DELETAR
with st.expander("Deletar ecommerce"):
    ecommerce_del = st.text_input("Prenota para deletar", key="ecommerce_del")

    if st.button("Deletar"):
        try:
            excluir_ecommerce(engine, ecommerce_del)
            st.success("Ecommerce deletado com sucesso")
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao deletar: {e}")




# ================= INSERIR
with st.expander("Inserir novo ecommerce"):

    prenota = st.text_input("Prenota", key="prenota")
    cliente = st.text_input("Cliente", key="cliente")
    coleta = st.text_input("Coleta", key="coleta")

    if st.button("Salvar"):
        valido, erro = validar_ecommerce(prenota, cliente, coleta)
        if not valido:
            st.error(erro)
        else:
            try:
                inserir_ecommerce(engine, prenota, cliente, coleta)
                st.success("Ecommerce inserido com sucesso")
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao inserir: {e}")
