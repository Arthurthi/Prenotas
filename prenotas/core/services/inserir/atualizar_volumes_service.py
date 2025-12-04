from core.data.estoqueData import atualizar_volumes

def atualizar_estoque(engine, df_editado):
    try:
        for _, row in df_editado.iterrows():
            prenota = row["prenota"]
            volumes = row["volumes"]

            if volumes is None:
                return False, f"Volumes inválido na prenota {prenota}"

            atualizar_volumes(engine, prenota, volumes)

        return True, "Estoque atualizado com sucesso"

    except Exception as e:
        return False, f"Erro ao atualizar estoque: {e}"
