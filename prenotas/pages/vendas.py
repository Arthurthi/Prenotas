import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from core.services.inserir.FuncaoVendas import validar_campos, inserir_campos
from core.services.deletar.Deletarvendas import excluir_venda


# ================= CONEXÃO
db = st.secrets["db"]

conn_str = (
    f"postgresql+psycopg2://{db['user']}:{db['password']}"
    f"@{db['host']}:{db['port']}/{db['database']}"
)

engine = create_engine(conn_str)




st.title("Vendas")




# ================= TABELA
st.title("Vendas")


tabela = "vendas"
df = pd.read_sql(f"SELECT * FROM {tabela}", con=engine)
st.dataframe(df)




# ================= DELETAR
with st.expander("Deletar venda"):
    prenota_del = st.text_input("Prenota para deletar", key="prenota_deletar")

    if st.button("Deletar"):
        try:
            excluir_venda(engine, prenota_del)
            st.success("Registro deletado com sucesso")
            st.rerun()
        except Exception as e:
            st.error(f"Erro ao deletar: {e}")





# ================= INSERIR
with st.expander("Inserir nova venda"):
    prenota = st.text_input("Prenota", key="prenota")

    transportadoras = ["bueno express", "planalto", "dfsul", "sao miguel"]
    transportadora = st.selectbox(
        "Transportadora",
        options=transportadoras,
        key="transportadora_input"
    )

    vendedores = ["joao", "maria", "pedro"]
    vendedor = st.selectbox(
        "Vendedor",
        options=vendedores,
        key="vendedor_input"
    )

    destino = st.text_input("Destino", key="destino")

    if st.button("Salvar"):
        valido, erro = validar_campos(prenota, transportadora, vendedor, destino)

        if not valido:
            st.error(erro)

        else:
            try:
                inserir_campos(engine, prenota, transportadora, vendedor, destino)
                st.success("Registro inserido com sucesso")

                st.rerun()

            except Exception as e:
                st.error(f"Erro ao inserir: {e}")
