# ==========================================================
# CONFIGURAÇÕES DO SIMR
# ==========================================================

import os
from dotenv import load_dotenv

load_dotenv()

# ----------------------------------------------------------
# MikroTik
# ----------------------------------------------------------

MIKROTIK = {
    "host": os.getenv("MIKROTIK_HOST"),
    "porta": int(os.getenv("MIKROTIK_PORT", "8728")),
    "usuario": os.getenv("MIKROTIK_USER"),
    "senha": os.getenv("MIKROTIK_PASSWORD")
}

# ----------------------------------------------------------
# Links de Internet
# ----------------------------------------------------------

LINKS = [

    {

        "nome": "BrasilNET",

        "interface": "pppoe-Brasilnet-ether3",

        "ip": "100.65.3.205",

        "tipo": "Internet"

    },

    {

        "nome": "Imicro",

        "interface": "pppoe-Imicro-ether1",

        "ip": "138.117.103.3",

        "tipo": "Internet"

    }

]


# ----------------------------------------------------------
# Redes / Gateways
# ----------------------------------------------------------

SETORES = [

    {

        "nome": "Administração",

        "gateway": "192.168.0.1",

        "monitor": "ping"

    },

    {

        "nome": "Assessores",

        "gateway": "192.168.1.1",

        "monitor": "ping"

    },

    {

        "nome": "Wi-Fi Administração",

        "gateway": "192.168.3.1",

        "monitor": "ping"

    },

    {

        "nome": "Wi-Fi Assessores",

        "gateway": "192.168.2.1",

        "monitor": "ping"

    },

    {

        "nome": "Transmissão",

        "gateway": "192.168.4.1",

        "monitor": "ping"

    },

    {

        "nome": "Segplan",

        "gateway": "192.168.5.1",

        "monitor": "ping"

    }

]


# ----------------------------------------------------------
# Access Points
# ----------------------------------------------------------

ACCESS_POINTS = [

    {

        "nome": "TI",

        "ip": "192.168.0.101",

        "fabricante": "Intelbras",

        "modelo": "AP 360",

        "tipo": "Access Point",

        "monitor": "fetch"

    },

    {

        "nome": "Administrativo",

        "ip": "192.168.3.200",

        "fabricante": "Intelbras",

        "modelo": "AP 360",

        "tipo": "Access Point",

        "monitor": "http"

    },

    {

        "nome": "Plenário",

        "ip": "192.168.2.197",

        "fabricante": "Intelbras",

        "modelo": "AP",

        "tipo": "Access Point",

        "monitor": "netwatch"

    },

    {

        "nome": "Mesa",

        "ip": "192.168.1.126",

        "fabricante": "Intelbras",

        "modelo": "W5-300",

        "tipo": "Roteador",

        "monitor": "netwatch"

    },

    {

        "nome": "Gabinetes 1",

        "ip": "192.168.2.2",

        "fabricante": "Intelbras",

        "modelo": "AP",

        "tipo": "Acsses Point",

        "monitor": "netwatch"

    },

    {

        "nome": "Gabinetes 2",

        "ip": "192.168.2.3",

        "fabricante": "Intelbras",

        "modelo": "AP",

        "tipo": "Acsses Point",

        "monitor": "netwatch"

    },

    {

        "nome": "Sistema de Votação",

        "ip": "10.0.0.1",

        "fabricante": "Intelbras",

        "modelo": "W5-300",

        "tipo": "Roteador",

        "monitor": "http"

    }

]


# ----------------------------------------------------------
# Impressoras
# ----------------------------------------------------------

IMPRESSORAS = [

    {

        "nome": "Epson L6490 - 1º Andar",

        "setor": "1º Andar",

        "ip": "192.168.2.138",

        "fabricante": "Epson",

        "modelo": "L6490",

        "tipo": "Impressora",

        "monitor": "netwatch"

    },

    {

        "nome": "Epson L6490 - 2º Andar",

        "setor": "2º Andar",

        "ip": "192.168.2.143",

        "fabricante": "Epson",

        "modelo": "L6490",

        "tipo": "Impressora",

        "monitor": "netwatch"

    },

    {

        "nome": "Pantum Contabilidade",

        "setor": "Contabilidade",

        "ip": "192.168.0.124",

        "fabricante": "Pantum",

        "modelo": "Pantum",

        "tipo": "Impressora",

        "monitor": "ping"

    },

    {

        "nome": "Pantum Protocolo",

        "setor": "Protocolo",

        "ip": "192.168.0.117",

        "fabricante": "Pantum",

        "modelo": "Pantum",

        "tipo": "Impressora",

        "monitor": "ping"

    },

    {

        "nome": "Canon TI",

        "setor": "TI",

        "ip": "192.168.0.236",

        "fabricante": "Canon",

        "modelo": "GX",

        "tipo": "Impressora",

        "monitor": "ping"

    },

    {

        "nome": "Canon Jurídico",

        "setor": "Jurídico",

        "ip": "10.0.0.79",

        "fabricante": "Canon",

        "modelo": "GX",

        "tipo": "Impressora",

        "monitor": "ping"

    }

]