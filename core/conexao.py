# ==========================================================
# Conexão Única com o MikroTik
# ==========================================================

from threading import Lock

from core.mikrotik import MikroTik


class ConexaoMikroTik:

    _instancia = None
    _lock = Lock()

    @classmethod
    def obter(cls):
        """
        Retorna uma única instância da conexão com o MikroTik.
        Caso a conexão tenha sido perdida, cria uma nova.
        """

        with cls._lock:

            if cls._instancia is None:

                print("[SIMR] Conectando ao MikroTik...")

                cls._instancia = MikroTik()

                print("[SIMR] Conexão estabelecida.")

            return cls._instancia

    @classmethod
    def reconectar(cls):
        """
        Força uma nova conexão.
        """

        with cls._lock:

            try:

                if cls._instancia is not None:

                    cls._instancia.close()

            except Exception:

                pass

            cls._instancia = None

            return cls.obter()

    @classmethod
    def fechar(cls):
        """
        Encerra a conexão.
        """

        with cls._lock:

            if cls._instancia is not None:

                try:

                    cls._instancia.close()

                except Exception:

                    pass

                cls._instancia = None

                print("[SIMR] Conexão encerrada.")