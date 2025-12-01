
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
import streamlit as st
from core.services.inserir.FuncaoVendas import validar_campos, inserir_campos


#==========Banco de dados
db = st.secrets["db"]
dbname = db["database"]


conn_str = (
    f"postgresql+psycopg2://{db['user']}:{db['password']}"
    f"@{db['host']}:{db['port']}/{db['database']}"
)

engine = create_engine(conn_str)





#=======tabela visivel

tabela = "vendas"

df = pd.read_sql(f"SELECT * FROM {tabela}", con=engine)


st.title("Vendas")



df = pd.read_sql(f"SELECT * FROM {tabela}", con=engine)
st.dataframe(df)



#======Tabela visivel



with st.expander("Inserir nova venda"):
    prenota = st.text_input("prenota")
    transportadora = st.text_input("transportadora")
    vendedor = st.text_input ("vendedor")



    #=============Inserir dados
    if st.button("Salvar"):
        valido, erro = validar_campos(prenota, transportadora, vendedor)

        if not valido:
            st.error(erro)

        else:
            try:
                inserir_campos(engine, prenota, transportadora, vendedor)
                st.success("Registro inserido com sucesso")
            except Exception as e:
                st.error(f"erro ao inserir: {e}")
    st.rerun()
