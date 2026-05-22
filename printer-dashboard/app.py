import os
from flask import Flask, render_template
from config import load_config
from syncthru_mock import get_toner

PRINTERS_JSON = os.path.join(os.path.dirname(__file__), "printers.json")
TONER_THRESHOLD = 10


def create_app(config_path=PRINTERS_JSON):
    app = Flask(__name__)

    @app.route("/")
    def index():
        printers = load_config(config_path)
        critical = []
        for p in printers:
            level = get_toner(p["ip"])
            if level is not None and level <= TONER_THRESHOLD:
                critical.append({"label": p["label"], "toner": level})
        return render_template("index.html", critical=critical)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
