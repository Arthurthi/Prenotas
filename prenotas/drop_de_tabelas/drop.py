from sqlalchemy import create_engine, text

database_url = 'sqlite:///prenotas.db'


# =========== SERVE PRA EXCLUIR A TABEL ==============

engine = create_engine(database_url)

with engine.connect() as conn:
    #========PARA EXCLUIR OUTRA TABELA TROQUE ↓↓↓↓ AQUII
    conn.execute(text("DROP TABLE IF EXISTS vendas")) 
    #=======================================  ↑↑↑↑↑
    conn.commit()

print("Tabela removida com sucesso, se existia.")



