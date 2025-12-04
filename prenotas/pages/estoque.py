import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from core.services.inserir.atualizar_volumes_service import atualizar_estoque

# ================= CONEXÃO
db = st.secrets["db"]

conn_str = (
    f"postgresql+psycopg2://{db['user']}:{db['password']}"
    f"@{db['host']}:{db['port']}/{db['database']}"
)
engine = create_engine(conn_str)

st.title("Estoque")
st.divider()

# ================= BUSCA DE DADOS
df = pd.read_sql("""
    SELECT prenota, vendedor, transportadora, volumes, destino 
    FROM principal
    ORDER BY prenota
""", engine)

busca = st.text_input("Pesquisar prenota")

if busca:
    df = df[df["prenota"].astype(str).str.contains(busca, case=False, na=False)]

st.subheader("Editar volumes diretamente na tabela:")

df_editado = st.data_editor(
    df,
    disabled=["prenota", "vendedor", "transportadora", "destino"],
    key="editor_estoque"
)

if st.button("Salvar alterações"):
    ok, msg = atualizar_estoque(engine, df_editado)

    if ok:
        st.success(msg)
        st.rerun()
    else:
        st.error(msg)
