# ==========================================================
# SIMR
# Comunicação com o MikroTik
# ==========================================================

import subprocess
import requests

from routeros_api import RouterOsApiPool
from config import MIKROTIK


class MikroTik:

    # ======================================================
    # Construtor
    # ======================================================

    def __init__(self):

        self.pool = RouterOsApiPool(

            host=MIKROTIK["host"],
            username=MIKROTIK["usuario"],
            password=MIKROTIK["senha"],
            port=MIKROTIK["porta"],
            plaintext_login=True

        )

        self.api = self.pool.get_api()

        self._resource = None
        self._netwatch = None
        self._pppoe = None

    # ======================================================
    # Fecha conexão
    # ======================================================

    def close(self):

        try:
            self.pool.disconnect()

        except Exception:
            pass

    # ======================================================
    # Recursos Router
    # ======================================================

    def resource(self):

        if self._resource is None:

            self._resource = self.api.get_resource(
                "/system/resource"
            )

        return self._resource.get()[0]

    # ======================================================
    # Interfaces
    # ======================================================

    def interfaces(self):

        return self.api.get_resource(
            "/interface"
        ).get()

    # ======================================================
    # PPPoE
    # ======================================================

    def pppoe(self):

        if self._pppoe is None:

            self._pppoe = self.api.get_resource(
                "/interface/pppoe-client"
            )

        return self._pppoe.get()

    # ======================================================
    # IP Address
    # ======================================================

    def addresses(self):

        return self.api.get_resource(
            "/ip/address"
        ).get()

    # ======================================================
    # Netwatch
    # ======================================================

    def netwatch(self):

        if self._netwatch is None:

            self._netwatch = self.api.get_resource(
                "/tool/netwatch"
            )

        return self._netwatch.get()

    # ======================================================
    # Host Online
    # ======================================================

    def host_online(self, ip):

        try:

            for host in self.netwatch():

                if host.get("host") == ip:

                    return host.get("status", "").lower() == "up"

            return False

        except Exception:

            return False

    # ======================================================
    # Ping
    # (temporário)
    # ======================================================

    def ping(self, ip):

        try:

            resultado = subprocess.run(

                ["ping", "-n", "1", "-w", "1000", ip],

                capture_output=True,

                text=True

            )

            return resultado.returncode == 0

        except Exception:

            return False

    
# ======================================================
# HTTP via MikroTik
# ======================================================
    def http_online(self, ip):

        print(f"\n[HTTP RouterOS] Testando {ip}")

        try:

            recurso = self.api.get_resource("/tool")

            resultado = recurso.call(
                "fetch",
                {
                    "url": f"http://{ip}",
                    "output": "user",
                    "as-value": "yes",
                    "duration": "3s"
                }
            )

            print(f"[HTTP RouterOS] Resultado: {resultado}")

            if isinstance(resultado, list):

                for item in resultado:

                    if item.get("status") == "finished":
                        return True

            return False

        except Exception as erro:

            print(f"[HTTP RouterOS] Erro: {erro}")

            return False
    # ======================================================
    # Fetch RouterOS
    # (V3)
    # ======================================================

    def fetch_routeros(self, url):

   
        try:

            recurso = self.api.get_resource("/tool")

            resultado = recurso.call(
                "fetch",
                {
                    "url": url,
                    "output": "none"
                }
            )

            for item in resultado:

                if item.get("status") == "finished":
                    return True

            return False

        except Exception as erro:

            print(f"[FETCH RouterOS] Erro: {erro}")

            return False

    # ======================================================
    # Ping RouterOS
    # (V3)
    # ======================================================

    def ping_routeros(self, ip):

        """
        Este método substituirá o ping Windows.

        Utilizará:

        /tool ping

        """

        raise NotImplementedError

    # ======================================================
    # PPPoE Status
    # ======================================================

    def pppoe_status(self, interface):

        try:

            for cliente in self.pppoe():

                if cliente.get("name") == interface:

                    return cliente.get("running", "false") == "true"

            return False

        except Exception:

            return False

    # ======================================================
    # Teste API
    # ======================================================

    def conectado(self):

        try:

            self.resource()

            return True

        except Exception:

            return False

    # ======================================================
    # Informações Gerais
    # ======================================================

    def info(self):

        try:

            return {

                "router": self.resource(),

                "interfaces": self.interfaces(),

                "pppoe": self.pppoe(),

                "netwatch": self.netwatch()

            }

        except Exception:

            return {}