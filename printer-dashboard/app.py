import os
from flask import Flask, render_template
from config import load_config
from syncthru_mock import get_toner

PRINTERS_JSON = os.path.join(os.path.dirname(__file__), "printers.json")


def create_app(config_path=PRINTERS_JSON):
    app = Flask(__name__)

    @app.route("/")
    def index():
        printers = load_config(config_path)
        accessible = []
        inaccessible = []
        for p in printers:
            level = get_toner(p["ip"])
            if level is None:
                inaccessible.append({"label": p["label"], "toner": None})
            else:
                accessible.append({"label": p["label"], "toner": level})
        all_printers = accessible + inaccessible
        return render_template("index.html", printers=all_printers)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
