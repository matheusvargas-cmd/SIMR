# ==========================================================
# Monitor SIMR
# ==========================================================

from config import LINKS
from config import SETORES
from config import IMPRESSORAS
from config import ACCESS_POINTS


# ==========================================================
# Classificação
# ==========================================================

def classificar_ping(ping):

    if ping < 0:
        return "🔴"

    if ping <= 10:
        return "🟢"

    if ping <= 40:
        return "🟡"

    return "🔴"


# ==========================================================
# Converte resultado em Status
# ==========================================================

def montar_status(online):

    if online:
        return 5, "ONLINE"

    return -1, "OFFLINE"


# ==========================================================
# Monitor Genérico
# ==========================================================

def verificar_dispositivo(mk, dispositivo):

    metodo = dispositivo.get("monitor", "ping")
    ip = dispositivo["ip"]

    print(f"\n==============================")
    print(f"IP: {ip}")
    print(f"Método: {metodo}")

    try:

        if metodo == "netwatch":

            resultado = mk.host_online(ip)

        elif metodo == "http":

            resultado = mk.http_online(ip)

        elif metodo == "fetch":

            resultado = mk.fetch_routeros(f"http://{ip}")

        elif metodo == "router_ping":

            resultado = mk.ping_routeros(ip)

        else:

            resultado = mk.ping(ip)

        print(f"Resultado: {resultado}")

        return resultado

    except Exception as e:

        print(f"ERRO: {e}")

        return False

# ==========================================================
# Links
# ==========================================================

def obter_links(mk):

    links = []

    for link in LINKS:

        online = mk.pppoe_status(link["interface"])

        links.append({

            "nome": link["nome"],

            "interface": link["interface"],

            "ip": link["ip"],

            "status": "ONLINE" if online else "OFFLINE",

            "velocidade": "🟢" if online else "🔴"

        })

    return links


# ==========================================================
# Rede Cabeada
# ==========================================================

def obter_setores(mk):

    setores = []

    for setor in SETORES:

        online = verificar_dispositivo(

            mk,

            {

                "ip": setor["gateway"],

                "monitor": setor.get("monitor", "ping")

            }

        )

        ping, status = montar_status(online)

        setores.append({

            "nome": setor["nome"],

            "gateway": setor["gateway"],

            "status": status,

            "velocidade": classificar_ping(ping)

        })

    return setores


# ==========================================================
# Access Points
# ==========================================================

def obter_wifi(mk):

    wifi = []

    for ap in ACCESS_POINTS:

        if ap["ip"] == "":

            wifi.append({

                "nome": ap["nome"],

                "ip": "-",

                "status": "NÃO CADASTRADO",

                "velocidade": "⚪"

            })

            continue

        online = verificar_dispositivo(mk, ap)

        ping, status = montar_status(online)

        wifi.append({

            "nome": ap["nome"],

            "ip": ap["ip"],

            "status": status,

            "velocidade": classificar_ping(ping)

        })

    return wifi


# ==========================================================
# Impressoras
# ==========================================================

def obter_impressoras(mk):

    impressoras = []

    for impressora in IMPRESSORAS:

        online = verificar_dispositivo(mk, impressora)

        ping, status = montar_status(online)

        impressoras.append({

            "nome": impressora["nome"],

            "setor": impressora["setor"],

            "ip": impressora["ip"],

            "status": status,

            "velocidade": classificar_ping(ping)

        })

    return impressoras


# ==========================================================
# Resumo
# ==========================================================

def obter_resumo(links, impressoras):

    return {

        "links_online": sum(

            1

            for item in links

            if item["status"] == "ONLINE"

        ),

        "links_total": len(links),

        "equipamentos_online": sum(

            1

            for item in impressoras

            if item["status"] == "ONLINE"

        ),

        "equipamentos_total": len(impressoras)

    }


# ==========================================================
# Estatísticas
# ==========================================================

def obter_estatisticas(links, setores, wifi, impressoras):

    listas = [

        links,

        setores,

        wifi,

        impressoras

    ]

    total = sum(len(lista) for lista in listas)

    online = sum(

        1

        for lista in listas

        for item in lista

        if item["status"] == "ONLINE"

    )

    return {

        "online": online,

        "offline": total - online,

        "total": total

    }