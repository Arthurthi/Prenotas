from sqlalchemy import text

def atualizar_volumes(engine, prenota, volumes):
    sql = text("""
        UPDATE principal
        SET volumes = :volumes
        WHERE prenota = :prenota
    """)

    with engine.begin() as conn:
        conn.execute(sql, {
            "prenota": prenota,
            "volumes": volumes
        })
