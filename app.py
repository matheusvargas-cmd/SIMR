import os
import sys

from flask import Flask, jsonify, render_template

from core.dashboard import carregar_dashboard


# ==========================================================
# Caminho para PyInstaller
# ==========================================================

def resource_path(relative_path):

    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ==========================================================
# Flask
# ==========================================================

app = Flask(
    __name__,
    template_folder=resource_path("templates"),
    static_folder=resource_path("static")
)


# ==========================================================
# Página Principal
# ==========================================================

@app.route("/")
def index():

    return render_template("index.html")


# ==========================================================
# API Dashboard
# ==========================================================

@app.route("/api/dashboard")
def dashboard():

    return jsonify(carregar_dashboard())


# ==========================================================
# Inicialização
# ==========================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True
    )