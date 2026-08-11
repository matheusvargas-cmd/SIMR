# ==========================================================
# Dashboard SIMR
# ==========================================================

from datetime import datetime

from core.conexao import ConexaoMikroTik

from core.monitor import (

    obter_links,

    obter_setores,

    obter_wifi,

    obter_impressoras,

    obter_resumo,

    obter_estatisticas

)


# ==========================================================
# Dashboard
# ==========================================================

def carregar_dashboard():

    try:

        # --------------------------------------------------
        # Conecta ao MikroTik
        # --------------------------------------------------

        mk = ConexaoMikroTik.obter()

        if not mk.conectado():

            mk = ConexaoMikroTik.reconectar()

        # --------------------------------------------------
        # Informações do MikroTik
        # --------------------------------------------------

        resource = mk.resource()

        memoria_total = int(resource["total-memory"])
        memoria_livre = int(resource["free-memory"])

        memoria = round(

            ((memoria_total - memoria_livre) /
             memoria_total) * 100

        )

        mikrotik = {

            "status": "ONLINE",

            "modelo": resource.get("board-name", "-"),

            "routeros": resource.get("version", "-"),

            "cpu": int(resource.get("cpu-load", 0)),

            "memoria": memoria,

            "uptime": resource.get("uptime", "-")

        }

        # --------------------------------------------------
        # Coleta de Dados
        # --------------------------------------------------

        print("[DASHBOARD] INICIANDO LINKS")
        links = obter_links(mk)
        print("[DASHBOARD] LINKS OK")

        print("[DASHBOARD] INICIANDO SETORES")
        setores = obter_setores(mk)
        print("[DASHBOARD] SETORES OK")

        print("[DASHBOARD] INICIANDO WIFI")
        wifi = obter_wifi(mk)
        print("[DASHBOARD] WIFI OK")

        print("[DASHBOARD] INICIANDO IMPRESSORAS")
        impressoras = obter_impressoras(mk)
        print("[DASHBOARD] IMPRESSORAS OK")

        # --------------------------------------------------
        # Resumos
        # --------------------------------------------------

        resumo = obter_resumo(

            links,

            impressoras

        )

        estatisticas = obter_estatisticas(

            links,

            setores,

            wifi,

            impressoras

        )

        # --------------------------------------------------
        # Retorno
        # --------------------------------------------------

        return {

            "sucesso": True,

            "mikrotik": mikrotik,

            "links": links,

            "setores": setores,

            "wifi": wifi,

            "impressoras": impressoras,

            "resumo": resumo,

            "estatisticas": estatisticas,

            "ultima_atualizacao": datetime.now().strftime(

                "%d/%m/%Y %H:%M:%S"

            )

        }

    except Exception as erro:

        import traceback

        print("\n================ ERRO NO DASHBOARD ================\n")

        traceback.print_exc()

        print("\n===================================================\n")

        return {

            "sucesso": False,

            "erro": str(erro)

    }